#Avinda
#Raspbian Linux: pip3 install picamera 
#Alternative: python -c "import picamera"
#Alternative 2: sudo apt-get update && sudo apt-get install python-picamera python3-picamera

#run this file in bash: python3 camera.py

from picamera import PiCamera
from time import sleep

def main():
    newCamera = PiCamera()
    newCamera.start_preview() #opens camera window
    
    sleep(5) #need about 3 seconds after opening preview to adjust lenses

    newCamera.capture('/home/pi/Desktop/newImage.jpg') #saves image into a file

    newCamera.stop_preview() #stops camera, REQUIRED

main()