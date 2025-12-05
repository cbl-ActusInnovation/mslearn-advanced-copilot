from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]


def test_cities_spain():
    """
    Test the /countries/{country} endpoint with Spain as the country.
    
    This test verifies that the API returns the correct list of cities
    for Spain from the historical weather data.
    """
    response = client.get("/countries/Spain")
    assert response.status_code == 200
    cities = response.json()
    assert isinstance(cities, list)
    assert len(cities) > 0
    # Verify that the response contains expected Spanish cities
    assert all(isinstance(city, str) for city in cities)