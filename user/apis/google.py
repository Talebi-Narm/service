from typing import Tuple

import requests
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import transaction
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from user.serializers.google import GoogleLoginSerializer

GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'


def google_validate_id_token(email: str, id_token: str) -> bool:
    # Reference: https://developers.google.com/identity/sign-in/web/backend-auth#verify-the-integrity-of-the-id-token
    response = requests.get(
        GOOGLE_ID_TOKEN_INFO_URL,
        params={'id_token': id_token}
    )

    data = response.json()

    if response.status_code != status.HTTP_200_OK:
        raise ValidationError('id_token is invalid.')

    audience = data['aud']

    if audience != settings.GOOGLE_OAUTH2_CLIENT_ID:
        raise ValidationError('Invalid audience.')

    if data['email'] != email:
        raise ValidationError('Invalid email.')

    return True


def user_create(email, password=None, **extra_fields) -> User:
    extra_fields = {
        'username': email,
        'is_active': True,
        'is_staff': False,
        'is_superuser': False,
        **extra_fields
    }

    user = User(email=email, **extra_fields)

    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()

    user.full_clean()
    user.save()

    return user


@transaction.atomic
def user_get_or_create(*, email: str, **extra_data) -> Tuple[User, bool]:
    user = User.objects.filter(email=email).first()

    if user:
        return user, False

    return user_create(email=email, **extra_data), True


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class GoogleLogin(generics.GenericAPIView):
    serializer_class = GoogleLoginSerializer

    @extend_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            google_validate_id_token(
                email=serializer.validated_data['email'],
                id_token=serializer.validated_data['id_token']
            )
        except ValidationError as e:
            message = f'Validation failed: {e.message}'
            return Response({'detail': message}, status=status.HTTP_401_UNAUTHORIZED)

        serializer.validated_data.pop('id_token')
        user, _ = user_get_or_create(**serializer.validated_data)

        tokens = get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)
