from tkinter import *
import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)

def show(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('L_click')
        x0 = x - 35
        y0 = y - 35
        print(x0,y0)
        rectangle.append((x-35,y-35))
        

cv2.namedWindow("Obosrat sa")
cv2.setMouseCallback("Obosrat sa", show)       

rectangle = []

while True: 
    ret, frame = cap.read() 
    for (x0,y0) in rectangle:
        x1 = x0 + 70
        y1 = y0 + 70
        cv2.rectangle(frame,(x0,y0),(x1,y1),(0,255,0),3)


    cv2.imshow('Obosrat sa', frame)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

    if cv2.waitKey(30) & 0xFF == ord('c'):
        print('You have Windows or Linux? \n Input(W/L):')
        ans = input(str())
        if ans == 'W' or 'w' or 'Windows':
            os.system('CLS')
            
        elif ans == 'L' or 'l' or 'Linux':
            os.system('clear')

cap.release(), cv2.destroyAllWindows()