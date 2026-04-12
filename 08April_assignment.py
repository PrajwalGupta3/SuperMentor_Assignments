# Assignment Name : Image Filter Lab
# Description : Use OpenCV to grayscale, blur, detect edges and show before/after.

"""
This script demonstrates the three most common preprocessing steps in Computer Vision:
1. Grayscale Conversion: Reducing complexity by removing color.
2. Gaussian Blur: Smoothing the image to reduce noise/detail.
3. Canny Edge Detection: Identifying boundaries between objects.
"""

import numpy as np
try:
    import cv2
except ImportError:
    print("OpenCV (cv2) not found. Please install it using: pip install opencv-python")
    cv2 = None

def apply_filters(image_path):
    if cv2 is None:
        return
        
    # 1. Load Image
    img = cv2.imread(image_path)
    if img is None:
        # Create a synthetic image if path doesn't exist
        print(f"File '{image_path}' not found. Creating a synthetic testing image...")
        img = np.zeros((400, 400, 3), dtype=np.uint8)
        cv2.circle(img, (200, 200), 100, (0, 255, 0), -1) # Green Circle
        cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), 5) # Blue Square
        cv2.putText(img, 'AI LAB', (100, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    
    # 2. Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 3. Apply Gaussian Blur (Kernel size 7x7)
    # The kernel size must be odd. Larger kernel = more blur.
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    
    # 4. Canny Edge Detection
    # Thresholds (100, 200) determine sensitivity to edges
    edges = cv2.Canny(blur, 100, 200)
    
    # 5. Save the results
    cv2.imwrite('1_Original.jpg', img)
    cv2.imwrite('2_Grayscale.jpg', gray)
    cv2.imwrite('3_Blurred.jpg', blur)
    cv2.imwrite('4_Edges.jpg', edges)
    
    print("\n[PROCESS STATUS]")
    print("-" * 30)
    print("✅ Original Saved -> 1_Original.jpg")
    print("✅ Grayscale Done -> 2_Grayscale.jpg")
    print("✅ Blur Applied   -> 3_Blurred.jpg")
    print("✅ Edges Detected -> 4_Edges.jpg")
    print("-" * 30)
    print("\nSummary: The process transformed a full-color image into a clean outline of its primary shapes.")

def main():
    print("="*60)
    print("           ASSIGNMENT : IMAGE FILTER LAB")
    print("="*60)
    
    img_name = 'input_image.jpg'
    apply_filters(img_name)

if __name__ == "__main__":
    main()
