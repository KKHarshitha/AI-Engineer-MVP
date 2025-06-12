import requests

BASE_URL = "http://127.0.0.1:8000"

def test_spa_booking():
    payload = {"voice_text": "Hey Conci, book a spa at 5 PM"}
    response = requests.post(f"{BASE_URL}/voice", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["intent"]["intent"] == "spa_booking"
    print("✅ Spa booking test passed")

def test_towel_request():
    payload = {"voice_text": "Hey Conci, I need towels"}
    response = requests.post(f"{BASE_URL}/voice", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["intent"]["intent"] == "towel_request"
    assert data["hotticket"]["status"] == "created"
    print("✅ Towel request test passed")

def test_lights_off():
    payload = {"voice_text": "Hey Conci, turn off the lights"}
    response = requests.post(f"{BASE_URL}/voice", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["intent"]["intent"] == "lights_off"
    assert data["mqtt"]["message"] == "OFF"
    print("✅ Lights off test passed")

def test_privacy_mode():
    payload = {"voice_text": "Hey Conci, privacy mode"}
    response = requests.post(f"{BASE_URL}/voice", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["intent"]["intent"] == "privacy_mode"
    print("✅ Privacy mode test passed")

if __name__ == "__main__":
    test_spa_booking()
    test_towel_request()
    test_lights_off()
    test_privacy_mode()
