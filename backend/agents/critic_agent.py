def critic_agent(data):
    print("[AGENT] Critic Agent reviewing...")

    concerns = []

    if len(data["issues"]) > 3:
        concerns.append("Too many unstable metrics")

    return concerns