from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from intent_engine import detect_intent
from booking_service import book_spa
from ticket_service import create_ticket
from mqtt_service import control_lights  # ✅ Correct placement

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static/index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

@app.post("/voice")
async def handle_voice(request: Request):
    data = await request.json()
    voice_text = data.get("voice_text")

    intent_data = detect_intent(voice_text)

    if intent_data["intent"] == "book_spa":
        booking = book_spa(intent_data["time"])
        ticket = create_ticket(room="101", task=f"Spa booking for guest at {intent_data['time']}")
        return {
            "status": "success",
            "intent": intent_data,
            "booking": booking,
            "ticket": ticket
        }

    elif intent_data["intent"] == "request_towel":
        ticket = create_ticket(room="101", task="Towel request from guest")
        return {
            "status": "success",
            "intent": intent_data,
            "ticket": ticket
        }

    elif intent_data["intent"] == "lights_off":
        result = control_lights("off")
        return {
            "status": "success",
            "intent": intent_data,
            "mqtt": result
        }

    return {"status": "unrecognized", "message": "Could not detect valid intent."}
