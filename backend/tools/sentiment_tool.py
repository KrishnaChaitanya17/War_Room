def analyze_sentiment(feedbacks):
    print("[TOOL] Running sentiment analysis...")

    positive_words = ["good", "great", "amazing", "loved", "nice"]
    negative_words = ["bad", "bug", "crash", "slow", "error", "fail"]

    pos, neg = 0, 0

    for f in feedbacks:
        f = f.lower()
        if any(w in f for w in positive_words):
            pos += 1
        elif any(w in f for w in negative_words):
            neg += 1

    return {
        "positive": pos,
        "negative": neg,
        "overall": "negative" if neg > pos else "positive"
    }