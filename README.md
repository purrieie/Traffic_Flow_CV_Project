# Smart City Traffic Flow Detector

## Overview
This project is a Computer Vision application designed to automate traffic monitoring. It uses image processing techniques to detect moving vehicles in a video feed and counts them in real-time. This falls under the domain of **Transportation & Logistics** and **Smart City Automation**.

## Problem Statement
Manual traffic counting is inefficient and prone to errors. This system aims to solve that by using a camera feed to automatically track traffic density, which can be useful for traffic signal management.

## Tech Stack
* **Language:** Python 3
* **Libraries:** * `opencv-python` (Computer Vision)
    * `numpy` (Numerical operations)

## Algorithm Used
The project relies on **Background Subtraction** to separate moving objects (cars) from the static background (road). 
1.  **Background Subtraction (MOG2):** Uses a Gaussian Mixture-based algorithm to detect motion.
2.  **Thresholding:** Removes shadows and grey noise.
3.  **Morphological Dilation:** Fills gaps in the detected objects to make them solid.
4.  **Contour Detection:** Identifies the boundaries of the vehicles to draw bounding boxes.

## File Structure
* `main.py`: The core script containing the image processing logic.
* `traffic_video.mp4`: Input video file for testing.
* `output_processed.mp4`: The final output video with detection boxes.
* `screenshots/`: Contains sample output images.
* `screen_recordings/`: Contains a video demo of the project running.

## How to Run
1.  Clone this repository.
2.  Install dependencies:
    ```bash
    pip install opencv-python numpy
    ```
3.  Run the script:
    ```bash
    python main.py
    ```
4.  The output video will be saved as `output_processed.mp4`.

## Future Improvements
* Add vehicle classification (Car vs Truck vs Bike).
* Implement lane detection.
* Connect to a live IP camera feed.
