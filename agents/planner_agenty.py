from agno.agent import Agent
from agno.models.ollama import Ollama

def get_planner_agent():
    return Agent(
        name="Planner",
        model=Ollama(id="llama3.2"),
        instructions=[
            "Create a realistic day-wise travel itinerary.",
            "Label days clearly as Day 1, Day 2, etc.",
            "Be practical and concise."
        ]
    )
