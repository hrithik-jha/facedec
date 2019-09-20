import requests
import os
import cv2


def sendImage(i):
    image_file_descriptor = open(i, 'rb')
    files = {'url': 'done'}
    url = 'http://localhost:5000/upload'
    requests.get(url)

    image_file_descriptor.close()

def get_image():
    retval, im = camera.read()
    return im


camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
for i in range(ramp_frames):
    temp = get_image()
print("Taking image...")
camera_capture = get_image()
file = "./test_image.png"

cv2.imwrite(file, camera_capture)
sendImage("./test_image.png")
del(camera)

