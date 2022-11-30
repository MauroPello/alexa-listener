import os
from flask import Flask, request

app = Flask(__name__)

@app.get("/alexa-listener")
def alexa_listener():
    # checking if key is correct
    key = request.args.get("key")
    if key != "ciao35392ahgjai3":
        return "Error, wrong key!", 401
    
    match request.args.get("action"):
        case "shutdown":
            # disconnect stereo bluetooth 
            os.system("bluetoothctl disconnect 82:49:69:CC:D1:00")
            # shutdown pc
            os.system("qdbus org.kde.ksmserver /KSMServer logout 0 2 0")
            return "Success!", 200
        case "volume-up":
            os.system("pulseaudio-ctl up 10")
            return "Success!", 200
        case "volume-down":
            os.system("pulseaudio-ctl down 10")
            return "Success!", 200
        case "toggle":
            os.system("playerctl play-pause")
            return "Success!", 200
        case _:
            return "Error, action not supported!", 400