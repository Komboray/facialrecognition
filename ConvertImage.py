####I need to get the image directory and convert the image list to something i can get
import os
from PIL import Image


 #function to convert image
folderPath = "data"


# # Open the image file using Pillow
# img = Image.open('path/to/image.jpg')
#
# # Display the image
# img.show()

# def convertImage(folderPath):
#     imgPathList = os.listdir(folderPath)
#     print(imgPathList[0])
#
# print(os.listdir(folderPath))

imageList = os.listdir(folderPath)
# print(imageList)

print(len(imageList))
if len(imageList) == 2:

    pass






