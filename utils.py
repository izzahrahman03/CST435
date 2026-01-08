import os
import cv2
from filters import grayscale, gaussian_blur, sobel_edge, sharpen, adjust_brightness

def process_image(img_path, output_dir):
    # Reads an image, applies a sequence of image processing filters, and saves the result.
    try:
        # Load the image from the given file path
        img = cv2.imread(img_path)
        if img is None:
            return False

        # Apply image processing filters sequentially
        gray = grayscale(img)
        blur = gaussian_blur(gray)
        edge = sobel_edge(blur)
        sharp = sharpen(blur)
        final = adjust_brightness(sharp)

        # Create output directory and save the processed image
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.basename(img_path)
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, final)

        return True

    except Exception as e:
        # Handle and report any errors during image processing
        print(f"Error processing {img_path}: {e}")
        return False
