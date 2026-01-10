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

This project evaluates the effectiveness of parallel computing techniques for image filtering and performance evaluation using Python. Two parallel programming paradigms are implemented and compared:

- Multiprocessing using Python’s multiprocessing module
- Concurrent execution using Python’s concurrent.futures, including:
  - ProcessPoolExecutor for process-based parallelism
  - ThreadPoolExecutor for thread-based parallelism

A sequential implementation is used as a baseline for performance comparison. The primary objective is to analyze how data parallelism improves performance by measuring execution time, speedup and parallel efficiency.

All experiments are deployed and executed on a Google Cloud Platform (GCP) virtual machine while varying the number of workers (2, 4 and 8) to evaluate scalability, parallel overhead and resource utilization.

---

### **2. Dataset Description**
The dataset consists of 2000 food images, equally distributed across two categories:
- 1000 images of carrot cake
- 1000 images of chicken curry

Images are stored in JPG format with varying resolutions. The dataset is organized into category-based directories and dynamically discovered at runtime using directory traversal. This design allows the dataset to be extended or modified without requiring changes to the codebase.

---

### **3. Image Processing Pipeline**
Each image is processed using a fixed sequential pipeline consisting of five filters:

- Grayscale Conversion - Convert RGB images to grayscale using luminance formula
- Gaussian Blur - Apply 3×3 Gaussian kernel for smoothing
- Edge Detection - Sobel filter to detect edges
- Image Sharpening - Enhance edges and details
- Brightness Adjustment - Increase or decrease image brightness
  
---

### **4. Project Structure**
```lua
.
├── dataset/
│   ├── carrot_cake/
│   └── chicken_curry/
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
├── concurrent_futures_process.py
├── concurrent_futures_thread.py
├── filters.py
├── multiprocessing_ver.py
├── sequential.py
└── utils.py
```
---

### **5. System Requirement**
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

### **6. Environment Setup**
1. Instance Configuration
- Navigate to the Compute Engine section in the Google Cloud Console.
- Select Create Instance.
- Machine Family: Select General purpose, Series E2.
- Machine Type: Select E2 series and e2-standard-8.
- Boot Disk: Select Debian GNU/Linux 12 (bookworm) with 10 GB storage.
- Firewall: Default settings are sufficient.

2.  Install System Dependency
    ```bash
    sudo apt update
    sudo apt install git
    sudo apt install -y python3-venv python3-full
    sudo apt install -y libgl1 libglib2.0-0
    ```
3. Git Clone and Navigate to Project Folder
   ```bash
   git clone https://github.com/izzahrahman03/CST435.git
   cd CST435
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

### **7. How to Run the Programs**

You are required to run these commands:

1.  Sequential Execution
    ```bash
    python sequential.py
    ```
2.  Multiprocessing Execution
    ```bash
    python multiprocessing_ver.py
    ```
3.  Concurrent.futures Process Execution
    ```bash
    python concurrent_futures_process.py
    ```
4.  Concurrent.futures Thread Execution
    ```bash
    python concurrent_futures_thread.py
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

**Execution Time Results Details**
| Workers | Method       | Run 1 (s) | Run 2 (s) | Run 3 (s) | Total Run (s) | Average Calculation | Average Execution Time (s) |
| ------: | ------------ | --------: | --------: | --------: | ------------: | ------------------- | -------------------------: |
|       1 | Sequential   |    15.804 |    14.690 |    15.062 |        45.556 | 45.556 / 3          |                     15.185 |
|       2 | MP           |     7.877 |     8.133 |     8.100 |        24.110 | 24.110 / 3          |                      8.037 |
|       4 | MP           |     5.161 |     5.406 |     5.422 |        15.989 | 15.989 / 3          |                      5.330 |
|       8 | MP           |     2.990 |     4.012 |     4.974 |        11.976 | 11.976 / 3          |                      3.992 |
|       2 | CF – Process |     7.870 |     8.617 |     8.495 |        24.982 | 24.982 / 3          |                      8.327 |
|       4 | CF – Process |     5.413 |     5.619 |     5.657 |        16.689 | 16.689 / 3          |                      5.563 |
|       8 | CF – Process |     3.469 |     4.191 |     5.623 |        13.283 | 13.283 / 3          |                      4.428 |
|       2 | CF – Thread  |     8.339 |     8.281 |     8.436 |        25.056 | 25.056 / 3          |                      8.352 |
|       4 | CF – Thread  |     5.265 |     5.579 |     5.218 |        16.062 | 16.062 / 3          |                      5.354 |
|       8 | CF – Thread  |     3.324 |     3.685 |     5.204 |        12.213 | 12.213 / 3          |                      4.071 |
                    |

**Average Execution Time Comparison**
Average Sequential Time (s): 15.185

| Workers | Multiprocessing (s) | Concurrent.futures – Process (s) | Concurrent.futures – Thread (s) |
| ------: | ------------------: | -------------------------------: | ------------------------------: |
|       2 |               8.037 |                            8.327 |                           8.352 |
|       4 |               5.330 |                            5.563 |                           5.354 |
|       8 |               3.992 |                            4.428 |                           4.071 |



**Multiprocessing Speedup and Efficiency**
| Workers | Speedup (×) | Efficiency (%) |
| ------: | ----------: | -------------: |
|    2    |   1.889×    |      94.45     |
|    4    |   2.849×    |      71.23     |
|    8    |   3.803×    |      47.54     |

**Concurrent.futures Process-Based Speedup and Efficiency**
| Workers | Speedup (×) | Efficiency (%) |
| ------: | ----------: | -------------: |
|    2    |   1.824x    |      91.20     |
|    4    |   2.730x    |      68.25     |
|    8    |   3.429x    |      42.86     |

**Concurrent.futures Thread-Based Speedup and Efficiency**
| Workers | Speedup (×) | Efficiency (%) |
| ------: | ----------: | -------------: |
|    2    |   1.818x    |      90.90     |
|    4    |   2.836x    |      70.90     |
|    8    |   3.730x    |      46.63     |
