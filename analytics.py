from db import activity, messages, users
from datetime import datetime, timedelta
import pandas as pd
def export_messages():

    data = list(messages.find())

    df = pd.DataFrame(data)

    df.to_csv(
        "exports/messages_report.csv",
        index=False
    )

    return "Export Complete"

# ---------------- USER ACTIVITY ----------------
def user_activity_summary():

    pipeline = [
        {
            "$group": {
                "_id": "$username",
                "actions": {"$sum": 1}
            }
        },
        {
            "$sort": {"actions": -1}
        }
    ]

    return list(activity.aggregate(pipeline))

# ---------------- HOURLY ACTIVITY ----------------
def hourly_activity():

    pipeline = [
        {
            "$group": {
                "_id": {"$hour": "$timestamp"},
                "count": {"$sum": 1}
            }
        }
    ]

    return list(activity.aggregate(pipeline))

# ---------------- MESSAGE STATS ----------------
def message_stats():

    total = messages.count_documents({})

    last_24h = messages.count_documents({
        "timestamp": {
            "$gte": datetime.utcnow() - timedelta(days=1)
        }
    })

    return {
        "total_messages": total,
        "last_24h": last_24h
    }

# ---------------- DAILY ACTIVE USERS ----------------
def dau():

    today = datetime.utcnow() - timedelta(days=1)

    users_count = activity.distinct(
        "username",
        {
            "timestamp": {"$gte": today}
        }
    )

    return len(users_count)

# ---------------- USER GROWTH ----------------
def user_growth():

    pipeline = [
        {
            "$group": {
                "_id": {
                    "$dateToString": {
                        "format": "%Y-%m-%d",
                        "date": "$created_at"
                    }
                },
                "count": {"$sum": 1}
            }
        }
    ]

    return list(users.aggregate(pipeline))
