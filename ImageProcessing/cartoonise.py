import cv2
import sys

def cartoonise(file):
       
   num_bilateral = 9 # For filtering process!!!

   imgRead = cv2.imread(file)

   imgProcess = imgRead

   #cv2.bilateralFilter(img,diameter,sigmaColor,sigmaSpace)

   for _ in range(num_bilateral):
      imgProcess = cv2.bilateralFilter(imgProcess, d=9, sigmaColor=9, sigmaSpace=7)

   # Edge mask....
   #cv2.adaptiveThreshold(src, dst, adaptedMethod, thresHoldType,blocksize )

   imgConvertedGrey = cv2.cvtColor(imgRead, cv2.COLOR_RGB2GRAY)
   imgBlur = cv2.medianBlur(imgConvertedGrey, 7)

   imgEdge = cv2.adaptiveThreshold(imgBlur, 255,
      cv2.ADAPTIVE_THRESH_MEAN_C,
      cv2.THRESH_BINARY,
      blockSize=9,
      C=2)

   imgEdge = cv2.cvtColor(imgEdge, cv2.COLOR_GRAY2RGB)
   imgProcess = cv2.bitwise_and(imgProcess, imgEdge)

   return imgProcess



# image = cartoonise("download-3.png")
#
# #You can change to jpg,png,jpeg, but other file extension might have trouble.
# cv2.imwrite('./cartoon.jpg',image)



