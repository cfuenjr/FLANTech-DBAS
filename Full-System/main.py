import tensorflow as tf
import keras
from keras import models

from userClass import Entry
import numpy as np
import pickle
import os
import cv2

import Collecting
from Collecting import save_fingerprint_images

from Enrollment import enroll
import CNN_features
import Gait_match
import Silh

def main():
    
    # Choose mode
    print("Choose Mode")
    print("1 - Verification Mode")
    print("2 - Enrollment Mode")
    choice = input("Enter your value: ")

    ##################
    ##### Camera #####
    ##################
    import camera
	
    # Paths and variables
    vPath_r = 'test.mkv'
    cPath_r = './Contours_R'
    oPath_r = './Silh_R'
    vPath_w = 'video.avi'
    cPath_w = './Contours_W'
    oPath_w = './Silh_W'
    
    ######################
    ##### Silhouette #####
    ######################
    # Clean contours and silhouette folders
    Silh.clean_folders(cPath_r, cPath_w, oPath_r, oPath_w)

    # Create silhouettes #for ribbon & web camera
    Silh.create_silhouettes(vPath_r, oPath_r, cPath_r)
    Silh.create_silhouettes(vPath_w, oPath_w, cPath_w)

    ####################
    ##### Features #####
    ####################
    # Load trained CNN model
    #model = keras.models.load_model('./CNN_model')

    # Create new class object and load data
    data = Entry()
    data.gait45 = CNN_features.get_feature(oPath_r)
    data.gait90 = CNN_features.get_feature(oPath_w)
	
    if choice == '1':
        with open('database.pkl', 'rb') as f:
            data_dict = pickle.load(f)
        similarities_45 = {key: Gait_match.cosine_similarity(value.gait45, data.gait45) for key, value in
                                           data_dict.items()}
        similarities_90 = {key: Gait_match.cosine_similarity(value.gait90, data.gait90) for key, value in
                                           data_dict.items()}
        print(similarities_45)
        print(similarities_90)

        import Fingerprint_Matching
    elif choice == '2':
        username = enroll(data)
        print("Person name: ", username)
        #import Collecting
        save_fingerprint_images(username, 5)
    else:
        print("Choose Mode")
        print("1 - Verification Mode")
        print("2 - Enrollment Mode")
        choice = input("Enter your value: ")


main()
