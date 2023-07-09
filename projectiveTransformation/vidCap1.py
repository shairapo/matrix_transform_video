import cv2
import numpy as np
# import matplotlib.pyplot as plt
counter=0
posList=[]

def on_click_original(event, x, y, p1, p2):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        counter=counter+1
        print('x = %d, y = %d'%(x, y))
        posList.append((x, y))
        if(counter==4):
            printcoor()
            

def printcoor():
    for row in posList:
        print(row) 


def transformOutput(frame):
    rows, cols = frame.shape[:2]

    pts1=np.float32([[posList[0],posList[1],posList[2],posList[3]]]) 
    pts2=np.float32([[0,0], [cols-1,0], [0,rows-1], [cols-1,rows-1]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)

    # Put in perspective
    result=cv2.warpPerspective(frame,matrix,(cols,rows))
    
    cv2.imshow('Result',result)
    # plt.imshow(result)
    # plt.title('Distorced')
    # plt.show()

cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    
    cv2.setMouseCallback('Frame', on_click_original)

    if(counter==4):
       transformOutput(frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
      
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
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

