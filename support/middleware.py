from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed


class TokenAuthMiddleware:
    """
    Custom middleware that takes a token from the query string and authenticates via SimpleJWT.
    """

    def __init__(self, app):
        # Store the ASGI application we were passed
        self.app = app

    async def __call__(self, scope, receive, send):
        # Look up user from query string (you should also do things like
        # checking if it is a valid user ID, or if scope["user"] is already
        # populated).
        query_params = parse_qs(scope["query_string"].decode())
        if "token" not in query_params.keys():
            await self.send_error_message(send, "Missing token in params")
            return

        token = query_params["token"][0]
        scope["token"] = token
        user = None
        try:
            user = await self.get_user(scope)
        except InvalidToken:
            message = "Invalid token provided"
            await self.send_error_message(send, message)
            return
        except AuthenticationFailed:
            message = "Authentication failed"
            await self.send_error_message(send, message)
            return

        print(f"Authenticated user: {user}")
        scope["user"] = user
        return await self.app(scope, receive, send)

    @staticmethod
    async def send_error_message(send, message):
        await send(
            {
                "type": "websocket.close",
                "text": message,
            }
        )

    @staticmethod
    @database_sync_to_async
    def get_user(scope):
        raw_token = scope["token"]
        jwt_authenticator = JWTAuthentication()
        validated_token = jwt_authenticator.get_validated_token(raw_token)
        user = jwt_authenticator.get_user(validated_token)
        return user
