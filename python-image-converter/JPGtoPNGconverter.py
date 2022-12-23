import sys
import os
from PIL import Image

original_folder = sys.argv[1]
new_folder = sys.argv[2]


# use os module to get path
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop through old folder
# convert images to png
# save to the new folder
for filename in os.listdir(original_folder):
    image = Image.open(f'./{original_folder}/{filename}')
    image.save(f'./{new_folder}/{os.path.splitext(filename)[0]}.png', 'png')
