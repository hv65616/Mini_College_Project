import numpy as np
import cv2
import glob
import os

logo = cv2.imread("logo.png")
h_logo, w_logo = logo.shape[:2]

images_path = glob.glob("images/*.*")

print(images_path)

print("Adding Watermark")
for image_path in images_path:

    img = cv2.imread(image_path)
    h_img, w_img = img.shape[:2]

    scale = 40
    h = int(logo.shape[0]*scale/100)
    w = int(logo.shape[1]*scale/100)
    dim = (w, h)
    updated_logo = cv2.resize(logo, dim, interpolation=cv2.INTER_AREA)
    ulh, ulw = logo.shape[:2]

    centre_y = int(h_img/2)
    centre_x = int(w_img/2)
    top_y = centre_y - int(h_logo/2)
    left_x = centre_x - int(w_logo/2)
    bottom_y = top_y+h_logo
    right_x = left_x+w_logo
    # cv2.circle(img, (left_x, top_y), 30, (0, 255, 0), -1)
    # cv2.circle(img, (right_x, bottom_y), 30, (0, 255, 0), -1)

    roi = img[top_y:bottom_y, left_x:right_x]
    # img[top_y:bottom_y, left_x:right_x] = logo
    result = cv2.addWeighted(roi, 0.5, logo, 0.5, 0)
    img[top_y:bottom_y, left_x:right_x] = result
    filename = os.path.basename(image_path)
    cv2.imwrite(filename+" Watermarked", img)

    # print(h_img, end=" ")
    # print(w_img, end=" ")
    # print(centre_y, end=" ")
    # print(centre_x, end=" ")
    # print(top_y, end=" ")
    # print(left_x, end=" ")
    # print(bottom_y, end=" ")
    # print(right_x, end=" ")

print("Watermarked Images")
# cv2.imshow("Logo", logo)
# cv2.imshow("Image", img)
#
# cv2.imshow("ROI", roi)
#
# cv2.imshow("Result", result)
# cv2.waitKey(0)
