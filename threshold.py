import cv2
from matplotlib import pyplot as plt
import matplotlib.cm as cm


def threshold(img):
    img[img < 150] = 0


def main():

    img = cv2.imread('kidface.jpg', cv2.IMREAD_GRAYSCALE)

    threshold(img)

    plt.imshow(img, cmap=cm.Greys_r)
    plt.show()


if __name__ == '__main__':
    main()
