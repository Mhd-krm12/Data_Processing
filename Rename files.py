import glob, os

path=r"C:\Users\...\folder"
def get_image_files(folder_path):
    img_formats = ['jpg','png', 'jpeg',"txt", "gif"] 
    files = []
    for image_file in glob.iglob(os.path.join(folder_path, "**"), recursive=True):
        files.append(image_file)
    return [x for x in files if x.split('.')[-1].lower() in img_formats]
    for i in get_image_files(path):
        os.rename(i, str(i.split(".")[:-1][0]) + "edetid" + str(i.split(".")[-1]))
        os.rename(i, i.replace("-", ""))
        
          
