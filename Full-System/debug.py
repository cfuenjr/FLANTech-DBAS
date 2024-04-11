import os
import cv2
import numpy as np
import serial
from adafruit_fingerprint import Adafruit_Fingerprint
import adafruit_fingerprint
from PIL import Image

def preprocess_and_thin(image_path):
    img = cv2.imread(image_path)
    if img is None:
        img = cv2.imread(filename)
        raise ValueError("Image could not be loaded")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eq = cv2.equalizeHist(gray)
    blurred = cv2.GaussianBlur(eq, (3,3), 0)
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thinned_img = cv2.ximgproc.thinning(cv2.bitwise_not(binary))
    return thinned_img

input_img_path = "/home/pi/Downloads/full_system/tmp/user.png"
input_img = preprocess_and_thin(input_img_path)

sift = cv2.SIFT_create(nfeatures=1000, nOctaveLayers=3, contrastThreshold=0.04, edgeThreshold=10, sigma=1.6)
keypoints_1, descriptors_1 = sift.detectAndCompute(input_img, None)

best_score = 0
filename = None
best_match_image = None
best_kp1 = keypoints_1
best_kp2 = None
best_final_matches = []

flann = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 5}, {'checks': 50})

for file in os.listdir("/home/pi/Downloads/full_system/Fingerprint-Database"):
    fingerprint_image_path = os.path.join("/home/pi/Downloads/full_system/Fingerprint-Database", file)
    fingerprint_image = preprocess_and_thin(fingerprint_image_path)

    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

    if descriptors_1 is None or descriptors_2 is None or len(descriptors_1) < 2 or len(descriptors_2) < 2:
        continue

    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    good_matches = [m for m, n in matches if m.distance < 0.70 * n.distance]

    if len(good_matches) >= 4:
        src_pts = np.float32([keypoints_1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints_2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, ransacReprojThreshold=5.0, confidence=0.99)

        if mask is not None:
            num_matches = np.sum(mask)
            score = num_matches / len(mask) * 100

            if score > best_score:
                best_score = score
                filename = file
                best_match_image = fingerprint_image
                best_kp2 = keypoints_2
                best_final_matches = [good_matches[i] for i, m in enumerate(mask) if m[0]]

if best_match_image is not None and best_final_matches:
    result = cv2.drawMatches(input_img, best_kp1, best_match_image, best_kp2, best_final_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    print(f"Fingerprint match found: {filename}, Score: {best_score}%")
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No match found.")

