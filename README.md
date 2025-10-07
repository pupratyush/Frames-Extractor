# Frames-Extractor
Extract Video Frames with OpenCV
This repository contains a Python script that extracts all frames from a video file and saves each one as a separate image using the OpenCV library. The script supports any standard video format compatible with OpenCV. This tool can help with dataset creation, video analysis, and machine learning preprocessing tasks where individual frames are needed.

Features
Counts the total number of frames in a video file.

Saves each frame as a JPG image with sequential file naming for easy sorting and access.

Robustly checks for input file and output directory existence and handles errors gracefully.

Can be used as a standalone script or integrated into larger data processing pipelines.

Requirements
Python 3.x

OpenCV (opencv-python)

OS (standard Python library)

Usage
Place your video file in a known location.

Edit the input_video_path and output_frames_folder variables in the script to provide the paths to your video file and desired output directory.

Run the script:

text
python extract_video_frames.py
Extracted frames will appear as frame_00001.jpg, frame_00002.jpg, ..., in your chosen output folder.
