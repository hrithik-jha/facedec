import cv2
from datetime import datetime

def detectImage(name):
    imagePath = name
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))
    now = datetime.now()
    file1 = open("log.txt", "a")
    strW = now.strftime("%d/%m/%Y %H:%M:%S")
    strW = strW + " " + "Faces: " + str(len(faces)) + "\n"
    file1.writelines(strW)
    file1.close()

    scale_percent = 60 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    imageSmol = cv2.resize(image, dim)
    cv2.imshow("Faces found", imageSmol)
    #if(len(faces) > 0):
        #cv2.imwrite("/detectedImages/" + name, image)

        #return len(faces)
    cv2.waitKey(0)