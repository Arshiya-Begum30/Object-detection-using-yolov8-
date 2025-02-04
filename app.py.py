import streamlit as st
from PIL import Image
import torch
from ultralytics import YOLO
import os
import matplotlib.pyplot as plt
import glob

# Set the model path
model_path = 'best.pt'
source_dir = 'temp/'  # Temporary directory for uploaded images

# Create the source directory if it does not exist
if not os.path.exists(source_dir):
    os.makedirs(source_dir)

# Load the model
model = YOLO(model_path)

# Streamlit UI
st.title('YOLO Object Detection')
st.write('Upload an image to detect objects')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Predict'):
        # Save the uploaded file to source directory
        img_path = os.path.join(source_dir, uploaded_file.name)
        with open(img_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Run YOLO prediction
        results = model(image)
        
        # Process the results
        for result in results:
            boxes = result.boxes
            masks = result.masks
            keypoints = result.keypoints
            probs = result.probs
            obb = result.obb
            
            # Show and save the result image
            
            result.save(filename="result.jpg")
            
            # Return the processed image

        # Display the predicted images
        st.write('Predictions:')
        result_image = 'result.jpg'

        st.image(result_image, caption='output Image', use_column_width=True)
 