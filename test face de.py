import cv2, os
import numpy as np, json
from tensorflow.keras.applications import MobileNet, resnet50
from tensorflow.keras.models import Model
from matplotlib import pyplot as plt
from scipy import spatial
import glob
from keras_vggface import VGGFace 
from tensorflow.keras.preprocessing import image
from keras_vggface import utils




yüz_içermeyen_resimler_sayacı=0
geçersiz_resimler_sayacı=0

# klasör içinde gezmek
def get_image_files(folder_path):
    img_formats = ['jpg','png', 'jpeg'] 
    files = []
    for image_file in glob.iglob(os.path.join(folder_path, "**"), recursive=True):
        files.append(image_file)
    return [x for x in files if x.split('.')[-1].lower() in img_formats]




#Yüz detect için model
protoPath = "deploy.prototxt.txt"
modelPath = "res10_300x300_ssd_iter_140000.caffemodel"
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)



#image to matrix
for file in get_image_files(r"C:\Users\Mhd Krm\Desktop\deneme"):
    count = 0
    print(file)
    resim = cv2.imread(file)
    try:
        resim_rgb = resim[...,::-1]  # BGR to RGB
        (h, w) = resim_rgb.shape[:2]
        imageBlob = cv2.dnn.blobFromImage(
            cv2.resize(resim_rgb, (300, 300)), 1.0, (300, 300),
            (104.0, 177.0, 123.0), swapRB=False, crop=False)

        detector.setInput(imageBlob)  #resmi modele viriyoruz.
        detections = detector.forward()
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            # benzerlik oranı     

            if confidence > 0.5:
                count += 1
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                #resim2=cv2.rectangle(resim, (startX, startY), (endX, endY), (0, 255, 0),1) #yüzü böl kare çiz
                ss = resim[startY:endY, startX:endX]    #yüzü böl kes
                ss = ss[:, :, [2, 1, 0]]    # RGB to BGR
                plt.imshow(ss)
                plt.show(block=False)
                plt.pause(1)
                plt.close() 
                file_name=os.path.split(file)[-1].split('.')[-2]
                koor = detections [0, 0, i, 3:7]

                
                selecteed_folder=(f"C:/Users/Mhd Krm/Desktop/deneme/{file_name}")  
                fi= open(selecteed_folder+'.txt' , "a")
                fi.write("0 "+str(koor[1]) + " " + str(koor[2])  + " " + str(koor[3]) + " " + str(koor[0]) + "\n")
                fi.close()
        print("Yüz sayısı: " + str(count))


                
        if count == 0:
            print(str(file))
            
            yüz_içermeyen_resimler_sayacı+=1
            print("  yüz içermeyen bir resim,silinecektir *******")
            os.remove(file)

    except:
        
        geçersiz_resimler_sayacı=+1
        print("  geçersiz resim,silinecektir---------------")
        os.remove(file)

     
print("\n")                
print(str(yüz_içermeyen_resimler_sayacı)+"  yüz içremeyen resim,silinmiştir.")
print(str(geçersiz_resimler_sayacı)+"  geçersiz resim,silinmiştir.")

            


           
           


            
        



