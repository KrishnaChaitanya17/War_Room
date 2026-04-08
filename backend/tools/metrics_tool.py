import numpy as np 

def detect_anomalies(metrics):
    print("[TOOL] Running anomaly detection...")
    result = {}

    for key, values in metrics.items():
        trend = "decreasing" if values[-1] < values[0] else "increasing"
        spike = max(values) > (np.mean(values) * 1.3)

        result[key] = {
            "trend": trend,
            "spike": spike,
            "latest": values[-1]
        }

    return result