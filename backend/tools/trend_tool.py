def trend_score(metrics):
    print("[TOOL] Calculating trend score...")

    score = 0
    trend_details = {}

    for key, values in metrics.items():
        if values[-1] < values[0]:
            score -= 1
            trend_details[key] = "decreasing"
        else:
            score += 1
            trend_details[key] = "increasing"

    print("[TOOL] Trend details:", trend_details)

    return score