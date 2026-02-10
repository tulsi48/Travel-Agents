import streamlit as st
from datetime import datetime, timedelta

from agents.planner_agenty import get_planner_agent
from agents.hotel_agents import get_hotel_agent

from services.weather_services import get_weather_forecast, build_weather_rows
from services.amadeus_service import get_amadeus_token, get_city_code, search_hotels

from utils.itinerary_utils import generate_ics
from utils.booking_utils import build_booking_link

st.title("🌍 AI Travel Planner")

destination = st.text_input("Destination")
start_date = st.date_input("Start date", datetime.today())
days = st.number_input("Number of days", 1, 14, 5)

weather_key = st.text_input("Weather API Key", type="password")
amadeus_key = st.text_input("Amadeus API Key", type="password")
amadeus_secret = st.text_input("Amadeus API Secret", type="password")

if st.button("Plan Trip"):
    planner = get_planner_agent()
    hotel_agent = get_hotel_agent()

    itinerary = planner.run(f"{destination} for {days} days", stream=False).content
    st.subheader("📄 Itinerary")
    st.write(itinerary)

    forecast = get_weather_forecast(destination, weather_key, days)
    weather_rows = build_weather_rows(
        datetime.combine(start_date, datetime.min.time()),
        forecast,
        days
    )

    st.subheader("🌦 Weather")
    st.write(weather_rows)

    token = get_amadeus_token(amadeus_key, amadeus_secret)
    city_code = get_city_code(destination, token)

    hotels = search_hotels(
        city_code,
        start_date.isoformat(),
        (start_date + timedelta(days=days)).isoformat(),
        token
    )

    hotel_data = [
        {
            "name": h["hotel"]["name"],
            "price": h["offers"][0]["price"]["total"],
            "currency": h["offers"][0]["price"]["currency"]
        }
        for h in hotels[:5]
    ]

    prompt = f"""
Itinerary:
{itinerary}

Weather:
{weather_rows}

Hotels:
{hotel_data}

Rank the hotels and explain.
"""
    ranking = hotel_agent.run(prompt, stream=False).content

    st.subheader("🏨 Hotels")
    st.write(ranking)

    for h in hotel_data:
        st.markdown(
            f"**{h['name']}** – {h['price']} {h['currency']}  \n"
            f"[Book]({build_booking_link(h['name'], destination)})"
        )

    st.download_button(
        "Download Calendar",
        generate_ics(itinerary, datetime.combine(start_date, datetime.min.time())),
        "trip.ics",
        "text/calendar"
    )
