import os
import shutil

# os -- check files & folders in the current directory 
# shutil -- moves/copies files based on type 

path = r'/Users/bhawanasaxena/Downloads'

# create a folder for pdf files
pdf_folder = os.path.join(path, "PDFs")

# #if the folder doesn't exist, create it 
if not os.path.exists(pdf_folder):
    os.mkdir(pdf_folder)


# loop through files in the current directory and move pdf files to the pdf_files folder
# move files
for file in os.listdir(path):
    if file.endswith(".pdf"):
        shutil.move(os.path.join(path, file), os.path.join(pdf_folder, file))










