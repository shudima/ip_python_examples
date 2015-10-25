import cv2
from matplotlib import pyplot as plt
import matplotlib.cm as cm


def add_value(img, i, j, count, sum):
    if 0 <= j < len(img[0]) and 0 <= i < len(img):
        count += 1
        sum += img[i, j]

    return count, sum


def smooth(img):
    for i in range(len(img)):
        for j in range(len(img)):

            count = 0
            sum = 0

            for i1 in range(i-1, i+2):
                for j1 in range(j-1, j+2):

                    count, sum = add_value(img, i1, j1, count, sum)

            img[i, j] = sum/count


def main():

    img = cv2.imread('circle.jpg', cv2.IMREAD_GRAYSCALE)

    smooth(img)

    plt.imshow(img, cmap=cm.Greys_r)
    plt.show()


if __name__ == '__main__':
    main()