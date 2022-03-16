#complete CAPITALIZED sections

#AUTHOR: Ocean Saviors
#DATE: 3/18/2022

#import libraries
import time
import os
import board
import busio
import adafruit_bno055
#from git import Repo
from picamera import PiCamera
from camera import main

#setup imu and camera
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

"""
#bonus: function for uploading image to Github
def git_push():
    try:
        repo = Repo('/home/pi/FlatSatChallenge') #PATH TO YOUR GITHUB REPO
        repo.git.add('folder path') #PATH TO YOUR IMAGES FOLDER WITHIN YOUR GITHUB REPO
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')
"""
#Alt by Avinda
"""
def git_push():
    try:
        os.system("git add -A")
        msg = input("add message: ")
        os.system(f"git commit -m {msg}")
        os.system("git push")
    except:
        print("Couldn't upload to git")
"""


#SET THRESHOLD
threshold = 1


#read acceleration
while True:
    accelX, accelY, accelZ = sensor.acceleration

    if accelX > threshold or accelY > threshold or accelZ > threshold:
        main()


    #PAUSE
