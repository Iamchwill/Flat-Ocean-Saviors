#sensor_calc.py
import time
import numpy as np
import adafruit_fxos8700
import adafruit_fxas21002c
import time
import os
import board
import busio
from statistics import mean

i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_fxos8700.FXOS8700(i2c)
sensor2 = adafruit_fxas21002c.FXAS21002C(i2c)

#Activity 1: RPY based on accelerometer and magnetometer
def roll_am(accelX,accelY,accelZ):
    roll = np.arctan2(accelY/((accelX * accelX) + (accelZ * accelZ))**0.5)
    return roll

def pitch_am(accelX,accelY,accelZ):
    pitch = np.arctan2(accelX/((accelY * accelY) + (accelZ * accelZ))**0.5)
    return pitch

def yaw_am(accelX,accelY,accelZ,magX,magY,magZ):
    #TODO
    mag_x = (magX * np.cos(pitch_am)) + ((magY * np.sin(roll_am) * np.sin(pitch_am)) + (magZ * np.cos(roll_am) * np.sin(pitch_am)))
    return (180/np.pi)*np.arctan2(-mag_y, mag_x)

#Activity 2: RPY based on gyroscope
def roll_gy(prev_angle, delT, gyro):
    roll = prev_angle + (delT * gyro)
    return roll
def pitch_gy(prev_angle, delT, gyro):
    pitch = prev_angle + (delT * gyro)
    return pitch
def yaw_gy(prev_angle, delT, gyro):
    yaw = prev_angle + (delT * gyro)
    return yaw

def set_initial(offset = [0,0,0]):
    #Sets the initial position for plotting and gyro calculations.
    print("Preparing to set initial angle. Please hold the IMU still.")
    time.sleep(3)
    print("Setting angle...")
    accelX, accelY, accelZ = sensor1.accelerometer #m/s^2
    magX, magY, magZ = sensor1.magnetometer #gauss
    #Calibrate magnetometer readings. Defaults to zero until you
    #write the code
    magX = magX + offset[0]
    magY = magY + offset[1]
    magZ = magZ + offset[2]
    roll = roll_am(accelX, accelY,accelZ)
    pitch = pitch_am(accelX,accelY,accelZ)
    yaw = yaw_am(accelX,accelY,accelZ,magX,magY,magZ)
    print("Initial angle set.")
    return [roll,pitch,yaw]

def calibrate_mag():
    set_mag_X = []
    set_mag_Y = []
    set_mag_Z = []
    set_accel_X = []
    set_accel_Y = []
    set_accel_Z = []
    interval = 10
    #TODO: Set up lists, time, etc
    print("Preparing to calibrate magnetometer. Please wave around.")
    time.sleep(2)
    for i in range(interval):
        mag_new_X, mag_new_Y, mag_new_Z = sensor1.magnetometer
        accel_new_X, accel_new_Y, accel_new_Z = sensor1.accelerometer
        set_mag_X.add(mag_new_X)
        set_mag_Y.add(mag_new_Y)
        set_mag_Z.add(mag_new_Z)
        set_accel_X.add(accel_new_X)
        set_accel_Y.add(accel_new_Y)
        set_accel_Z.add(accel_new_Z)
        time.sleep(1)
    print("Calibrating...")
    #TODO: Calculate calibration constants
    magX = mean(set_mag_X)
    magY = mean(set_mag_Y)
    magZ = mean(set_mag_Z)
    accelX = mean(set_accel_X)
    accelY = mean(set_accel_Y)
    accelZ = mean(set_accel_Z)
    roll = roll_am(accelX, accelY,accelZ)
    pitch = pitch_am(accelX,accelY,accelZ)
    yaw = yaw_am(accelX,accelY,accelZ,magX,magY,magZ)    
    print("Calibration complete.")
    return [roll,pitch,yaw]

def calibrate_gyro():
    set_theta_previous = []
    set_delT = []
    set_Wgyro = []
    #print("Preparing to calibrate gyroscope. Put down the board and do not touch it.")
    #time.sleep(3)
    #print("Calibrating...")
    #TODO
    #print("Calibration complete.")
    return [0, 0, 0]
