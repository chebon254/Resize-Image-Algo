from PIL import Image
import os

# set the path to the folder containing the images
folder_path = 'images'

# loop through all the files in the folder
for filename in os.listdir(folder_path):
    # check if the file is an image (jpg, png, etc.)
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # open the image using PIL
        img = Image.open(os.path.join(folder_path, filename))
        # resize the image to a width of 1920 and a height of 1080
        img = img.resize((1920, 1080))
        # save the resized image with the same filename in a new folder
        img.save(os.path.join('resized', filename))
