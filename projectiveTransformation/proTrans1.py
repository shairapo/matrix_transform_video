import cv2
import numpy as np

counter=0
posList=[]
img = cv2.imread('../Images/lroom1.jpg')


print("original " , img.shape)

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#putting a colored circle in the picture for monitoring

p = (3172,1928)
cv2.circle(img,p, 20, (0,0,255), -1)

# print("resized " , resized.shape)

rows, cols = img.shape[:2]
cv2.namedWindow("Input", cv2.WINDOW_NORMAL) 
cv2.imshow('Input', img)

# once the user finishes clicking on the original src pic coordinates, this function will transform the image and create the new one
def transformOutput():
    src_points = np.float32([posList[0],posList[1],posList[2],posList[3]])
    dst_points = np.float32([[0,0], [cols-1,0], [0,rows-1], [cols-1,rows-1]]) 
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    img_output = cv2.warpPerspective(img, matrix, (cols,rows))

    p = (3172,1928)
    #!!!!!!!!the formula is wrong, this needs to be checked. then we can draw a green circel where it is to see
    px = (matrix[0][0]*p[0] + matrix[0][1]*p[1] + matrix[0][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
    py = (matrix[1][0]*p[0] + matrix[1][1]*p[1] + matrix[1][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
    p_after = (int(px), int(py))
    print('transformed circle is in x = %d, y = %d'%(px, py))
    
    cv2.namedWindow("Output", cv2.WINDOW_NORMAL) 
    cv2.imshow('Output', img_output)
    


# clicking order: top left-top right-bottom left-bottom right

def on_click_originial(event, x, y, p1, p2):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        counter=counter+1
        print('x = %d, y = %d'%(x, y))
        posList.append((x, y))
        if(counter==4):
            printcoor()
            transformOutput()
            cv2.setMouseCallback('Output', on_click_transformed)

def on_click_transformed(event, x, y, p1, p2):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x = %d, y = %d'%(x, y))


def printcoor():
    for row in posList:
            print(row)    

cv2.setMouseCallback('Input', on_click_originial, counter)
cv2.waitKey()


