

def test_profile_success(client):

    response = client.get("/profile")

    assert response.status_code == 200

    data = response.json()

    assert "message" in data
    assert data["user_id"] == 1
    assert "is_admin" in data
    assert data["is_admin"] is True


def test_admin_success(client):
    response = client.get("/admin")

    assert response.status_code == 200
    data = response.json()

    assert data["message"] == "Welcome to admin panel"
