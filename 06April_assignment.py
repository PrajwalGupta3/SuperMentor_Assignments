# Assignment Name : Image as Numbers
# Description : Load an image, print shape, pixel values, channels, and explain them.

"""
In Computer Vision, an image is nothing more than a structured grid of numbers.
This script demonstrates:
1. Loading/Creating an image as a Multi-dimensional Array (Matrix).
2. Inspecting the dimensions (Height, Width, Channels).
3. Accessing individual pixel values and understanding RGB channels.
"""

import numpy as np
try:
    import cv2
except ImportError:
    print("OpenCV (cv2) not found. Please install it using: pip install opencv-python")
    cv2 = None

def explain_image_data(image):
    """Prints and explains the numerical data of an image."""
    print("-" * 60)
    print("1. IMAGE SHAPE (Dimensions)")
    print("-" * 60)
    
    # image.shape returns (Height, Width, Channels)
    shape = image.shape
    print(f"Shape: {shape}")
    print(f" - Vertical Pixels (Height): {shape[0]}")
    print(f" - Horizontal Pixels (Width): {shape[1]}")
    print(f" - Color Channels: {shape[2] if len(shape) > 2 else 1}")
    
    print("\n" + "-" * 60)
    print("2. PIXEL VALUES (A Closer Look)")
    print("-" * 60)
    
    # Access middle pixel
    mid_h, mid_w = shape[0] // 2, shape[1] // 2
    pixel_value = image[mid_h, mid_w]
    
    print(f"Pixel at coordinates ({mid_h}, {mid_w}): {pixel_value}")
    
    if len(shape) > 2:
        print("\nBreakdown of Channels (BGR in OpenCV):")
        print(f" - Blue Intensity:  {pixel_value[0]}")
        print(f" - Green Intensity: {pixel_value[1]}")
        print(f" - Red Intensity:   {pixel_value[2]}")
        print("Note: Values range from 0 (Black) to 255 (Full Intensity).")
    
    print("\n" + "-" * 60)
    print("3. RAW MATRIX DATA (Sample 5x5 Grid)")
    print("-" * 60)
    # Print a tiny slice of the image matrix
    print(image[0:5, 0:5, 0]) # Just the first channel (Blue) for simplicity
    print("\nResult: Each number represents the brightness of a specific color at that pixel.")

def create_demo_image():
    """Generates a simple 3-channel gradient image using NumPy."""
    # Create a 200x200 image with 3 channels
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    
    # Fill with a Blue-Red gradient
    for y in range(200):
        for x in range(200):
            img[y, x] = [x % 256, (x+y) % 256, y % 256] # [B, G, R]
            
    return img

def main():
    print("="*60)
    print("           ASSIGNMENT : IMAGE AS NUMBERS")
    print("="*60)

    # 1. Attempt to load an actual image (if exists) or create a demo one
    img_path = 'sample_image.jpg' # Potential placeholder
    
    if cv2:
        image = cv2.imread(img_path)
        if image is None:
            print(f"Could not find '{img_path}'. Generating a synthetic image for demonstration...")
            image = create_demo_image()
        else:
            print(f"Successfully loaded '{img_path}'.")
    else:
        print("Using NumPy to create a sample matrix since OpenCV is missing.")
        image = create_demo_image()

    # 2. Analyze the image
    explain_image_data(image)
    
    # 3. Save the generated image if possible
    if cv2:
        output_file = 'output_demo.png'
        cv2.imwrite(output_file, image)
        print(f"\n[SUCCESS] Demo image saved as '{output_file}' for visual verification.")

if __name__ == "__main__":
    main()
