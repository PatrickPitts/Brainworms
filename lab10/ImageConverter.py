# Author : John Patrick Pitts
# Date   : June 28, 2021
# File   : ImageConverter.py

from PIL import Image
from os import listdir, path
import pathlib


# img = Image.open('/lab10/Lab10Images/._cwu_logo0.jpg')
imgpath = path.realpath("Lab10Images")
savepath = path.realpath("grey_resized_logos")
for filename in listdir("Lab10Images"):
    img = Image.open(path.join(imgpath, filename))
    w, h = img.size
    img = img.convert('L')
    img = img.resize((int(w/2), int(h/2)))
    img.save(path.join(savepath, filename.split(".")[0] + "_formatted." + filename.split(".")[1]))

