
import requests

BASE_URL = "https://reqres.in/api/users"

# Sample test users (without ID initially)
test_users = [
    {"name": "Alice", "job": "Tester"},
    {"name": "Bob", "job": "Developer"},
    {"name": "Charlie", "job": "Manager"},
]

def test_create_user(user):
    response = requests.post(BASE_URL, json=user)
    assert response.status_code == 201
    user_id = response.json().get("id")
    print(f"[CREATE] User {user['name']} created with ID {user_id}")
    return user_id

def test_get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print(f"[GET] User with ID {user_id} retrieved successfully.")
    else:
        print(f"[GET] User with ID {user_id} not found (Status: {response.status_code})")

def test_delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    assert response.status_code == 204
    print(f"[DELETE] User with ID {user_id} deleted successfully.")

if __name__ == "__main__":
    for user in test_users:
        user_id = test_create_user(user)
        test_get_user(user_id)
        test_delete_user(user_id)
