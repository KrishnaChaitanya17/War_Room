def pm_agent(data, sentiment, finance):
    print("[AGENT] PM Agent making decision...")

    if sentiment["overall"] == "negative" and "crash_rate" in data["issues"]:
        decision = "Roll Back"
    elif sentiment["overall"] == "negative":
        decision = "Pause"
    else:
        decision = "Proceed"

    return decision