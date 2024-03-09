import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
def qr_recognition():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)

    DataList = ["START","END"]
    Flag = False
    Show = False
    
    while True:
	    success , img = cap.read()    
	    for barcode in decode(img):
	        mydata = barcode.data.decode('utf-8')
			#print(mydata)
	        if mydata in DataList: #True if the data in barcode is START or END
	            myoutput = f"Authorized {mydata}"
	            mycolor = (0,255,0)
	            Flag = True
	            Show = True
	        else:
	            myoutput = f"Un-Authorized {mydata}"
	            mycolor = (0,0,255)
	            Show = True
	        pts = np.array([barcode.polygon],np.int32)
	        pts = pts.reshape((-1,1,2))
	        cv2.polylines(img,[pts],True,mycolor,5)
	        pts2 = barcode.rect
	        cv2.putText(img,myoutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,mycolor,2)#message(info o qr code) onn the window
	       
	    cv2.imshow('Result',img)
	    if cv2.waitKey(1) & Show:
	        time.sleep(2)
	        break
	  
    cap.release()
    cv2.destroyAllWindows()
    return Flag
