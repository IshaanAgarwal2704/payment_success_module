# Payment Success Module

This project implements the **PaymentSuccess Producer** in a distributed system using FastAPI.

## 🚀 Features
- Idempotency handling
- PaymentSuccess event generation
- Queue simulation using Python
- REST API using FastAPI
- Swagger UI for API testing

---

## 🛠️ Tech Stack
- Python
- FastAPI
- Pydantic
- Uvicorn
- Git & GitHub

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/IshaanAgarwal2704/payment_success_module.git
cd payment_success_module

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the FastAPI Server
uvicorn main:app --reload

4️⃣ Open Swagger UI

Open this in your browser:

http://127.0.0.1:8000/docs

🧪 API Testing
POST /payment-success

Sample Request:

{
  "order_id": "101",
  "amount": 240
}

Expected Response:

{
  "status": "success",
  "message": "Event created"
}
🔁 Duplicate Request Handling

Sending the same request again returns:

{
  "status": "duplicate",
  "message": "Already processed"
}
📦 GET /events

Used to view all generated events stored in the simulated queue.

📌 Concepts Implemented
Event-Driven Architecture
Idempotency
Queue-Based Communication
Distributed System Simulation

cd payment_success_module

