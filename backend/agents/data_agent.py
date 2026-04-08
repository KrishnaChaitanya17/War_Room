from tools.metrics_tool import detect_anomalies
from tools.trend_tool import trend_score

def data_agent(metrics):
    print("[AGENT] Data Analyst running...")

    anomalies = detect_anomalies(metrics)
    trend = trend_score(metrics)

    issues = [
    k for k, v in anomalies.items()
    if v.get("anomaly", False) or v.get("trend") == "decreasing"
]

    return {
        "anomalies": anomalies,
        "issues": issues,
        "trend_score": trend
    }