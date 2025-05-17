import cv2
import numpy as np


img1 = cv2.imread("frame1.jpeg")
img2 = cv2.imread("frame2.jpeg")


if img1 is None or img2 is None:
    print("Erro ao carregar as imagens. Verifique os nomes e o caminho.")
    exit()


img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))


gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


flow = cv2.calcOpticalFlowFarneback(
    gray1, gray2,
    None, 0.5, 3, 15, 3, 5, 1.2, 0
)


hsv = np.zeros_like(img1)
hsv[..., 1] = 255

mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
hsv[..., 0] = ang * 180 / np.pi / 2
hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


cv2.imshow("Movimento Estimado", rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
