import pytest
import copy
from fastapi.testclient import TestClient
from src.app import app, activities


# Define fresh baseline activities
FRESH_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball team for intramural and regional tournaments",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu", "alex@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn tennis skills and participate in friendly matches",
        "schedule": "Wednesdays and Saturdays, 3:00 PM - 4:30 PM",
        "max_participants": 16,
        "participants": ["noah@mergington.edu"]
    },
    "Drama Club": {
        "description": "Perform in theatrical productions and develop acting skills",
        "schedule": "Tuesdays and Thursdays, 4:30 PM - 6:00 PM",
        "max_participants": 25,
        "participants": ["isabella@mergington.edu", "liam@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and other visual arts techniques",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["ava@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills through competitive debate",
        "schedule": "Mondays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts through hands-on activities",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["ethan@mergington.edu"]
    }
}


@pytest.fixture
def client():
    """Provide a TestClient with fresh app state for each test"""
    # Reset activities to fresh state before test
    activities.clear()
    activities.update(copy.deepcopy(FRESH_ACTIVITIES))
    
    yield TestClient(app)
    
    # Reset after test
    activities.clear()
    activities.update(copy.deepcopy(FRESH_ACTIVITIES))
