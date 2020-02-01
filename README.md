# facedec
Face detection on image stream transmitted from a Raspberry Pi.

# piPrograms
Consists of programs supposed to run on Raspberry Pi. Can be hooked with a motion sensor and use `detect.py` to send stream of images to server.
`upload.py` is used to send the image to the server as a POST request.

# `server.py`
Used to listen to requests from Raspberry Pi. Uses `detect.py` to detect faces and save in `log.txt`.

Back-end is written using Flask. To run the server, run `python server.py`.
