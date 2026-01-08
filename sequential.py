import os
import time
from utils import process_image

# Directory containing the input image dataset
DATASET_DIR = "dataset"

# Output directory for sequential image processing results
OUTPUT_DIR = os.path.join("output", "sequential")

def get_images():
    # Collects all .jpg image file paths from the dataset directory.
    images = []
    for root, _, files in os.walk(DATASET_DIR):
        for f in files:
            if f.lower().endswith((".jpg")):
                images.append(os.path.join(root, f))
    return images

if __name__ == "__main__":
    # Retrieve all image paths and initialize counters
    images = get_images()
    total_images = len(images)
    success = 0
    fail = 0

    # Create the output directory if it does not exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Record the start time
    start = time.time()

    # Process images one by one in a single thread
    for img in images:
        if process_image(img, OUTPUT_DIR):
            success += 1
        else:
            fail += 1

    # Record the end time
    end = time.time()

    print("========================================")
    print("MODE           : SEQUENTIAL")
    print(f"TOTAL IMAGES   : {total_images}")
    print(f"SUCCESS        : {success}")
    print(f"FAILED         : {fail}")
    print(f"TIME (seconds) : {end - start:.3f}")
    print(f"OUTPUT FOLDER  : {OUTPUT_DIR}")
    print("========================================")

