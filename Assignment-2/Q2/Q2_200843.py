import cv2
import numpy as np
import math

def cbf(img, flash, d, s_C, s_S):
    rows= img.shape[0]
    cols = img.shape[1]
    ch = img.shape[2]
    res = np.zeros_like(img, dtype=np.float32)

    for i in range(rows):
        for j in range(cols):

            i_min, i_max = np.clip([i -d, i+ d +1], 0, rows)
            j_min, j_max = np.clip([j- d, j + d + 1], 0, cols)
            
            j_v, i_v = np.meshgrid(np.arange(j_min, j_max), np.arange(i_min, i_max))
            i_v = i - i_v
            j_v = j - j_v

            n_f = flash[i_min:i_max, j_min:j_max].astype(np.float32)
            n = img[i_min:i_max, j_min:j_max].astype(np.float32)

            p = np.float32(flash[i, j])
            int_d = np.clip(n_f - p, -255, 255)
            int_w = np.exp(-np.sum(int_d ** 2, axis=2) / (2 * s_C ** 2))

            s_w = np.exp(-((i_v) ** 2 + (j_v) ** 2) / (2 * s_S ** 2))
             # w = s_w * int_w / (np.sum(s_w * int_w) + np.finfo(float).eps)
            w = s_w*int_w/np.sum(s_w*int_w)

            for c in range(ch):
                wp = w * n[:, :, c]
                res[i, j, c] = np.sum(wp)

    return np.uint8(res)

def solution(image_path_a, image_path_b):
    ############################
    ############################
    ## image_path_a is path to the non-flash high ISO image
    ## image_path_b is path to the flash low ISO image
    ############################
    ############################
    ## comment the line below before submitting else your code wont be executed##
    # pass
    # image = cv2.imread(image_path_b)
    
    A = cv2.imread(image_path_a)
    F = cv2.imread(image_path_b) 
    # A = cv2.imread('ultimate_test/2_a.jpg')
    # F = cv2.imread('ultimate_test/2_b.jpg')
    # # show(A)
    # show(F)\
    sigma_s = 5
    sigma_c = 10
    d = 15
    A_base = cbf(A,F,d, sigma_s, sigma_c)
    
    
    return A_base
