# count the number of circles in the image
import cv2
import numpy as np
image = cv2.imread("blobs.png",0)
# set our filtering parameters using SimpleBlobDetector Function
params = cv2.SimpleBlobDetector_Params()
# change thresholds
params.filterByArea = True
params.minArea = 100
# set circukarity
params.filterByCircularity = True
params.minCircularity = 0.9
# set convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.2
# set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.1
# create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(image)
#detect blobs
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs = len(keypoints)
print("Number of blobs detected: ", number_of_blobs)
cv2.imshow("Blobs circular",blobs)
cv2.waitKey(20000)
cv2.destroyAllWindows()