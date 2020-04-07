import sys,time,argparse,math
from pythonosc import dispatcher
from pythonosc import osc_server

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, requests  # noqa: E402

host = "localhost"
port = 4444
password = "secret"

ws = obsws(host, port, password)
ws.connect()

ScenesNames = []
SceneSources = []

def sourceSwitch(source_name,scene,switch):
    ws.call(requests.SetSceneItemProperties(source_name,scene,visible=switch)) 

def scene_switch(unused_addr, args, filter):  
       
    if filter > 60 : # change to scene 2 
        ws.call(requests.SetCurrentScene(ScenesNames[1]))          
                                                                    #sourceSwitch("screen1","Scene1",True)   
                                                                    #sourceSwitch("screen2","Scene1",False)
    elif filter <= 59 :
        ws.call(requests.SetCurrentScene(ScenesNames[0]))           # COntrol sources by using sourceSwitch("source_Name","Scene_name", bool)
                                                                    #sourceSwitch("screen1","Scene1",False)
    print("\n [{0}] +" " + {1}".format(args[0], filter))    


if __name__ == "__main__":
    try:
        scenes = ws.call(requests.GetSceneList())

        for s in scenes.getScenes():
            name = s['name']
            print(ws.call(requests.GetSourcesList()),"\n")       # Get The list of available sources in each scene in OBS
            ScenesNames.append(name)                        # Add every scene to a list of scenes

        print("\n CURRENT SCENES IN OBS" ,ScenesNames)
       
        ### OSC SETTINGS
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip",default="127.0.0.1", help="The ip to listen on")
        parser.add_argument("--port",type=int, default=5005, help="The port to listen on")

        args = parser.parse_args()                           # parser for --ip --port arguments
        dispatcher = dispatcher.Dispatcher()

        dispatcher.map("/Scene", scene_switch, "Scene")      # OSC LISTENER
        server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)  
        print("Serving on {}".format(server.server_address))
        
        server.serve_forever()

    except KeyboardInterrupt:
        pass

    ws.disconnect()

  