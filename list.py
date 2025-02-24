from PIL import Image, ImageOps, ImageFilter

# Load the image
image_path = "Screenshots\Screenshot 2025-02-20 200115.png"
image = Image.open(image_path)

# Convert to grayscale
gray_image = ImageOps.grayscale(image)

# Invert the grayscale image
inverted_image = ImageOps.invert(gray_image)

# Apply Gaussian Blur to the inverted image
blurred_image = inverted_image.filter(ImageFilter.GaussianBlur(radius=15))

# Blend grayscale and blurred images to create a pencil sketch effect
sketch_image = Image.blend(gray_image, blurred_image, alpha=0.5)

# Show and save the final sketch
sketch_image.show()
sketch_image.save("Screenshots\Screenshot 2025-02-20 200115.png")
