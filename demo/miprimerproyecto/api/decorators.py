from builtins import Exception

import base64
from django.http import HttpResponse
from functools import wraps

from app.logger import EmployeeLogger


def http_basic_auth(func):
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            allowed_users = {
                'helloworld': 'VrDlKsoRlluYuQkoFIdcYoFS9w1XCT47',
            }
            read_only_users = [

            ]
            authmeth, auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            if authmeth.lower() == 'basic':
                try:
                    auth = base64.b64decode(auth).decode()
                except Exception as e:
                    EmployeeLogger.log("http_basic_auth() - error decoding base64 auth string: {0}".format(e))
                    return HttpResponse(status=400, reason="Authorization string does not decode")
                username, password = auth.split(':', 1)
                EmployeeLogger.log('http_basic_auth() - username: {0}'.format(username))
                if username in allowed_users and password == allowed_users[username]:
                    EmployeeLogger.log("http_basic_auth() - user {0} authenticated".format(username))
                    EmployeeLogger.log(
                        "http_basic_auth() - calling function '{0}' with request method {1}".format(func.__name__,
                                                                                                    request.method))
                    # Handle read-only users
                    if username in read_only_users:
                        # Allow access to any API using the GET method
                        if request.method == 'GET':
                            pass
                        # Allow access to the members_get_or_update API using the POST method (it's read-only)
                        elif request.method == 'POST':
                            pass
                        # Otherwise deny access
                        else:
                            EmployeeLogger.log(
                                "http_basic_auth() - read-only user '{}' not authorized to access '{}' with method '{}'".format(
                                    username, func.__name__, request.method))
                            return HttpResponse(status=401, reason="Read only user not authorized")

                    return func(request, *args, **kwargs)
                else:
                    EmployeeLogger.log("http_basic_auth() - user {0} failed authentication".format(username))
        response = HttpResponse(status=401)
        return response

    return _decorator
