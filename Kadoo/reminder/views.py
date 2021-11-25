from __future__ import print_function

from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *

import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from django.utils import timezone

@api_view(['POST'])
def reminder(request):
    if request.user.is_anonymous:
        return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)

    _user = request.user

    SCOPES = ['https://www.googleapis.com/auth/calendar']
    data = EventSerializer(data=request.data)
    if data.is_valid():
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)
        
        _calendar = {
            'summary': 'Plants',
            'timeZone': 'Asia/Tehran'
        }
        
        try:
            calendar = service.calendars().get(calendarId=_user.calnderID).execute()
        except:
            calendar = service.calendars().insert(body=_calendar).execute()
            _user.calenderID = calendar['id']
        
        print(_user.calnderID)
        print(calendar['id'])
        event = service.events().insert(calendarId=calendar['id'], body=data.data).execute()

        return Response(data.data)
    
    return Response(data.errors)