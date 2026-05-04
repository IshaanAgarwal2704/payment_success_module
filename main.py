from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
processed_orders = set()   
event_queue = []          

class PaymentRequest(BaseModel):
    order_id: str
    amount: float

@app.post("/payment-success")
def payment_success(request: PaymentRequest):
    if request.order_id in processed_orders:
        return {
            "status": "duplicate",
            "message": "Already processed",
            "order_id": request.order_id
        }
    processed_orders.add(request.order_id)
    
    event = {
        "event": "PaymentSuccess",
        "order_id": request.order_id,
        "amount": request.amount,
        "timestamp": str(datetime.now())
    }
    event_queue.append(event)
    
    return {
        "status": "success",
        "message": "Event created",
        "event": event
    }

@app.get("/events")
def get_events():
    return event_queue