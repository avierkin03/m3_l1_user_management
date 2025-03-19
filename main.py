from fastapi import FastAPI

app = FastAPI()


class User:
    def __init__(self, user_id: int, username: str, email: str):
        self.id = user_id
        self.username = username
        self.email = email


users = [
    User(user_id=1, username="john_doe", email="john@example.com"),
    User(user_id=2, username="jane_doe", email="jane@example.com")
]


# повертає інформацію про користувача за його ідентифікатором
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}


# повертає список всіх користувачів
@app.get("/users")
def get_all_users():
    return users


# дозволяє створити нового користувача за допомогою POST-запиту з обов'язковими полями username та email
@app.post("/create_user")
def create_user(username: str, email: str):
    user_id = len(users) + 1
    new_user = User(user_id = user_id, username = username, email = email)
    users.append(new_user)
    return new_user
