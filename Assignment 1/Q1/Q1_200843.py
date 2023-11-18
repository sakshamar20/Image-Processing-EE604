import cv2
import numpy as np

# Usage
def solution(image_path):
    # image= cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
    image = cv2.imread(image_path)
    # print(image.shape)
    ######################################################################
    ######################################################################
    #####  WRITE YOUR CODE BELOW THIS LINE ###############################

    if image.shape[-1] == 4:
        # print(1)
        image[image[:, :, 3] < 240] = [0,0,0,255]  

    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    # cv2.imshow("Image", gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thr = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for pnt in contours:
        points = cv2.approxPolyDP(pnt, 0.04 * cv2.arcLength(pnt, True), True)

    p = []

    for point in points:
        p.append(point[0])
    
    # print(p)
    p = sorted(p, key=lambda x: x[0])
    temp = p[1]
    if(p[0][1] > p[1][1]):
        p[1] = p[0]
        p[0] = temp
    temp = p[2]
    if(p[2][1] < p[3][1]):
        p[2] = p[3]
        p[3] = temp
    
    pts1 = np.float32(p)
    
    pts2 = np.float32([[0,0],[0,599],[599,599],[599,0]])
    # print(pts1,pts2)
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(image,M,(600,600))

    image = dst
    # cv2.imwrite("done.jpg", dst)
    

    ######################################################################

    return image
