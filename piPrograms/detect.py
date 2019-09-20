'''

INSERT CODE TO DETECT MOTION

'''
import os
'''
IF MOTION DETECTED
    CALL(TAKE_IMAGE())
    CALL(SEND_IMAGE())
'''

def imgName():
        files = os.listdir('./img/')
        return len(files) + 1

print(imgName())