import cv2
import numpy as np

# Usage
def solution(image_path):
    image= cv2.imread(image_path)
    ######################################################################
    ######################################################################
    '''
    The pixel values of output should be 0 and 255 and not 0 and 1
    '''
    #####  WRITE YOUR CODE BELOW THIS LINE ###############################
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blurred_hsv = cv2.GaussianBlur(hsv_image, (5,5), 6) 

    lowerLimit = np.array([2,120,110])
    
    upperLimit= np.array([255, 255, 255])
    # lower_lava = np.array([100,2,2])
    # upper_lava = np.array([255, 120, 120])



    lava_mask = cv2.inRange(blurred_hsv, lowerLimit ,upperLimit)
    # show(lava_mask)

    _, labels, stats, _ = cv2.connectedComponentsWithStats(lava_mask, connectivity=8)

    largest_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1

    largest_component_mask = np.uint8(labels == largest_label) * 255
    # show(largest_component_mask)
    # show(image)
    result = cv2.bitwise_and(image, image, mask=largest_component_mask)

 

    # show(result)

    contours, _ = cv2.findContours(largest_component_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # contours = sorted(contours, key=cv2.contourArea, reverse=True)


    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # for contour in contours:
    #     epsilon = 0.01 * cv2.arcLength(contour, True)
    #     approx = cv2.approxPolyDP(contour, epsilon, True)


    #     cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    #     cv2.drawContours(image, [approx], -1, (255, 0, 0), 2)
    result_image = np.zeros_like(image)

    # cv2.drawContours(result_image, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    for contour in contours:
    # Adjust the epsilon value to change the resolution of polygons
        epsilon = 0.003 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Draw the smoothed contour on the result image
        cv2.polylines(result_image, [approx], isClosed=True, color=(255, 255, 255), thickness=2)
        cv2.fillPoly(result_image, [approx], color=(255, 255, 255))


    # show(result_image)








    ######################################################################  
    return result_image

