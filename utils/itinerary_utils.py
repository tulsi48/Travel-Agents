import re
from datetime import timedelta
from icalendar import Calendar, Event

def extract_days(itinerary_text):
    pattern = re.compile(r"Day (\d+)[:\s]+(.*?)(?=Day \d+|$)", re.DOTALL)
    return pattern.findall(itinerary_text)

def generate_ics(itinerary, start_date):
    cal = Calendar()
    cal.add("prodid", "-//AI Travel Planner//")
    cal.add("version", "2.0")

    for d, content in extract_days(itinerary):
        date = start_date + timedelta(days=int(d) - 1)
        e = Event()
        e.add("summary", f"Day {d}")
        e.add("description", content.strip())
        e.add("dtstart", date.date())
        e.add("dtend", date.date())
        cal.add_component(e)

    return cal.to_ical()
