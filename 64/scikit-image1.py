import skimage as ski

image = ski.data.coins()
# ... or any other NumPy array!

ski.io.imshow(image)
ski.io.show()

edges = ski.filters.sobel(image)
ski.io.imshow(edges)
ski.io.show()