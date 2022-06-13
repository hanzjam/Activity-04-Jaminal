import cv2
egg = 'gudetama.jpg'
screenName = 'This is so me!!!'
imgRead = cv2.imread(egg, 1)
cv2.imshow(screenName, imgRead)
cv2.waitKey(0)
cv2.destroyAllWindows()