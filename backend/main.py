print("🚀 Starting War Room System...")
import json
from orchestrator.coordinator import run_system

metrics = json.load(open("data/metrics.json"))
feedback = json.load(open("data/feedback.json"))

result = run_system(metrics, feedback)

print("\n FINAL OUTPUT:\n")
print(json.dumps(result, indent=2))

with open("output/final_output.json", "w") as f:
    json.dump(result, f, indent=2)