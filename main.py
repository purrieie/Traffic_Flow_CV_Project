import cv2
import numpy as np
import os
from google.colab.patches import cv2_imshow 

# check if the input video exists, otherwise download a sample
if not os.path.exists('traffic_video.mp4'):
    !wget -O traffic_video.mp4 https://github.com/intel-iot-devkit/sample-videos/raw/master/car-detection.mp4

# load the video file
cap = cv2.VideoCapture('traffic_video.mp4')

# initializing the background subtractor algorithm (MOG2) to detect motion
backSub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

# get video properties for the output writer
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20

# setup video writer to save the processed output
out = cv2.VideoWriter('output_processed.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

print("Processing video... please wait.")

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # apply background subtraction to get the mask
    fgMask = backSub.apply(frame)
    
    # thresholding to remove shadows (grey values) so we only get solid objects
    _, fgMask = cv2.threshold(fgMask, 250, 255, cv2.THRESH_BINARY)
    
    # dilate the image to fill gaps in the detected objects (make them solid blobs)
    kernel = np.ones((3,3), np.uint8)
    fgMask = cv2.dilate(fgMask, kernel, iterations=2)
    
    # find contours for the moving objects
    contours, _ = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    car_count = 0
    
    for contour in contours:
        # filter out noise/small objects based on area
        if cv2.contourArea(contour) > 800:
            # get the bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            
            # draw the rectangle around the vehicle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # add a label
            cv2.putText(frame, "Vehicle", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            car_count += 1
            
    # display the total count on the top left
    cv2.putText(frame, f"Moving Vehicles: {car_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # save the frame to the output file
    out.write(frame)
    
    # just a helper to see progress, skipping frames to keep it fast
    if frame_count % 10 == 0:
        # cv2_imshow(frame) 
        pass
    frame_count += 1

cap.release()
out.release()
print("Done! The video 'output_processed.mp4' has been saved.")