import cv2
import numpy as np
image=cv2.imread("img/shadow.png")
px=image[229, 982]
px1=image[554, 890]

h, w=image.shape[:2]
resized=cv2.resize(image, (w//2, h//2))
image_roi=resized[0:510//2, 0:1195//2]
image2_roi=resized[510//2: 640//2, 0:1194//2]
gray_image=cv2.cvtColor(image_roi, cv2.COLOR_BGR2GRAY)
ret, thresh=cv2.threshold(gray_image, 60, 255, cv2.THRESH_BINARY_INV)

kernel=np.ones((5,5),np.uint8)
img_erosion=cv2.erode(thresh, kernel, iterations=1)
# cv2.imshow("erosion", img_erosion)

dilation=cv2.dilate(thresh, kernel, iterations=1)
results1=image_roi.copy()
results1[dilation==255]=px
print(results1)

# cv2.imshow("delation", results1)


gray=cv2.cvtColor(image2_roi, cv2.COLOR_BGR2GRAY)
ret, thresh1=cv2.threshold(gray, 60,255,cv2.THRESH_BINARY_INV)
kernel1=np.ones((5,5), np.uint8)
img_erosion1=cv2.erode(thresh1, kernel, iterations=1)
dilation1=cv2.dilate(thresh1, kernel1, iterations=1)
results2=image2_roi.copy()
results2[dilation1==255]=px1
# cv2.imshow("delation1", results2)

print(image_roi.shape)
print(image2_roi.shape)

im_v=cv2.vconcat([results1, results2])
cv2.imshow("image", im_v)



gray=cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
ret, thresh=cv2.threshold(gray, 60,255,cv2.THRESH_BINARY_INV)

result=resized.copy()
result[thresh==255]=px

# cv2.imread("thresh1", thresh)
# cv2.imshow("result1", results1)
# cv2.imshow("result2", results2)
# cv2.imshow("result", result)

cv2.imshow("resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

