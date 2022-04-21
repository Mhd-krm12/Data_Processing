#EN:This code visits a selected folder and changes the first letter of each line.
#TR:Bu kod belirli bir klasöre girer ve her satırın ilk harfini değiştirir.
#AR:يعمل هذا الكود على الدخل إلى مجلد معين وتغير أول حرف من كل سطر 

import os

os.chdir(r"C:\Users\........\folder") #Enter your folder path                                                               
for paths,folders,files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith("txt"):
                reading_file = open(file,"r")
                new_str = ""
                for line in reading_file:
                    new_line=(line[0].replace(line[0],'0')+line[1:])
                    new_str += new_line
                writing_file = open(file,"w")
                writing_file.write(new_str)
                writing_file.close()
                
                
