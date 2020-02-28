import os

import cv2

def stich(left_i,right_i):

    dim=(1024,768)
    left = cv2.imread(str(left_i),cv2.IMREAD_COLOR)
    left = cv2.resize(left, dim, interpolation= cv2.INTER_AREA)
    right = cv2.imread(str(right_i),cv2.IMREAD_COLOR)
    right = cv2.resize(right, dim, interpolation= cv2.INTER_AREA)

    images = [left, right]

    stitcher = cv2.Stitcher.create()
    ret, pano = stitcher.stitch(images)

    if ret == cv2.STITCHER_OK:
        # cv2.imshow('Panorama', pano)
        cv2.imwrite('./Panorama.jpg', pano)
        cv2.waitKey()
        cv2.destroyAllWindows()
    else:
        print("Error during Stitching")

    # return pano

# image1= os.path.join(os.path.abspath('imageProcessing'), "uttower_left.jpeg")
# image2= os.path.join(os.path.abspath('imageProcessing'), "uttower_right.jpeg")
# stich( "uttower_right.jpeg", "uttower_left.jpeg")