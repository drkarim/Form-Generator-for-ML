
import numpy as np

def crop_image(img):
    arr = np.array(img)
    fromtop = []
    for i in range(arr.shape[0]):
        if np.mean(arr[i]) !=255:
            fromtop.append(i)     
    fromleft = []
    for i in range(arr.shape[1]):
        if np.mean(arr.T[i]) !=255:
            fromleft.append(i)
    top = fromtop[0]
    bottom = fromtop[-1]
    left = fromleft[0]
    right = fromleft[-1]
    img = img.crop((left,top,right,bottom))
    return img