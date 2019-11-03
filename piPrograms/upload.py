import requests
import os
import cv2


def sendImage(i):
         
    image_filename = os.path.basename(i)
 
    multipart_form_data = {
        'image': (image_filename, open(i, 'rb')),
    }
 
    response = requests.post('http://iotProj.pythonanywhere.com/upload',
                             files=multipart_form_data)
 
    print(response)

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
file = "./file.png"

cv2.imwrite(file, camera_capture)
sendImage("./file.png")
del(camera)

