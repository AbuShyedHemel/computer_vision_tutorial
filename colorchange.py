import cv2
from matplotlib import pyplot as plt
#img = cv2.imread('picture\smarties.png',0)

img = cv2.imread('picture\smarties.png',0)
# cv2.imshow('frame',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(img)
plt.show()