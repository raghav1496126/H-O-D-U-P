import cv2

# Load the pre-trained Haar Cascade classifier XML file
cascade_path = "D:\cascade.xml"
cascade = cv2.CascadeClassifier(cascade_path)

# Read the input image
image_path = "D:\download.jfif"
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform object detection
objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw bounding boxes around the detected objects
for (x, y, w, h) in objects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Display the image with the detected objects
cv2.imshow('Harmful Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
