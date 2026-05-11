from textblob import TextBlob
from collections import Counter
from db import messages

# ---------------- SENTIMENT ANALYSIS ----------------
def sentiment_analysis():

    data = list(messages.find())

    positive = 0
    negative = 0
    neutral = 0

    for msg in data:

        text = msg["message"]

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0:
            positive += 1

        elif polarity < 0:
            negative += 1

        else:
            neutral += 1

    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }

# ---------------- TRENDING WORDS ----------------
def trending_keywords():

    data = list(messages.find())

    words = []

    for msg in data:

        text = msg["message"].lower()

        words.extend(text.split())

    common = Counter(words).most_common(10)

    return common
