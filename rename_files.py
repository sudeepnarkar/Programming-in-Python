import os

def rename_files():
    files_list = os.listdir("/home/sudeep/Udacity - Programming foundations with python/Rename files/prank /prank")
   # print(files_list)
    char_delete="0123456789"

    current_dir = os.getcwd()
    print("Current working directory:"+current_dir)

    os.chdir("/home/sudeep/Udacity - Programming foundations with python/Rename files/prank /prank")
    
    for file_name in files_list:
        print("Old filename:"+file_name)
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print("New filename:"+file_name.translate(None,"0123456789"))  

    print("Printing all the file names:")

    os.chdir(current_dir)

rename_files()
 
