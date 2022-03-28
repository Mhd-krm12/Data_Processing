import cv2
import os

os.chdir(r"C:\myComputer\Desktop\Test_folder")                                                        #Enter your folder path                                                               
for paths,folders,files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(('bmp','jpg', 'jpeg', 'png', 'tif',  'tiff',  'dng', 'webp', 'mpo')):
                image_path=((os.path.join(paths,file)))
                img=cv2.imread(image_path)
                print("Image path:  "+str(image_path)+"\n"+"Image Size: "+str(img.shape)+"\n")
