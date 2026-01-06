import os
import time
from utils import process_image

# DATASET_DIR = "dataset"
DATASET_DIR = "dataset2"
OUTPUT_DIR = os.path.join("output", "sequential")

def get_images():
    images = []
    for root, _, files in os.walk(DATASET_DIR):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg")):
                images.append(os.path.join(root, f))
    return images

if __name__ == "__main__":
    images = get_images()
    total_images = len(images)
    success = 0
    fail = 0

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    start = time.time()
    for img in images:
        if process_image(img, OUTPUT_DIR):
            success += 1
        else:
            fail += 1
    end = time.time()

    print("========================================")
    print("MODE           : SEQUENTIAL")
    print(f"TOTAL IMAGES   : {total_images}")
    print(f"SUCCESS        : {success}")
    print(f"FAILED         : {fail}")
    print(f"TIME (seconds) : {end - start:.3f}")
    print(f"OUTPUT FOLDER  : {OUTPUT_DIR}")
    print("========================================")
