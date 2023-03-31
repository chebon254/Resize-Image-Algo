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
        # get the dimensions of the image
        width, height = img.size
        # calculate the coordinates to crop the image
        left = (width - height) / 2
        top = 0
        right = (width + height) / 2
        bottom = height
        # crop the image to a square shape with a height and width of 1080 pixels
        img = img.crop((left, top, right, bottom)).resize((1080, 1080))
        # save the cropped image with the same filename in a new folder
        img.save(os.path.join('cropped', filename))
