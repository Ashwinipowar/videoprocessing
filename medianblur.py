#it remove noise
import cv2
image=cv2.imread("camel.jpg")
blurred=cv2.medianBlur(image,5)
cv2.imshow("original image",image)
cv2.imshow("blurred image",blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()
