🌍 AI Travel Planner (Weather-Aware & Hotel-Integrated)

An AI-powered, modular travel planning system that generates personalized itineraries, integrates real-time weather forecasts, automatically replans trips during bad weather, recommends hotels with live pricing via Amadeus, and provides booking links and calendar exports.

🚀 Features

🧠 AI Itinerary Generation – Day-wise travel plans using LLMs

🌦 Real-Time Weather Integration – Daily forecasts using WeatherAPI

🔄 Weather-Aware Replanning – Automatically adjusts plans for bad weather

🏨 Hotel Recommendations – Real hotels & pricing via Amadeus API

🤖 Hotel Agent Reasoning – AI ranks hotels based on itinerary & weather

🔗 Booking Redirects – One-click booking via Google Hotels

📅 Calendar Export – Download trip as .ics file

🧩 Modular Architecture – Clean separation of agents, services, and utilities

🗂 Project Structure
Travel_Agent/
│
├── app.py
├── requirements.txt
│
├── agents/
│   ├── planner_agenty.py
│   └── hotel_agents.py
│
├── services/
│   ├── weather_services.py
│   └── amadeus_service.py
│
├── utils/
│   ├── itinerary_utils.py
│   └── booking_utils.py

🛠 Tech Stack

Python 3.9+

Streamlit – Web UI

Ollama + Agno – Multi-agent AI system

WeatherAPI.com – Free weather forecasts

Amadeus API – Hotel availability & pricing

iCalendar – Calendar export

🔑 API Requirements

You need free API keys for:

WeatherAPI – https://www.weatherapi.com

Amadeus Developers – https://developers.amadeus.com

⚠️ No paid APIs required.

⚙️ Installation & Setup
git clone <repo-url>
cd Travel_Agent
pip install -r requirements.txt


Install and run Ollama separately:

ollama run llama3.2

▶️ Run the Application
streamlit run app.py


Then open:

http://localhost:8501

🧠 How It Works (High-Level Flow)

User enters destination, dates, and API keys

Planner Agent generates itinerary

Weather service fetches daily forecast

System detects bad weather and replans if needed

Amadeus fetches real hotel data with prices

Hotel Agent ranks hotels using itinerary + weather

User views hotels, booking links, and downloads calendar

📌 Notes

Booking is handled via redirect links, not in-app payments

Designed for scalability and future agent extensions

Suitable for portfolio, research, or startup prototyping

📈 Future Enhancements

Structured itinerary JSON

Per-day hotel suggestions

Cost breakdown per trip/day

Hotel images & ratings

Trip confidence score

📄 License

This project is open-source and intended for educational and prototyping purposes.
