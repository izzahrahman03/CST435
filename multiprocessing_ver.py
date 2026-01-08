import os
import time
from multiprocessing import Pool
from utils import process_image

# Directory containing the input image dataset
DATASET_DIR = "dataset"

# Base directory for output images processed using multiprocessing
OUTPUT_BASE = os.path.join("output", "mp")

def get_images():
    # Collects all .jpg and .jpeg image file paths from the dataset directory.
    images = []
    for root, _, files in os.walk(DATASET_DIR):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg")):
                images.append(os.path.join(root, f))
    return images

def wrapper(args):
    # Unpacks arguments and calls the image processing function.
    img_path, out_dir = args
    return process_image(img_path, out_dir)

if __name__ == "__main__":
    # Retrieve all image paths and count total images
    images = get_images()
    total_images = len(images)

    print("========================================")
    print("MODE : MULTIPROCESSING (AUTO 2,4,8)")
    print("========================================")

    # Execute image processing using different numbers of worker processes
    for workers in [2, 4, 8]:
        output_dir = os.path.join(OUTPUT_BASE, f"{workers}_proc")
        os.makedirs(output_dir, exist_ok=True)

        # Record start time
        start = time.time()

        # Create a multiprocessing pool to distribute tasks across processes
        with Pool(processes=workers) as pool:
            results = pool.map(wrapper, [(img, output_dir) for img in images])

        # Record end time
        end = time.time()

        # Count successful and failed image processing results
        success = sum(1 for r in results if r)
        fail = total_images - success

        print(f"\n--- PROCESSES: {workers} ---")
        print(f"TOTAL IMAGES   : {total_images}")
        print(f"SUCCESS        : {success}")
        print(f"FAILED         : {fail}")
        print(f"TIME (seconds) : {end - start:.3f}")

    print("\nAll multiprocessing experiments completed.")
