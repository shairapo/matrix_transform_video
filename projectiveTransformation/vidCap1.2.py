import cv2
import numpy as np

counter = 0
posList = []
pause=False

# append points chosen on video
def on_click_original(event, x, y, p1, p2):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        counter += 1
        print('x = %d, y = %d' % (x, y))
        posList.append((x, y))
        if counter == 4:
            printcoor()

# Print chosen points
def printcoor():
    for row in posList:
        print(row, end=' ')
    print()

# Create transform matrix and show warped image
def transformOutput(frame):
    rows, cols = frame.shape[:2]

    pts1 = np.float32([[posList[0], posList[1], posList[2], posList[3]]])
    pts2 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Put in perspective
    result = cv2.warpPerspective(frame, matrix, (cols, rows))

    cv2.imshow('Result', result)

# start video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video stream or file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        cv2.setMouseCallback('Frame', on_click_original)

        # When all points are chosen, create the matrix and pause video on specific frame
        if counter == 4:
            transformOutput(frame)
            pause=True

        # Pause video until 'r' (resume) is pressed
        while pause:
            cv2.imshow('Frame', frame)
            key = cv2.waitKey(1)
                
            # If 'r' key is pressed again, resume playback and reset all variables to choose new points
            if key == ord('r'):
                pause=False
                counter=0
                posList = []
                break
        
        # When video is on, press 'q' (quite) to close all windows
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()



# # point transformation function call
# calMatchCoor(matrix,result)

# # transform the point
# def calMatchCoor(matrix,result):
#     px = (matrix[0][0]*p[0] + matrix[0][1]*p[1] + matrix[0][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
#     py = (matrix[1][0]*p[0] + matrix[1][1]*p[1] + matrix[1][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
#     p_after = (int(px), int(py))

#     # Draw the new point
#     cv2.circle(result,p_after, 30, (0,255,0), 20)

#     # Show the result
#     plt.imshow(result)
#     plt.title('Predicted position of your point in blue')
#     plt.show()

