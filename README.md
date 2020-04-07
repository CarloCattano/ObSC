# Control [OBS Studio](https://obsproject.com/) with Open Sound Control template example

### Uses [Python-osc](https://pypi.org/project/python-osc/)   
### [OBS web socket](https://github.com/Palakis/obs-websocket/releases/tag/4.7.0) and [obs-websocket-py](https://github.com/Elektordi/obs-websocket-py) 


#### Watch a creative simple example use :
[![Watch creative simple example use](https://img.youtube.com/vi/00V3wrOonBU/hqdefault.jpg)](https://youtu.be/00V3wrOonBU)

## Control Obs from any OSC capable app running on the same network :
### * the script connects python to obs websocket         on port 4444 in localhost using default credentials ( you might want to change that if you stream :-) 

 * you can get all the needed stuff with pip install -r requirements.txt
 * An osc listener runs on port 5005 and listens for /Scene message  
     
 * It lists all the available scenes to iterate through them 
     
 * A lot of parameters are exposed to the web socket so you can control almost anything in OBS with the right address. For           now I commented out a few lines that ilustrates a way to control individual elements as "webcam1" on "Scene1" on/off switch.
 
 * Current example switches between two scenes named Scene1 and Scene2 with values from a m4l device sending values from 0 to 127 
    
## Will try to develope it futher , and maybe make a GUI with tkinter or similar to learn about it 
    
    
    
# Stay at home , and spin your streams :-)
    
    
    
    
