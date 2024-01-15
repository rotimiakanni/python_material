from fastapi.testclient import TestClient
from main import app
from user_service import UserService
from unittest.mock import patch


client = TestClient(app)


def test_read_items():
    response = client.get("/items/", params={"token": "secret"})

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"name": "Item 1"},
            {"name": "item 2"},
        ]
    }


def test_read_items_invalid_token():
    response = client.get("/items/", params={"token": "invalid"})

    assert response.status_code == 403
    assert response.json() == {"detail": "Unauthorized"}


# Mocking a service
def test_read_users():
    mock_users = [
        {"username": "new user 1"},
        {"username": "new user 2"},
    ]

    # Mocking the user_service dependency
    with patch("main.user_service", spec=UserService) as mock_user_service:
        mock_user_service.get_users_from_db.return_value = mock_users

        response = client.get("/users/", params={"token": "secret"})
        assert response.status_code == 200
        assert response.json() == {"users": mock_users}

        # Asserting the user_service method was called
        mock_user_service.get_users_from_db.assert_called_once()
