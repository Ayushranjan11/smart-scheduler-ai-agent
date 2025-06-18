from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
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
    return service

def find_available_slot(service, preferred_start, duration_minutes):
    calendar_id = 'primary'
    preferred_end = preferred_start + timedelta(minutes=duration_minutes)

    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=preferred_start.isoformat() + 'Z',
        timeMax=preferred_end.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        return preferred_start, preferred_end
    return None

def create_calendar_event(service, start_time, end_time):
    event = {
        'summary': 'Scheduled Meeting',
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
    }

    try:
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        print("📅 Event created:", event_result.get('htmlLink'))
        return event_result
    except Exception as e:
        print("❌ Failed to create event:", e)
        return None
