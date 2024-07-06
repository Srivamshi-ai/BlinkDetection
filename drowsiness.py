import os
import cv2
import numpy as np
import dlib
from math import hypot

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)

# Initialize dlib's face detector (HOG-based) and create a facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# This below mehtod will draw all those points which are from 0 to 67 on face one by one.



# Function to calculate the midpoint between two points
def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


# Initialize font for displaying text on the screen
font = cv2.FONT_HERSHEY_PLAIN


# Initialize counters and status
sleep= 0
active = 0
drowsy=0
status=""



# Function to calculate the blinking ratio of the eyes by Calculating the ratio of horizontal to vertical length
def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[4]), facial_landmarks.part(eye_points[5]))

    #uncomment below lines if you want to see the horizontal lines or vertical lines  
    # hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    # ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

    h_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    v_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = h_length/v_length
    return ratio

# Main loop to process video frames
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #landmarks=predictor(gray,face)
    
    faces = detector(gray)
    for face in faces:
        x1=face.left()
        y1=face.top()
        x2=face.right()
        y2=face.bottom()
        landmarks=predictor(gray,face)
        for n in range(0,68):
         x=landmarks.part(n).x
         y=landmarks.part(n).y
         cv2.circle(frame,(x,y),4,(255,0,0),-1)
       # print(landmarks)
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)

        # Calculate the blinking ratio for both eyes
        left_blink = get_blinking_ratio([36, 37, 38, 39,40,41], landmarks)
        right_blink = get_blinking_ratio([42, 43, 44, 45,46,47], landmarks)
        blinking_ratio = (left_blink + right_blink) / 2
        if blinking_ratio > 5.7:
            drowsy+=1
            if drowsy<=6:
              cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0))
            elif drowsy>6:
              cv2.putText(frame,"SLEEPING ",(50,150),font,7,(255,0,0))  
              
          # Determine the status based on the blinking ratio
        elif blinking_ratio <5.7:
            active+=1
            if active>3:
              cv2.putText(frame,"ACTIVE",(50,150),font,7,(250,0,0)) 
        
                                  
        elif blinking_ratio>6:
            if sleep>2:
              cv2.putText(frame,"BLINKING",(50,150),font,7,(250,0,0))      
             

    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
     # Break the loop if 'Esc' key is pressed
    if key == 27:
        break 


# Release the webcam and close all OpenCV windows
cap .release()
cv2.destroyAllWindows()
