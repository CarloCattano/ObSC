# Control [OBS Studio](https://obsproject.com/) with Open Sound Control template example

## Uses [Python-osc](https://pypi.org/project/python-osc/) python3+ and [OBS web socket](https://github.com/Palakis/obs-websocket/releases/tag/4.7.0)

[![Watch creative simple example use](https://img.youtube.com/vi/00V3wrOonBU/hqdefault.jpg)](https://youtu.be/00V3wrOonBU)

## Control Obs from any OSC capable app running on the same network :

###     In this first example the script connect python to obs websocket on port 4444 in localhost using default credentials ( you might want to change that if you stream :-) 
     
#### An osc listener runs on port 5005 .
#### It lists all the available scenes to iterate through them 
#### -         A lot of parameters are exposed to the web socket so you can control almost anything in OBS with the right address. For now I commented out a few lines to control individual elements as "webcam1" on "Scene1" on/off switch , and a scenes iterator for demostration purposes
    
### Will try to develope it futher , and maybe maka an GUI with tkinter or similar to learn about it 
    
## Stay at home , and spin your streams :-)
    
    
    
    
