def finance_agent(metrics):
    print("[AGENT] Finance Agent running...")

    revenue_impact = "negative" if metrics["conversion"][-1] < metrics["conversion"][0] else "positive"

    return {
        "impact": revenue_impact
    }