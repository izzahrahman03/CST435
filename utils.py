import os
import cv2
from filters import grayscale, gaussian_blur, sobel_edge, sharpen, adjust_brightness

def process_image(img_path, output_dir):
    try:
        img = cv2.imread(img_path)
        if img is None:
            return False

        # Apply filters
        gray = grayscale(img)
        blur = gaussian_blur(gray)
        edge = sobel_edge(blur)
        sharp = sharpen(blur)
        final = adjust_brightness(sharp)

        # Save output
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.basename(img_path)
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, final)

        return True

    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        return False
