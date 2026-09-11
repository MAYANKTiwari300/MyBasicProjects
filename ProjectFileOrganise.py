import os
import shutil
 
 # Folder path you want to organize
Folder_path = os.getcwd()  # Current working directory
File_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.js', '.html', '.css'],
}
# create folders if they don't exist
for folder in File_types.keys():
    folder_path = os.path.join(Folder_path, folder) # this line creates the path for each folder
    if not os.path.exists(folder_path): 
        os.makedirs(folder_path)
# organize files
for file in os.listdir(Folder_path):
    file_path = os.path.join(Folder_path, file)
    
# skip folders
    if os.path.isdir(file_path):
        continue
    
    # get file extension
    #print(os.path.splitext(file))
    file_ext = os.path.splitext(file)[1].lower()
    for folder, extensions in File_types.items():   
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(Folder_path, folder, file))
            break
print("Files organized successfully!!")          
        

