import os
import cv2
import numpy as np


def create_silhouettes(video_path, s_output_path, c_output_path):
    # Open the video
    cap = cv2.VideoCapture(video_path)
    fgbg = cv2.createBackgroundSubtractorKNN()  # KNN Background subtractor

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Video ended or failed

        # Apply background subtraction
        fgmask = fgbg.apply(frame)

        # Use adaptive thresholding to get a binary image
        _, thresh = cv2.threshold(fgmask, 254, 255,
                                  cv2.THRESH_BINARY)

        # Fill in holes using morphological closing
        kernel = np.ones((5, 5), np.uint8)
        closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # Find contours and fill them
        contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        silhouette = cv2.drawContours(closing.copy(), contours, -1, (255, 255, 255), thickness=cv2.FILLED)

        # Apply a binary threshold to get a binary image
        _, binary_image = cv2.threshold(silhouette, 1, 255, cv2.THRESH_BINARY)

        # Find all contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Assuming that the largest contour by area is the person
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)

        # Create a mask for the largest contour
        mask = np.zeros_like(binary_image)
        cv2.drawContours(mask, [largest_contour], -1, color=255, thickness=cv2.FILLED)

        # Create a new image that isolates the largest contour
        isolated_image = cv2.bitwise_and(silhouette, silhouette, mask=mask)

        # Draw contours onto normal image and save
        frame_with_contours = cv2.drawContours(frame.copy(), largest_contour, -1, (0, 255, 0), 3)
        contour_output_path = f"{c_output_path}/contours_{frame_count:04d}.png"
        cv2.imwrite(contour_output_path, frame_with_contours)

        # Save the silhouette to a file
        silhouette_output_path = f"{s_output_path}/silhouette_{frame_count:04d}.png"
        cv2.imwrite(silhouette_output_path, isolated_image)
        frame_count += 1

    cap.release()
    print(f"Processed {frame_count} frames.")


def clean_folders(cPath_r, cPath_w, oPath_r, oPath_w):
    # Remove all files in Contours_R and Contours_W
    for filename in os.listdir(cPath_r):
        path = os.path.join(cPath_r, filename)
        if os.path.isfile(path):
            os.remove(path)

    for filename in os.listdir(cPath_w):
        path = os.path.join(cPath_w, filename)
        if os.path.isfile(path):
            os.remove(path)

    # Remove all files in Silh_R and Silh_W
    for filename in os.listdir(oPath_r):
        path = os.path.join(oPath_r, filename)
        if os.path.isfile(path):
            os.remove(path)

    for filename in os.listdir(oPath_w):
        path = os.path.join(oPath_w, filename)
        if os.path.isfile(path):
            os.remove(path)
