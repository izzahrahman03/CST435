import os
import time
from concurrent.futures import ProcessPoolExecutor
from utils import process_image

DATASET_DIR = "dataset"
OUTPUT_BASE = os.path.join("output", "cf")

def get_images():
    images = []
    for root, _, files in os.walk(DATASET_DIR):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg")):
                images.append(os.path.join(root, f))
    return images

def wrapper(args):
    img_path, out_dir = args
    return process_image(img_path, out_dir)

if __name__ == "__main__":
    images = get_images()
    total_images = len(images)

    print("========================================")
    print("MODE : CONCURRENT.FUTURES (AUTO 2,4,8)")
    print("========================================")

    for workers in [2, 4, 8]:
        output_dir = os.path.join(OUTPUT_BASE, f"{workers}_workers")
        os.makedirs(output_dir, exist_ok=True)

        start = time.time()
        with ProcessPoolExecutor(max_workers=workers) as executor:
            results = list(executor.map(wrapper, [(img, output_dir) for img in images]))
        end = time.time()

        success = sum(1 for r in results if r)
        fail = total_images - success

        print(f"\n--- WORKERS: {workers} ---")
        print(f"TOTAL IMAGES   : {total_images}")
        print(f"SUCCESS        : {success}")
        print(f"FAILED         : {fail}")
        print(f"TIME (seconds) : {end - start:.3f}")

    print("\nAll concurrent.futures experiments completed.")
