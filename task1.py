import cv2
import numpy as np

data_images = []
def RorateImage(data_images):
    for i in range(0,len(data_images)):
        image = data_images[i]
        row,col = image.shape[:2]
        M = cv2.getRotationMatrix2D((col/2,row/2),180,1) 
        dst = cv2.warpAffine(image,M,(col,row))
        data_images[i] = dst
    return data_images

def createVideo(data_images):
    video = cv2.VideoWriter('Output.avi',cv2.VideoWriter_fourcc(*'DIVX'), 3, (np.shape(data_images)[1],np.shape(data_images)[2]))
    for i in range(0,len(data_images)):
        video.write(data_images[i])
    video.release()
    print("Output.avi Generated")

def VideotoImage(filename):
    capture = cv2.VideoCapture(filename)
    i=0
    while(capture.isOpened()):
        r, frame = capture.read()
        if(r != False):
            data_images.append(frame)
            i = i+1
        else:
            break
    return data_images

fileName = input("Enter File name with path: ")
frames = VideotoImage(fileName)
rotate_photoes = RorateImage(frames)
createVideo(rotate_photoes)

cv2.destroyAllWindows()