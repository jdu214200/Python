from skimage.io import imread, imshow
import matplotlib.pyplot as plt

file = "images/Kolibri.jpg"

def rgbToGray(imageFile):
    image = imread(imageFile)
    image_grey = imread(imageFile, as_gray=True)

    print(image.shape)
    print(image_grey.shape)

    figura = plt.figure()

    figura.add_subplot(1,2, 1)
    plt.imshow(image)
    plt.title("Original tasvir")

    figura.add_subplot(1,2, 2)
    plt.imshow(image_grey, cmap="gray")
    plt.title("Kulrang tasvir")
    plt.show()