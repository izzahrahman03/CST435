import os
import time
from concurrent.futures import ProcessPoolExecutor
from utils import process_image

# Root directory containing all input images
DATASET_DIR = "dataset"

# Base directory for output images processed using concurrent.futures
OUTPUT_BASE = os.path.join("output", "cf")

def get_images():
    """
    Traverse the dataset directory and collect all image file paths.
    Only .jpg and .jpeg files are included.
    """
    images = []
    for root, _, files in os.walk(DATASET_DIR):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg")):
                images.append(os.path.join(root, f))
    return images

def wrapper(args):
    """
    Wrapper function to unpack arguments.
    This is required because executor.map() accepts only
    a single iterable of arguments.
    """
    img_path, out_dir = args
    return process_image(img_path, out_dir)

if __name__ == "__main__":
    # Retrieve all image paths from the dataset
    images = get_images()
    total_images = len(images)

    print("================================================")
    print("MODE : CONCURRENT.FUTURES PROCESS (AUTO 2,4,8)")
    print("================================================")

    # Run experiments with different numbers of worker processes
    for workers in [2, 4, 8]:
        # Create output directory for the current worker configuration
        output_dir = os.path.join(OUTPUT_BASE, f"{workers}_workers")
        os.makedirs(output_dir, exist_ok=True)

        # Record start time
        start = time.time()

        # Create a process pool executor
        # Each process runs independently, bypassing the GIL
        with ProcessPoolExecutor(max_workers=workers) as executor:
            # Distribute image processing tasks across worker processes
            results = list(
                executor.map(
                    wrapper,
                    [(img, output_dir) for img in images]
                )
            )

        # Record end time
        end = time.time()

        # Count successful and failed image processing results
        success = sum(1 for r in results if r)
        fail = total_images - success

        # Display performance results
        print(f"\n--- WORKERS: {workers} ---")
        print(f"TOTAL IMAGES   : {total_images}")
        print(f"SUCCESS        : {success}")
        print(f"FAILED         : {fail}")
        print(f"TIME (seconds) : {end - start:.3f}")

    print("\nAll concurrent.futures experiments completed.")

