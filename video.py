import cv2
import os
import time

#this takes pics of myself and stores them in a file named data
#a file named data is created and it makes the program interactive

cam = cv2.VideoCapture(0)

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):

    # reading from frame
    ret, frame = cam.read()


    if ret:


        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imshow("frame", frame)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
        time.sleep(10)

        if currentframe>=5:
            print("We have saved only 5 pics")
            break


    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()