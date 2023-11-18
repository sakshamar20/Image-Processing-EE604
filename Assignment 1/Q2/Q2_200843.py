import cv2
import numpy as np
import librosa

def solution(audio_path):
    ############################
    ############################


    y, sr = librosa.load(audio_path, sr=None)
    n_fft = 2048
    hop_length = 512
    spec = librosa.feature.melspectrogram(y=y,sr=sr,n_fft=n_fft, hop_length = hop_length, fmax = 22000)
    fspec = spec.ravel()
    mean = np.mean(fspec)
    # print(mean)
    if(mean>2.5):
        class_name1 = 'metal'
    else:
        class_name2 = 'cardboard'
        
    fft_score = abs(np.fft.fft2(spec)).max()
    # print(fft_score)
    if(fft_score>20000):
        class_name = 'metal'
    else:
        class_name = 'cardboard'
    
    ############################
    ############################
    

    return class_name
