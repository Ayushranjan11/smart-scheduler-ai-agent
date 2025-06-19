from datetime import datetime
import dateparser

def parse_duration(text):
    words = text.split()
    for word in words:
        if word.isdigit():
            return int(word)
    return None

def parse_datetime(text):
    dt = dateparser.parse(text, settings={"PREFER_DATES_FROM": "future"})
    if not dt:
        print("❌ Could not parse date hint.")
    return dt
