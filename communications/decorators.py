import jwt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

def jwt_required(view_func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            raise AuthenticationFailed('No authentication token provided')
        try:
            token = auth_header.split(' ')[1]
            authenticator = JWTAuthentication()
            user, token = authenticator.authenticate(request)
            request.user = user
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        return view_func(request, *args, **kwargs)
    return wrapper