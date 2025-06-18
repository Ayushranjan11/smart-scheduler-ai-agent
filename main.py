import os
import re
from datetime import datetime
from voice_utils import speak, listen
from google_calendar_tool import authenticate_google_calendar, find_available_slot, create_calendar_event
from dateutil import parser

# Start the agent
print("🔄 Starting Smart Scheduler Agent...")

# Initialize Google Calendar service
service = authenticate_google_calendar()

def get_valid_input(prompt_text):
    while True:
        speak(prompt_text)
        text = listen()
        if text:
            return text
        speak("I didn't catch that. Please repeat.")

# Step 1: Ask user what they want
user_input = get_valid_input("Hello! What do you want to schedule?")
if "meeting" not in user_input.lower():
    speak("Currently, I only support scheduling meetings.")
    exit()

# Step 2: Ask for meeting duration
duration_text = get_valid_input("How long should the meeting be in minutes?")
duration_match = re.search(r"\d+", duration_text)
if duration_match:
    duration = int(duration_match.group())
else:
    speak("Sorry, I couldn't understand the duration. Please restart.")
    exit()

# Step 3: Ask for preferred time
parsed_datetime = None
while parsed_datetime is None:
    time_text = get_valid_input("Please tell me the day and time you want the meeting.")
    try:
        parsed_datetime = parser.parse(time_text, fuzzy=True)
        print(f"🧠 Parsed datetime: {parsed_datetime}")
    except:
        speak("Sorry, I couldn't understand the time. Please try again with a clear day and time.")
        parsed_datetime = None

# Step 4: Find available slots
speak("Finding available slots...")
slot = find_available_slot(service, parsed_datetime, duration)
if not slot:
    speak("Sorry, I couldn't find any matching slot. Try suggesting a different time or duration.")
    exit()

start_time, end_time = slot
speak(f"Shall I schedule your meeting on {start_time.strftime('%A at %I:%M %p')}?")
confirmation = listen()

if "yes" in confirmation.lower():
    created_event = create_calendar_event(service, start_time, end_time)
    if created_event:
        speak(f"Your meeting has been scheduled on {start_time.strftime('%A at %I:%M %p')}.")
    else:
        speak("Something went wrong while scheduling. Please try again.")
else:
    speak("Okay, no meeting scheduled.")
