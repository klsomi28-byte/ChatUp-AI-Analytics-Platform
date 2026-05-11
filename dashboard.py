from flask import Flask, jsonify

from analytics import (
    user_activity_summary,
    hourly_activity,
    message_stats,
    dau,
    user_growth
)

from ai_analysis import (
    sentiment_analysis,
    trending_keywords
)

app = Flask(__name__)

@app.route("/")
def home():

    return jsonify({

        "user_activity":
            user_activity_summary(),

        "hourly_activity":
            hourly_activity(),

        "message_stats":
            message_stats(),

        "daily_active_users":
            dau(),

        "user_growth":
            user_growth(),

        "sentiment":
            sentiment_analysis(),

        "trending_keywords":
            trending_keywords()
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
