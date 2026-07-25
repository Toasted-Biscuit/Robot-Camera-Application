import cv2 as cv
import sys
import time

def displayBaguette():
    img = cv.imread(cv.samples.findFile("baguette robbery.jpg"))
    if img is None:
        sys.exit("Couldn't read the image, loser")

    cv.imshow("Display WONDOW", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("baguette robbery.png", img)


def displayWebcam(fps = 30):
    capture = cv.VideoCapture(0)
    if not capture.isOpened():
        sys.exit("Poor poor code couldn't open the webcam :(")

    isCapturing = True
    while isCapturing:
        check, frame = capture.read()
        if not check:
            print("Can't recieve the frame lol")
            break

        cv.imshow("Camera Feed", frame)

        if cv.waitKey(1) & 0xff == ord("q"):
            break

        time.sleep(1.0 / fps)

displayWebcam(30)