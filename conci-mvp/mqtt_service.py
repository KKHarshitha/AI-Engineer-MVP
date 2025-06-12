import paho.mqtt.publish as publish

def control_lights(state):
    topic = "room/101/lights"
    message = "off" if state == "off" else "on"
    try:
        publish.single(topic, payload=message, hostname="localhost")
        return {"status": "sent", "topic": topic, "message": message}
    except Exception as e:
        return {"status": "error", "error": str(e)}
