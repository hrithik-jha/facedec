import requests
import os
import cv2


def sendImage(i):
    image_file_descriptor = open(i, 'rb')
    files = {'media': image_file_descriptor}
    url = 'localhost:5000/upload'
    requests.post(url, files=files)

    image_file_descriptor.close()


camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
 
def get_image():
    retval, im = camera.read()
    return im

for i in range(ramp_frames):
    temp = get_image()
print("Taking image...")
camera_capture = get_image()
file = "/randomImage/test_image.png"

cv2.imwrite(file, camera_capture)
sendImage("/randomImage/test_image.png")
del(camera)

