import glob, os 




#Get all Image path in folder.
def get_image_files(folder_path):
    img_formats = ['jpg','png', 'jpeg'] 
    files = []
    for image_file in glob.iglob(os.path.join(folder_path, "**"), recursive=True):
        files.append(image_file)
    return [x for x in files if x.split('.')[-1].lower() in img_formats]


count = 0

path = r"C:\Users\foren\Desktop\WiderVeriSeti\WIDER_val\images"
labels_path = r"C:\Users\foren\Desktop\WiderVeriSeti\WIDER_val\labels"
for i in get_image_files(path):
    image_name = os.path.basename(os.path.splitext(i)[0])
    #print(i)
    #print(image_name)
    
    #print(str(image_name))
    
    file_bool = os.path.exists(os.path.join(labels_path, image_name + ".txt"))
 
    if file_bool:
        pass
        #
    else:
        os.remove(i)
        print(os.path.join(labels_path, image_name + ".txt"))
        count = count + 1
print(count)