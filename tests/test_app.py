def test_root_redirect(client):
    """Test that root endpoint redirects to static/index.html"""
    # Arrange
    expected_redirect_url = "/static/index.html"
    
    # Act
    response = client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_redirect_url


def test_get_activities(client):
    """Test that get activities returns all activities with correct structure"""
    # Arrange
    expected_activity_count = 9
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    assert len(data) == expected_activity_count
    assert "Chess Club" in data
    assert "description" in data["Chess Club"]
    assert "schedule" in data["Chess Club"]
    assert "max_participants" in data["Chess Club"]
    assert "participants" in data["Chess Club"]


def test_signup_for_activity(client):
    """Test that a student can sign up for an activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    expected_initial_count = 2
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    activities_after = client.get("/activities").json()
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"
    assert email in activities_after[activity_name]["participants"]
    assert len(activities_after[activity_name]["participants"]) == expected_initial_count + 1


def test_unregister_from_activity(client):
    """Test that a student can unregister from an activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    initial_count = 2
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    activities_after = client.get("/activities").json()
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities_after[activity_name]["participants"]
    assert len(activities_after[activity_name]["participants"]) == initial_count - 1
