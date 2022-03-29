#EN: Get all Image path Size in folder.
#TR: Bu kod yardımıyla bir klasör belirleyip içinde yürüyüp ve bütün resimlerin yolunu ve boyutunu yazdırabiliriz.
#AR: يقوم هذا الكود بالتنقل داخل المجلد الذي حددناه وجمع كل الصور وطباعة مسار وأبعاد الصور.

import glob
import os
import cv2

def get_image_files(folder_path):
    img_formats = ['bmp','jpg', 'jpeg', 'png', 'tif',  'tiff',  'dng', 'webp', 'mpo'] 
    files = []
    for image_file in glob.iglob(os.path.join(folder_path, "**"), recursive=True):
        files.append(image_file)
    return [x for x in files if x.split('.')[-1].lower() in img_formats]
for file in get_image_files(r"C:\Users\MyComputer\Desktop\Test_folder"):   #Enter your folder path       
    print(file)
    resim = cv2.imread(file)
    resim = resim[...,::-1]
    (h, w) = resim.shape[:2]
    print(h,w)
    
    
