# Traffic_Flow_CV_Project
Smart City Traffic Flow Detector
Project Description
An automated computer vision system designed to monitor traffic density for smart city applications. The system processes video feeds to detect moving vehicles, ignoring static backgrounds and environmental noise.

Domain
Transportation & Logistics / Smart Cities

Technology Stack
Language: Python

Libraries: OpenCV, NumPy

Algorithm: Gaussian Mixture-based Background/Foreground Segmentation (MOG2)

Methodology
Input: Video stream of a traffic junction.

Preprocessing: Background subtraction is applied to isolate moving pixels from the static road.

Noise Removal: Thresholding and Morphological Dilation are used to remove shadows and fill gaps in object detection.

Detection: Contours are extracted from the mask. Bounding rectangles are drawn on valid objects (area > 800px).

How to Run
Open the project in Google Colab or a local Python environment.

Ensure traffic_video.mp4 is in the directory.

Run main.py.
