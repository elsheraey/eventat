import argparse
import requests
import cv2
import numpy as np
import PIL.Image

ap = argparse.ArgumentParser()
ap.add_argument('-u', '--url', required=True)
ap.add_argument('-f', '--filename', required=True)

args = vars(ap.parse_args())

image = open(args['filename'], 'rb')

res = requests.post(args['url'], files={'image': image}).json()
skeleton, points = res['skeleton'], res['points']

# Draw Skeleton
image = cv2.cvtColor(np.array(PIL.Image.open(image)), cv2.COLOR_RGB2BGR)

for pair in skeleton:
    partA = pair[0]
    partB = pair[1]

    if points[partA] and points[partB]:
        cv2.line(image, tuple(points[partA]), tuple(points[partB]), (0, 255, 255), 2)
        cv2.circle(image, tuple(points[partA]), 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

cv2.imshow('OpenPose', image)
cv2.waitKey(0)
