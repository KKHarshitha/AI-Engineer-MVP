def detect_intent(voice_text):
    voice_text = voice_text.lower()
    if "book" in voice_text and "spa" in voice_text:
        return {"intent": "book_spa", "time": "17:00"}
    elif "towel" in voice_text:
        return {"intent": "request_towel"}
    elif "turn off the lights" in voice_text or "lights off" in voice_text:
        return {"intent": "lights_off"}
    else:
        return {"intent": "unknown"}
