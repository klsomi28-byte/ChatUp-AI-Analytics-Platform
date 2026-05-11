from db import connections, users

# ---------------- SEND REQUEST ----------------
def send_request(sender, receiver):

    existing = connections.find_one({
        "from": sender,
        "to": receiver
    })

    if existing:
        return "Already sent"

    connections.insert_one({
        "from": sender,
        "to": receiver,
        "status": "pending"
    })

    return "Request Sent"

# ---------------- ACCEPT REQUEST ----------------
def accept_request(sender, receiver):

    connections.update_one(
        {
            "from": sender,
            "to": receiver
        },
        {
            "$set": {"status": "accepted"}
        }
    )

    users.update_one(
        {"username": sender},
        {"$push": {"connections": receiver}}
    )

    users.update_one(
        {"username": receiver},
        {"$push": {"connections": sender}}
    )

# ---------------- GET CONNECTIONS ----------------
def get_connections(user):

    u = users.find_one({"username": user})

    if not u:
        return []

    return u.get("connections", [])
