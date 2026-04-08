def marketing_agent(sentiment):
    print("[AGENT] Marketing running...")

    if sentiment["overall"] == "negative":
        return {
            "external": "Acknowledge issues publicly",
            "internal": "Prepare crisis communication"
        }
    else:
        return {
            "external": "Promote feature",
            "internal": "Scale campaigns"
        }