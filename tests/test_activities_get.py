def test_get_activities_returns_expected_structure(client):
    # Arrange
    endpoint = "/activities"
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert required_keys.issubset(data["Chess Club"].keys())
    assert isinstance(data["Chess Club"]["participants"], list)
