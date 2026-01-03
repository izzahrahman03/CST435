# CST435: Cloud and Parallel Computing Assignment 2

School of Computer Sciences - University Sains Malaysia
CST435 Cloud and Parallel Computing

Lecturer: Associate Professor Dr. Chong Yung Wey

Prepared by:
| NAME                                | MATRIC NUMBER |
|-------------------------------------|---------------|
| Nurul Afiqah Binti Azhar            | 160335        |
| Nur Aina Sofeya Binti Mohamed Yusof | 160423        |
| Siti Nawwarah Binti Mohd Abd Hadi   | 160304        |
| Siti Nur Izzah Binti Abdul Rahman   | 160302        |

---

### **1. Introduction**
This project evaluates the effectiveness of parallel computing techniques for accelerating image processing workloads. Three execution models are implemented and compared:
- Sequential execution
- Multiprocessing using Python’s multiprocessing module
- Concurrent execution using concurrent.futures
  
The primary objective is to analyze how data parallelism improves performance by measuring:
- Execution time
- Speedup
- Parallel efficiency

Experiments are conducted on the same virtual machine while varying the number of workers (2, 4, and 8) to observe scalability behavior and parallel overhead.

---

### **2. System Requirement**
**Operating System**
- Ubuntu 20.04 / 22.04 (GCP VM)

**Hardware**
- Google Cloud VM
- 8vCPUs

**Software**
- Python 3.10+
- Virtual Environment (venv)

**Required Libraries**
- numpy
- opencv-python
- pillow
- matplotlib

---

### **3. Environment Setup**
1. Instance Configuration
- Navigate to the Compute Engine section in the Google Cloud Console.
- Select Create Instance.
- Machine Family: Select General purpose, Series E2.
- Machine Type: Select E2 series and e2-standard-8.
- Boot Disk: Select Debian GNU/Linux 12 (bookworm) with 10 GB storage.
- Firewall: Default settings are sufficient.

3.  Install System Dependency
    ```bash
    sudo apt update
    sudo apt install -y python3-venv python3-full
    sudo apt install -y libgl1 libglib2.0-0
    ```
4.  Create Virtual Environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
5.  Install Required Packages
    ```bash
    pip install numpy opencv-python pillow matplotlib
    ```
---

### **4. Project Structure**
```lua
.
├── dataset/
│   ├── takoyaki/
│   ├── tiramisu/
│   └── waffle/
├── output/
│   ├── cf/
│   │   ├── 2_workers/
│   │   ├── 4_workers/
│   │   └── 8_workers/
│   ├── mp/
│   │   ├── 2_proc/
│   │   ├── 4_proc/
│   │   └── 8_proc/
│   └── sequential/
├── .gitignore
├── README.md
├── concurrent_futures.py
├── filters.py
├── multiprocessing_ver.py
├── sequential.py
└── utils.py
```
---

### **5. Dataset Description**
The dataset consists of 120 food images, equally distributed across three categories:
- 40 images of Waffles
- 40 images of Takoyaki
- 40 images of Tiramisu

Images are stored in JPEG format with varying resolutions. The dataset is organized into category-based directories and dynamically discovered at runtime using directory traversal. This design allows the dataset to be extended or modified without requiring changes to the codebase.

---

### **6. Image Processing Pipeline**
Each image is processed using a fixed sequential pipeline consisting of five filters:

Grayscale Conversion - Convert RGB images to grayscale using luminance formula
Gaussian Blur - Apply 3×3 Gaussian kernel for smoothing
Edge Detection - Sobel filter to detect edges
Image Sharpening - Enhance edges and details
Brightness Adjustment - Increase or decrease image brightness

---

### **7. How to Run the Programs**

1.  Sequential Execution
    ```bash
    python sequential.py
    ```
2.  Multiprocessing Execution
    ```bash
    python multiprocessing_ver.py
    ```
3.  Concurrent Futures Execution
    ```bash
    python concurrent_futures.py
    ```

Each execution prints:
1. Total images processed
2. Successful and failed images
3. Execution Time

---

### **8. Performance Analysis**

**Experimental Configuration**
1. Worker counts tested: 2, 4, 8
2. CPU cores available: 8 vCPUs
3. Same dataset used for all executions
4. Sequential execution used as baseline

**Speedup Results**
| Workers  | Multiprocessing Time (s) | Multiprocessing Speedup | Multiprocessing Speedup (s) |Multiprocessing Speedup |
|----------|--------------------------|-------------------------|-----------------------------|-------------------------|
| 2        | 0.560                    |1.37x                    |0.470                        |1.63x                    |
| 4        | 0.333                    |2.31x                    |0.331                        |2.32x                    |
| 8        | 0.258                    |2.98x                    |0.244                        |3.15                    |

**Efficiency Results**
| Workers  | Multiprocessing Efficiency  | Concurrent.futures Efficiency  |
|----------|-----------------------------|--------------------------------|
| 2        | 68.5%                       |81.5%                           |
| 4        | 57.8%                       |58.0%                           |
| 8        | 37.3%                       |39.4%                           |

