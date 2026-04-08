# 🧠 AI/ML Engineer Assessment – War Room Decision System

## 📌 Overview

This project implements a **multi-agent AI system** that simulates a cross-functional "war room" during a product launch.  
The system analyzes product metrics and user feedback to generate a structured decision:

➡️ **Proceed / Pause / Roll Back**

along with risks, actions, and communication strategy.

---

## ⚙️ System Architecture

The system is designed using a **multi-agent architecture**:

- **Data Analyst Agent** → Analyzes metrics, trends, anomalies  
- **Product Manager Agent** → Makes final decision  
- **Marketing Agent** → Generates communication strategy  
- **Risk Agent** → Identifies risks and mitigations  
- **Finance Agent** → Evaluates revenue impact  
- **Critic Agent** → Reviews assumptions and flags concerns  

A central **Coordinator** orchestrates all agents.

---

## 🛠️ Tools Used

- **Metrics Tool** → Detects anomalies and trends  
- **Trend Tool** → Computes overall trend score  
- **Sentiment Tool** → Analyzes user feedback sentiment  

All tools are programmatically invoked by agents.

---

## 📊 Input Data

### 1. Metrics (7-day time series)
- DAU
- Retention (D7)
- Conversion Rate
- Crash Rate
- API Latency
- Support Tickets
- Payment Failures

### 2. User Feedback
- 20+ entries (positive, neutral, negative)

### 3. Release Notes
- Feature changes and known risks

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd backend

### 2. Create virutal environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the system 

python main.py

```
---

## Output

The system generates a structured JSON output:

 - Decision ( Proceed / Pause / Roll Back)
 - Rationale ( metrics + sentiment)
 - Risk Register  (with mitigation)
 - Action Plan ( 24–48 hours)
 - Communication Plan
 - Confidence Score
 - Confidence Improvement Suggestions

---

### 🔍 Key Features

 - ✅ Multi-agent orchestration
 - ✅ Tool-based reasoning
 - ✅ Dynamic, data-driven decisions
 - ✅ Traceable execution ( logs for each agent)
 - ✅ Modular and extensible design

---

### 📈 Design Highlights
 
 - Agents operate independently and collaborate via orchestrator
 - Decisions are based on real metric trends and sentiment analysis
 - Risks and actions are dynamically generated from system state
<<<<<<< HEAD
 - Clean separation of concerns ( agents, tools, orchestration)
=======
 - Clean separation of concerns ( agents, tools, orchestration)
>>>>>>> b0b379d9cc15b53e362cdece2f42e44aabc99cf0
