def risk_agent(data):
    print("[AGENT] Risk Agent running...")

    risks = []
    mitigations = []

    if "crash_rate" in data["issues"]:
        risks.append("High crash rate")
        mitigations.append("Hotfix deployment")

    if "api_latency" in data["issues"]:
        risks.append("Latency spike")
        mitigations.append("Optimize backend")

    return list(zip(risks, mitigations))