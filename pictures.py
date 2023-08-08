from glob import glob
import os
import shutil as xu

pictures_folder = "/home/user/Pictures"

images = glob(f"{pictures_folder}{os.sep}picture*.jpg")
print(len(images))

current_folder = os.getcwd()

current_images = glob(f"{current_folder}{os.sep}label_*.jpg")
if len(current_images) == 0:
    offset = 1
else:
    offset = max([int(x[-6:-4]) for x in current_images]) + 1

for photo in images:
    dest = current_folder + os.sep + f"label_{images.index(photo) + offset:02}.jpg"
    xu.move(photo, dest)