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

This project evaluates the performance of different execution models for image processing tasks such as:

1. Sequential execution
2. Multiprocessing
3. Concurrent execution using concurrent.futures

The objective is to analyze how parallelism improves performance by measuring:

1. Execution time
2. Speedup
3. Efficiency

Experiments are conducted by varying the number of workers and processes (2, 4 and 8) on the same virtual machine.

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

1.  Install System Dependency
    ```bash
    sudo apt update
    sudo apt install -y python3-venv python3-full
    sudo apt install -y libgl1 libglib2.0-0
    ```
2.  Create Virtual Environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Install Required Packages
    ```bash
    pip install numpy opencv-python pillow matplotlib
    ```
---

### **4. How to Run the Programs**

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

