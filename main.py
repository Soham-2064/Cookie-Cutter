import cv2
import random
import time
import os
import numpy as np
from cvzone import HandTrackingModule, overlayPNG

# Read images from a folder
folderpath = 'frames'
mylist = os.listdir(folderpath)
graphic = [cv2.imread(f'{folderpath}/{inpath}') for inpath in mylist]
kill = graphic[0];  # Read frames\img 2 in the kill variable
winner = graphic[1];  # Read frames\img 3 in the winner variable
intro = graphic[2];  # Read frames\img 1 in the intro variable


cv2.imshow('Cookie Cutter', cv2.resize(intro, (0,0), fx=0.67, fy=0.67))
cv2.waitKey(1)


while True:
    cv2.imshow('Cookie Cutter', cv2.resize(intro, (0,0), fx=0.67, fy=0.67))
    if cv2.waitKey(1) & 0xFF==ord('q'):     
        break

# Read the camera
cam = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77)
# Sets the minimum confidence threshold for the detection

# Initializing game components
folderpath2 = 'img'
mylist2 = os.listdir(folderpath2)
graphic2 = [cv2.imread(f'{folderpath2}/{inpath2}') for inpath2 in mylist2]
sqr_img = graphic2[0];  # Read img\sqr (1) in the sqr_img variable
mlsa = graphic2[1];  # Read img\mlsa in the mlsa variable


# INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.67, fy=0.67))
cv2.waitKey(1)
while True:
    cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.67, fy=0.67))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

TIMER_MAX = 10       #so that user gets only 45 sec to complete the game
TIMER=TIMER_MAX
maxMove=10    #how frequently the red and green will change- if we give 5 then how many times the light will change
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
cap=cv2.VideoCapture(0)     #it captures the video from webcam, if u have exter webcam it will become 1
frameHeight=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  #assigned the webcam and the height
frameWidth=cap.get(cv2.CAP_PROP_FRAME_WIDTH)


prev=time.time()    #previous time means prev frame is updated
prevDoll=prev
showFrame=cv2.resize('Cookie Cutter',(0,0),fx=0.67,fy=0.67)



# GAME LOGIC UPTO THE TEAMS
# ----------------------------------------------------------------
gameOver = False
win=True
while not gameOver:
    continue

if not win:
    # LOSS SCREEN
    for i in range(10):
        cv2.imshow('Cookie Cutter', cv2.resize(kill, (0, 0), fx=0.67, fy=0.67))
    while True:
        cv2.imshow('Cookie Cutter', cv2.resize(kill, (0, 0), fx=0.67, fy=0.67))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    # Show the loss screen from the kill image read before and end it after we press q
else:
    # WIN SCREEN
    cv2.imshow('Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.67, fy=0.67))
    cv2.waitKey(125)
    # Show the win screen from the winner image read before
    while True:
        cv2.imshow('Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.67, fy=0.67))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        # End it after we press q

# Destroy all the window
cv2.destroyAllWindows()
