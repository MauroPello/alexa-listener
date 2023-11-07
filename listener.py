import os
from flask import Flask, request

app = Flask(__name__)

@app.get("/alexa-listener")
def alexa_listener():
    # checking if key is correct
    key = request.args.get("key")
    if key != "ciao35392ahgjai3":
        return "Hai sbagliato password!", 401

    match request.args.get("action"):
        case "shutdown":
            os.system("pkill -INT chrome")
            # disconnect stereo bluetooth
            os.system("bluetoothctl disconnect 82:49:69:CC:D1:00")
            # quit albert
            os.system("albert quit")
            # shutdown pc
            # os.system("qdbus org.kde.ksmserver /KSMServer logout 0 2 0")
            os.system("shutdown now")
            return "Ok!", 200
        case "volume-up":
            os.system("xdotool key XF86AudioRaiseVolume")
            return "Ok!", 200
        case "volume-down":
            os.system("xdotool key XF86AudioLowerVolume")
            return "Ok!", 200
        case "toggle":
            os.system("xdotool key XF86AudioPlay")
            return "Ok!", 200
        case "video-yt":
            query = request.args.get("query")
            if not query:
                return "Non hai fornito nessun video da cercare!", 401
            if "video dopo" in query.lower():
                os.system("xdotool key --window $(xdotool search --name \"YouTube\") shift+n")
                os.system("xdotool key XF86AudioNext")
                return "Ok!", 200
            if "video prima" in query.lower():
                os.system("xdotool key XF86AudioPrev")
                return "Ok!", 200

            # cerca e riproduci video
            os.system(f"google-chrome-stable \"https://www.youtube.com/results?search_query={query.replace(' ', '+')}&sp=EgIQAQ%253D%253D\" &")
            os.system(f"sleep 5 && xdotool search --name \"YouTube\" windowactivate mousemove 2500 400 click 1 && sleep 3 && xdotool key F")

            return "Ok!", 200
        case "video-ap":
            query = request.args.get("query")
            if not query:
                return "Non hai fornito nessun video da cercare!", 401

            # cerca e riproduci video
            link = f"https://www.primevideo.com/search/ref=atv_nb_sr?phrase={query}&ie=UTF8"

            os.system(f"google-chrome-stable \"{link}\" &")
            os.system(f"sleep 5 && xdotool search --name \"Prime Video\" windowactivate mousemove 2100 500 && sleep 1 && xdotool search --name \"Prime Video\" windowactivate mousemove 2100 650 click 1 && sleep 3 && xdotool search --name \"Prime Video\" windowactivate mousemove 4625 295 click 1")

            return "Ok!", 200
        case "video-nf":
            query = request.args.get("query")
            if not query:
                return "Non hai fornito nessun video da cercare!", 401

            # cerca e riproduci video
            link = "https://www.netflix.com/search?q=" + query

            os.system(f"google-chrome-stable \"{link}\" &")
            os.system(f"sleep 5 && xdotool search --name \"Netflix\" windowactivate mousemove 1500 600 && sleep 1 && xdotool search --name \"Netflix\" windowactivate mousemove 1380 880 click 1 && sleep 3 && xdotool search --name \"Netflix\" windowactivate click --repeat 2 1")

            return "Ok!", 200
        case _:
            return "Non ho capito il comando!", 400
