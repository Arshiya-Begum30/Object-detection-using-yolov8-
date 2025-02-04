# Object-detection-using-yolov8-


## Overview
This Streamlit application enables users to upload images and perform real-time object detection using the **YOLO** model. The uploaded image is processed, and detected objects are displayed along with bounding boxes. The app leverages **YOLO, PIL, and Streamlit** for seamless object detection.

## Features
- Upload an image in **JPG, JPEG, or PNG** format.
- Perform object detection using a pre-trained **YOLO** model.
- Display the detected objects with bounding boxes.
- Save and visualize the prediction results.

## Technologies Used
- **Python**
- **Streamlit** (for UI and interaction)
- **PIL** (for image processing)
- **YOLO (Ultralytics)** (for object detection)
- **Matplotlib** (for visualization)

## Installation

### Prerequisites
Ensure you have Python installed (version 3.7 or later).

### Steps
1. Clone this repository:
   ```sh
   git clone <repo-url>
   cd <repo-directory>
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate   # On macOS/Linux
   env\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Download or place your **YOLO** model (`best.pt`) in the root directory.

## Usage
1. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
2. Upload an image in **JPG, JPEG, or PNG** format.
3. Click **Predict** to perform object detection.
4. View the detected objects on the output image.

## Example Output
After uploading an image and running detection, you will see an output image with bounding boxes highlighting detected objects.



