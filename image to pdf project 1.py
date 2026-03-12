from PIL import Image

import os

print("Image to pdf conversion")

folder_path=input("Enter folder path: ")  #input a folder name

files=os.listdir(folder_path)  #getting a list of files from a folder

n=len(files)

for i in range(n-1):         #buuble sort to sort images from a file
 for j in range(n-1-i): 
    if files[j]>files[j+1]:
      files[j]=files[j+1]
    files[j]=files[j+1]
img=[]                       #converting that sorted image into a form of a list
for file in files:
  if file.lower().endswith((".png",".jpeg",".jpng")):
   path=os.path.join(folder_path,file) 
   image=Image.open(path).convert('RGB')
   img.append(image)
   if img:
     img[0].save("enter a folder path to store pdf file", save_all=True , append_images=img[1:])
     print("pdf created successfully")
   else:

     print("no image found! pdf is not created")
