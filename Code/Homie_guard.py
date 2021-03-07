import cv2
import numpy as np
from mDev import *
import RPi.GPIO as GPIO
import time
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)  # Read output from PIR motion sensor
GPIO.setup(21, GPIO.OUT)  # LED output pin

#Creating an object
mdev = mDEV()

def send_email(sender, recipant, subject, password):
    return 0

def face_search(classifier='./haarcascade_frontalface_default.xml'):
    face_detect = cv2.CascadeClassifier(classifier) # Give the classifer to identify the object
    cap = cv2.VideoCapture(0) # Capture the video

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # width
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # height
    fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0') # fourcc
    size = (int(width),int(height)) # Size
    print("width: ", width, "height: ", height) # Print

    # Angle
    pitch_angle = 90
    roll_angle = 90
    P_roll = 0.015
    P_pitch = 0.01

    j = 0  # number for pictures
    k = 0  # number for videos
    video_flag = False

    timer = 0 # timer
    count_out = 0  # leave the camera
    count_in = 0  # stay in camera

    center_position = [width / 2, height / 2]
    target_position = center_position

    # face_detect = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    while True:
        i = GPIO.input(17)
        if i == 0:  # When output from motion sensor is LOW
            print("No intruders", i)
            GPIO.output(21, 0)  # Turn OFF LED
            time.sleep(0.1)
        elif i == 1:  # When output from motion sensor is HIGH
            print("Intruder detected", i)
            GPIO.output(21, 1)  # Turn ON LED
            time.sleep(0.1)

        flag, frame = cap.read()
        if flag == False:
            break
        gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
        face_zone = face_detect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        try:
            video.write(frame)
        except NameError:
            pass
        detect = 0
        target_position = center_position
        for x, y, w, h in face_zone:
            cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255], thickness=2)
            cv2.circle(frame, center=(x + w // 2, y + h // 2), radius=w // 2, color=[0, 255, 0], thickness=2)
            target_position = [x + w // 2, y + h // 2]
            cv2.putText(frame, "Scanning", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            count_out = 0
            detect = 1

            print("Center: ", target_position[0], target_position[1])

        cv2.imshow('video', frame) # show
        if detect == 0:
            count_out += 1
        elif detect == 1:
            count_in += 1
        print(count_out)
        if count_out >= 50:
            roll_angle = 90
            pitch_angle = 90
            count = 0
        if count_in == 15 and video_flag == False:
            cv2.imwrite("image" + str(j) + '.jpg', frame)  # take a picture

            video = cv2.VideoWriter("Video" + str(k) + ".avi", fourcc, 20, size)
            video_flag = True
            j += 1
            k += 1
            count_in = 0
        if count_out == 10 and video_flag == True:
            video.release()
            video_flag = False

        error_vector = [target_position[0] - center_position[0]
            , target_position[1] - center_position[1]]

        # if error_vector[0] < 0:

        roll_angle -= P_roll * error_vector[0]
        pitch_angle -= P_pitch * error_vector[1]
        if pitch_angle < 0:
            pitch_angle = 0
        if pitch_angle > 180:
            pitch_angle = 180
        if roll_angle < 0:
            roll_angle = 0
        if roll_angle > 180:
            roll_angle = 180

        mdev.setServo("2", int(roll_angle))
        mdev.setServo("3", int(pitch_angle))
        print("roll_angle: ", roll_angle)
        print("pitch angle:", pitch_angle)
        if cv2.waitKey(1) == ord('q'):
            break

def initialization():
    for i in range(4):
        mdev.setServo(str(i + 1), 135)
    time.sleep(1)
    for i in range(4):
        mdev.setServo(str(i + 1), 90)
    mdev.move(0, 0)

if __name__ == '__main__':
    initialization()
    training_set = input("Please enter the training set: ")
    face_search(training_set)
    # face_search('./haarcascade_frontalface_default.xml')
