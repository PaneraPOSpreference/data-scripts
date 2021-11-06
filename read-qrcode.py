import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode


userdict ={
    0 : "Frank",
    1 : "John",
    2 : "Mary",
    3 : "Bob"
}

def QRdecoder(image):
    gray_img = cv2.cvtColor(image, 0)
    qrcode = decode(gray_img)

    for obj in qrcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")

        barcodeType = obj.type
        if barcodeData == '0':
            print("QR Code: " + barcodeData + " (" + barcodeType + ")")
            print("User: " + userdict[0])
            string = userdict[0]
        elif barcodeData == '1':
            print("QR Code: " + barcodeData + " (" + barcodeType + ")")
            print("User: " + userdict[1])
            string = userdict[1]
        elif barcodeData == '2':
            print("QR Code: " + barcodeData + " (" + barcodeType + ")")
            print("User: " + userdict[2])
            string = userdict[2]
        elif barcodeData == '3':
            print("QR Code: " + barcodeData + " (" + barcodeType + ")")
            print("User: " + userdict[3])
            string = userdict[3]
        else:
            print("QR Code: " + barcodeData + " (" + barcodeType + ")")
            print("User: Unknown")
            string = "User: Unknown"

        
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(20,0,0), 2)
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    QRdecoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break