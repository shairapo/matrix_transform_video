import cv2
import numpy as np

counter = 0
posList = []
pause=False

def on_click_original(event, x, y, p1, p2):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        counter += 1
        print('x = %d, y = %d' % (x, y))
        posList.append((x, y))
        if counter == 4:
            printcoor()

def printcoor():
    for row in posList:
        print(row, end=' ')
    print()

def transformOutput(frame):
    rows, cols = frame.shape[:2]

    pts1 = np.float32([[posList[0], posList[1], posList[2], posList[3]]])
    pts2 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Put in perspective
    result = cv2.warpPerspective(frame, matrix, (cols, rows))

    cv2.imshow('Result', result)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video stream or file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        cv2.setMouseCallback('Frame', on_click_original)

        if counter == 4:
            transformOutput(frame)
            pause=True

        while pause:
            cv2.imshow('Frame', frame)
            key = cv2.waitKey(1)
                
            # If 'r' key is pressed again, resume playback
            if key == ord('r'):
                pause=False
                counter=0
                posList = []
                break

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
