import cv2
import math
import os, os.path
import shutil
def cvfunc(filename):
  src = cv2.imread(filename)
  split = filename.split('.')
  re_path = os.getcwd()+'/'+'cropped_'+split[0]+'/'
  if os.path.isdir(re_path):
      shutil.rmtree(re_path, ignore_errors=True)
  os.mkdir(re_path)
  height, width = src.shape[:2]
  reheight = width*(1080.0/1920.0)/6.0
  reheight = int(reheight)
  dh = int(math.ceil(height / reheight))
  n = int(len(str(dh)))
  delay=0
  preendpoint=0
  binary=cv2.Canny(src,100,200)
  for i in range(0,dh-1):
      y = preendpoint
      for jj in range(0,reheight):
          temp_img = binary[y+reheight+jj:y+reheight+jj+1,0:width]
          hist = cv2.calcHist([temp_img],[0],None,[256],[0,256])
          #print(hist)
          #cv2.imshow('temp_img', temp_img)
          #cv2.waitKey(0)
          if hist[255]==0:
              delay = jj
              break
      crop_img = src[preendpoint:y+reheight+delay, 0:width]
      preendpoint=y+reheight+delay
      string = re_path+"crop_"+str(i).zfill(n)+".png"
      cv2.imwrite(string, crop_img)
  if preendpoint>(height-5):
      return re_path
  crop_img = src[preendpoint:height, 0:width]
  string = re_path+"crop_"+str(i+1).zfill(n)+".png"
  cv2.imwrite(string, crop_img)
  return re_path

def imlist(imageFile):
    impath = cvfunc(imageFile)
    valid_image_extensions = [".png"]
    valid_image_extensions = [item.lower() for item in valid_image_extensions]
    image_path_list = []
    dirlist = os.listdir(impath)
    for file in dirlist:
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_image_extensions:
            continue
        image_path_list.insert(len(image_path_list),os.path.join(impath,file))
    image_path_list.sort()
    return image_path_list
