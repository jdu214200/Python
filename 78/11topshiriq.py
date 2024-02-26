from skimage import io, color, feature
import matplotlib.pyplot as plt

# Load a sample image from scikit-image
image = io.imread('https://flomaster.top/uploads/posts/2022-07/1658193727_35-flomaster-club-p-sapsan-ptitsa-risunok-krasivo-42.jpg')

# Convert the image to grayscale
gray_image = color.rgb2gray(image)

# Apply edge detection (Canny edge detector)
edges = feature.canny(gray_image)

# Display the original and processed images
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
ax = axes.ravel()

ax[0].imshow(image)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(gray_image, cmap=plt.cm.gray)
ax[1].set_title('Grayscale')
ax[1].axis('off')

ax[2].imshow(edges, cmap=plt.cm.gray)
ax[2].set_title('Edge Detection')
ax[2].axis('off')





plt.tight_layout()
plt.show()
