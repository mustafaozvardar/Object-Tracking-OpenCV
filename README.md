# 🚗 Object Tracking with Euclidean Distance Tracker 

## 📝 Project Overview

Welcome to the **Object Tracking** project! This project utilizes a custom `EuclideanDistTracker` class with OpenCV for tracking objects in videos. It includes:

- **Object Detection**: Detects moving objects using background subtraction.
- **Object Tracking**: Tracks objects across frames and assigns unique IDs based on Euclidean distance.

## 📋 Requirements

Make sure you have Python 3.x installed. You'll also need the following libraries:

- **OpenCV**: For image processing.
- **NumPy**: For numerical operations.

Install the required libraries using `pip`:

```bash
pip install opencv-python
pip install numpy
```

## 📁 Files
**main.py:** The main script for running object tracking.

**tracker.py:** Contains the implementation of the EuclideanDistTracker class.

## 🚀 Usage
Prepare Your Video: Place your video file (e.g., highway.mp4) in the same directory as main.py.

Run the Script:
```bash
python main.py
```

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for more details. 
