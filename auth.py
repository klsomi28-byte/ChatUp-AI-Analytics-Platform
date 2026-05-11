import jwt
import bcrypt

from db import users
from config import SECRET_KEY

print("AUTH MODULE LOADED")

# ==============================
# REGISTER FUNCTION
# ==============================
def register(username, password):

    existing = users.find_one({
        "username": username
    })

    if existing:
        return "User already exists"

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    users.insert_one({
        "username": username,
        "password": hashed_password,
        "connections": []
    })

    return "Registration Successful"

# ==============================
# LOGIN FUNCTION
# ==============================
def login(username, password):

    user = users.find_one({
        "username": username
    })

    if not user:
        return None

    stored_password = user["password"]

    if bcrypt.checkpw(
        password.encode(),
        stored_password
    ):

        token = jwt.encode(
            {"user": username},
            SECRET_KEY,
            algorithm="HS256"
        )

        return token

    return None

# ==============================
# VERIFY TOKEN
# ==============================
def verify(token):

    try:

        data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return data["user"]

    except Exception as e:

        print("JWT ERROR:", e)

        return None

# ==============================
# MAIN PROGRAM
# ==============================
if __name__ == "__main__":

    print("AUTH SYSTEM STARTED")

    while True:

        print("\n========== CHAT AUTH ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        # ---------------- REGISTER ----------------
        if choice == "1":

            username = input("Enter username: ")
            password = input("Enter password: ")

            result = register(username, password)

            print("\n" + result)

        # ---------------- LOGIN ----------------
        elif choice == "2":

            username = input("Enter username: ")
            password = input("Enter password: ")

            token = login(username, password)

            if token:

                print("\nLOGIN SUCCESSFUL")
                print("\nYOUR JWT TOKEN:\n")
                print(token)

            else:

                print("\nInvalid username or password")

        # ---------------- EXIT ----------------
        elif choice == "3":

            print("\nExiting Program...")
            break

        else:

            print("\nInvalid choice")
