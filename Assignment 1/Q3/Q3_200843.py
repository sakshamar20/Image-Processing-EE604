import cv2
import numpy as np
import skimage as sk

def solution(image_path):
    ############################
    ############################
    image= cv2.imread(image_path)
    gray = 255 - cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    max_ang = 0
    max_ar = 0
    for angle in range(0,180):
        rot = sk.img_as_ubyte(sk.transform.rotate(thresh,angle, resize = True))
        arr = np.asarray(rot)
        dims = np.shape(arr)
        ar = np.zeros(dims[0])

        for i in range(0,dims[0]-1):
            ar[i] = np.sum(arr[i][:])

        if(max_ar <= np.max(ar)):
            max_ar = np.max(ar)
            max_angle = angle
    rot = sk.img_as_ubyte(sk.transform.rotate(thresh,max_angle, resize = True))
    arr = np.asarray(rot)
    dims = np.shape(arr)
    ar = np.zeros(dims[0])
    max = 0
    maxi = 0
    for i in range(0,dims[0]-1):
        ar[i] = np.sum(arr[i][:])
        if(ar[i] > max):
            max = ar[i]
            maxi = i

    flip = 0
    if(np.sum(ar[maxi-4:maxi-1])>np.sum(ar[maxi+1:maxi+4])):
        flip = 1
        
    if(flip == 1):
        max_angle -=180
    img = sk.img_as_ubyte(sk.transform.rotate(gray,max_angle, resize = True))
    
    ############################
    ############################
    ## comment the line below before submitting else your code wont be executed##
    # pass
    # image = cv2.imread(image_path)
    return (255 - cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
