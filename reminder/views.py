# from __future__ import print_function
#
# from django.shortcuts import get_object_or_404
#
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .serializer import *
#
# import datetime
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
#
# from django.utils import timezone
# import json
#
# def Reminder_Overview():
#     api_urls = {
#         '"GET" to connect user email to google calendar' : '/reminder/',
#         '"POST" create a new reminder':'/reminder/',
#         '"DELETE" delete credentials for user':'/deleteCreds/',
#         '"DELETE" delete calendar ID for user':'/deleteCalendar/'
#     }
#     return api_urls
#
# class reminder(APIView):
#     def get(self, request, format=None):
#         if request.user.is_anonymous:
#             return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
#
#         _user = request.user
#
#         SCOPES = ['https://www.googleapis.com/auth/calendar']
#         creds = None
#         if _user.creds:
#             creds = Credentials.from_authorized_user_info(json.loads(_user.creds), SCOPES)
#         if not creds or not creds.valid:
#             if creds and creds.expired and creds.refresh_token:
#                 creds.refresh(Request())
#             else:
#                 flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#                 creds = flow.run_local_server(port=0)
#             _user.creds = creds.to_json()
#             _user.save()
#
#         service = build('calendar', 'v3', credentials=creds)
#
#         _calendar = {
#                 'summary': 'Plants',
#                 'timeZone': 'Asia/Tehran'
#             }
#
#         try:
#             if (_user.calendarID != ''):
#                 calendar = service.calendarList().get(calendarId=_user.calendarID).execute()
#             else:
#                 raise Exception('Invalid calendar')
#         except:
#             calendar = service.calendars().insert(body=_calendar).execute()
#             _user.calendarID = calendar['id']
#             _user.save()
#
#         return Response("Auth completed !")
#
#     def post(self, request, format=None):
#         if request.user.is_anonymous:
#             return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
#
#         _user = request.user
#
#         SCOPES = ['https://www.googleapis.com/auth/calendar']
#         data = EventSerializer(data=request.data)
#         if data.is_valid():
#             creds = None
#             if _user.creds:
#                 creds = Credentials.from_authorized_user_info(json.loads(_user.creds), SCOPES)
#             if not creds or not creds.valid:
#                 if creds and creds.expired and creds.refresh_token:
#                     creds.refresh(Request())
#                 else:
#                     flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#                     creds = flow.run_local_server(port=0)
#                 _user.creds = creds.to_json()
#                 _user.save()
#
#             service = build('calendar', 'v3', credentials=creds)
#
#             _calendar = {
#                 'summary': 'Plants',
#                 'timeZone': 'Asia/Tehran'
#             }
#
#             try:
#                 if (_user.calendarID != ''):
#                     calendar = service.calendarList().get(calendarId=_user.calendarID).execute()
#                 else:
#                     raise Exception('Invalid calendar')
#             except:
#                 calendar = service.calendars().insert(body=_calendar).execute()
#                 _user.calendarID = calendar['id']
#                 _user.save()
#
#             event = service.events().insert(calendarId=_user.calendarID, body=data.data).execute()
#
#             return Response(data.data)
#         return Response(data.errors, status=400)
#
# class deleteCreds(APIView):
#     def delete(self, request, format=None):
#         if request.user.is_anonymous:
#             return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
#
#         _user = request.user
#         _user.creds = None
#         _user.save()
#         return Response("Email disconnected successfully !")
#
# class deleteCalendarID(APIView):
#     def delete(self, request, format=None):
#         if request.user.is_anonymous:
#             return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
#         _user = request.user
#         if not _user.calendarID:
#             return Response("you have no calendar !")
#         else :
#             creds = None
#             if _user.creds:
#                 creds = Credentials.from_authorized_user_info(json.loads(_user.creds), SCOPES)
#             if not creds or not creds.valid:
#                 if creds and creds.expired and creds.refresh_token:
#                     creds.refresh(Request())
#                 else:
#                     flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#                     creds = flow.run_local_server(port=0)
#                 _user.creds = creds.to_json()
#                 _user.save()
#
#             service = build('calendar', 'v3', credentials=creds)
#             service.calendarList().delete(calendarId='calendarId').execute()
#         _user.calendarID = None
#         _user.save()
#         return Response("Calendar deleted successfully !")
