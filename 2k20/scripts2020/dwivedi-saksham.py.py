import cv2 as cv
import numpy as np
from numpy.lib.function_base import copy
#################Variable Declaration########################
image_width=480
image_height=640
max_area=500
krnl=np.ones((5,5),np.int8)
myColor=[[79,16,128,153,118,225],[8,8,8,179,118,78]]
colorList=[[255,0,0],[0,0,255]]
drawingPoints=[]
#############################################################
############################################################################################################# Stack Image Function Begins ###############################################
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
############################################################################################################# Stack Image Function Ends ###############################################
########### Function For Preprocessing Image ###################
def preProcessImg(img):
  imGray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
  imgBlur=cv.GaussianBlur(imGray,(7,7),0.5)
  imgCanny=cv.Canny(imgBlur,100,100)
  imgDilation=cv.dilate(imgCanny,krnl,iterations=2)
  imgErode=cv.erode(imgDilation,krnl,iterations=1)
  return imgErode
########### Function Ends ######################################
################## Colour Picker Function #################
def colourPicker(img):
    cv.namedWindow("Track")
    cv.resizeWindow("Track",350,500)
    def empty(a):
      pass
    cv.createTrackbar("Hue min","Track",0,179,empty)
    cv.createTrackbar("Hue max","Track",20,179,empty)
    cv.createTrackbar("Saturation min","Track",112,255,empty)
    cv.createTrackbar("Saturation max","Track",235,255,empty)
    cv.createTrackbar("Value min","Track",150,255,empty)
    cv.createTrackbar("Value max","Track",255,255,empty)
    h_min=cv.getTrackbarPos("Hue min","Track")
    h_max=cv.getTrackbarPos("Hue max","Track")
    satu_min=cv.getTrackbarPos("Saturation min","Track")
    satu_max=cv.getTrackbarPos("Saturation max","Track")
    val_min=cv.getTrackbarPos("Value min","Track")
    val_max=cv.getTrackbarPos("Value max","Track")
    lower=np.array([h_min,satu_min,val_min])
    upper=np.array([h_max,satu_max,val_max])
    imgHsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    mask=cv.inRange(imgHsv,lower,upper)
    imagRes=cv.bitwise_and(img,img,mask=mask)
    return [imagRes,mask]
################## Function Ends #############################
################## Color Detector ############################
def colorDetector(img,myColor,colorList):
    cnt= 0
    newPoints=[]
    imgHsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    for color in myColor:
        upp=np.array(color[3:6])
        lwr=np.array(color[0:3])
        msk=cv.inRange(imgHsv,lwr,upp)
        x,y=getContours(msk)
        cv.circle(imgFinal,(x,y),12,colorList[cnt],cv.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,cnt])
        cnt+=1
    return newPoints
################## Function Ends #############################
################## Function to get outer contour #############
def getContours(img):
    contour,hr=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cn in contour:
        area=cv.contourArea(cn)
        if area >500:
            peri = cv.arcLength(cn,True)
            approx = cv.approxPolyDP(cn,0.02*peri,True)
            x, y, w, h = cv.boundingRect(approx)
    return x+w//2,y        
################## Function Ends #############################
################## Draw on Image #############################
def drawOnImage(pts,colorList):
    for point in pts:
        cv.circle(imgFinal, (point[0], point[1]),10,colorList[point[2]], cv.FILLED)
################## Function Ends #############################
cap = cv.VideoCapture(0)
cap.set(3,360)
cap.set(4,480)
cap.set(10,150)
if (cap.isOpened()== False): 
  print("Error opening")
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    imgFinal=copy(frame)
    point=colorDetector(frame,myColor,colorList)
    if len(point)!=0:
        for newP in point:
            drawingPoints.append(newP)
    if len(drawingPoints)!=0:
        drawOnImage(drawingPoints,colorList)
    arrayimg=([frame,imgFinal])
    stackimg=stackImages(0.7,arrayimg)
    cv.imshow('Frame', stackimg)
    if cv.waitKey(1) & 0xFF == ord('q'):
      break
  else: 
    break
cap.release()
cv.destroyAllWindows()