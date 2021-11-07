import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode
import requests

# takes the endpoint from our database in order to send our userIDs
USER_ENDPOINT = 'https://breadpass.vercel.app/api/user'

# a tremendous help in getting our code reader working was
# https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5 
# this provided the basic functionality and a lot of the needed variables to find the codes

# this function will decode barcodes from an image we will provide via webcam

# setting previousID to empty string, this will be used to check if code is same as previous code
# and if it is same code request will not be resent
def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
   
# this will then draw the barcode and set the decoded data to variable barcodeData
    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)
        barcodeData = obj.data.decode("utf-8")
    
        idList = []
        idList += [barcodeData]

        string = 'USERID: ' + barcodeData

        # for demo purposes we will also print the data decoded from our image directly above the code
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
    
        #this will save our barcodeData as an object which we need in order to send in correct format
        idDict = {'userId' : barcodeData}
            
        r = requests.post(USER_ENDPOINT, data = idDict)
        data = r.json()
        print(data)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break

