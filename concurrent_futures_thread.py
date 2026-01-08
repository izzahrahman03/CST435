import os
import time
from concurrent.futures import ThreadPoolExecutor
from utils import process_image

# Directory containing the input image dataset
DATASET_DIR = "dataset"

# Base directory for output images processed using concurrent.futures
OUTPUT_BASE = os.path.join("output", "cf")

def get_images():
    # Collects all .jpg image file paths from the dataset directory.
    images = []
    for root, _, files in os.walk(DATASET_DIR):
        for f in files:
            if f.lower().endswith((".jpg")):
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

    print("================================================")
    print("MODE : CONCURRENT.FUTURES THREADS (AUTO 2,4,8)")
    print("================================================")

    # Execute image processing using different numbers of worker threads
    for workers in [2, 4, 8]:
        output_dir = os.path.join(OUTPUT_BASE, f"{workers}_workers")
        os.makedirs(output_dir, exist_ok=True)

        # Record the start time
        start = time.time()

        # Create a thread pool executor to run tasks concurrently using threads
        with ThreadPoolExecutor(max_workers=workers) as executor:
            results = list(executor.map(wrapper, [(img, output_dir) for img in images]))

        # Record the end time
        end = time.time()

        # Count successful and failed image processing results
        success = sum(1 for r in results if r)
        fail = total_images - success

        print(f"\n--- WORKERS: {workers} ---")
        print(f"TOTAL IMAGES   : {total_images}")
        print(f"SUCCESS        : {success}")
        print(f"FAILED         : {fail}")
        print(f"TIME (seconds) : {end - start:.3f}")

    print("\nAll concurrent.futures thread experiments completed.")
