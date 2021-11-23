from __future__ import print_function

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *

import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

@api_view(['POST'])
def reminder(request):
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
        
        calendar = {
            'summary': 'plants',
            'timeZone': 'Asia/Tehran'
        }
        
        try:
            created_calendar = service.calendars().get(calendarId='KEY').execute()
        except:
            created_calendar = service.calendars().insert(body=calendar).execute()
        event = service.events().insert(calendarId=created_calendar['id'], body=data.data).execute()

        return Response(data.data)
    
    return Response(data.errors)