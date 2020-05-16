import cv2, time

#Create an object. Zero for external camera
video = cv2.VideoCapture(0)
a = 0

while True:
    a += 1
    #Create frame object
    check, frame = video.read()
    # print(check)
    #print(frame)#Repersent image

    #Convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Show the frame
    cv2.imshow("Capturing", gray)

    # For press any key to out(miliseconds)
    # cv2.waitKey(0)

    #For playing
    key = cv2.waitKey(1)

    if key == ord("q") and ord("Q"):
        break

print(a)
#Shutdown the camera
video.release()

cv2.destroyAllWindows