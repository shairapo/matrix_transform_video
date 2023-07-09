import numpy as np
import cv2
import matplotlib.pyplot as plt

# to see the next plot in line for each stage, close the current image plot

counter=0
posList=[]
global p

# load the image and get the dimensions
image = cv2.imread('../images/lroom1.jpg')
rows, cols = image.shape[:2]

# Draw a point for reference. cv2.WINDOW_NORMAL makes sure the size of the window is adjustable. original coordinates in image are kept.
p = (2000,1000)
cv2.namedWindow("Input", cv2.WINDOW_NORMAL)
cv2.circle(image,p, 20, (0,0,255), -1)
cv2.imshow('Input', image)

# create perspective matrix, show the new image, call a function to calculate the new point's coordinates according to the matrix.
def transformOutput():
    
    pts1=np.float32([[posList[0],posList[1],posList[2],posList[3]]]) 
    pts2=np.float32([[0,0], [cols-1,0], [0,rows-1], [cols-1,rows-1]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)

    # Put in perspective
    result=cv2.warpPerspective(image,matrix,(cols,rows))

    plt.imshow(result)
    plt.title('Distorced')
    plt.show()

    calMatchCoor(matrix,result)

# transform the point
def calMatchCoor(matrix,result):
    px = (matrix[0][0]*p[0] + matrix[0][1]*p[1] + matrix[0][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
    py = (matrix[1][0]*p[0] + matrix[1][1]*p[1] + matrix[1][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
    p_after = (int(px), int(py))

    # Draw the new point
    cv2.circle(result,p_after, 30, (0,255,0), 20)

    # Show the result
    plt.imshow(result)
    plt.title('Predicted position of your point in blue')
    plt.show()


# clicking order: 
# TOP left
# TOP right 
# BOTTOM left 
# BOTTOM right

def on_click_originial(event, x, y, p1, p2):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        counter=counter+1
        print('x = %d, y = %d'%(x, y))
        posList.append((x, y))
        if(counter==4):
            printcoor()
            transformOutput()

def printcoor():
    for row in posList:
            print(row)    

cv2.setMouseCallback('Input', on_click_originial, counter)
cv2.waitKey()


