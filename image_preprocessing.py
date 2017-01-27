
import pandas as pd
import numpy as np
import urllib
from PIL import Image
import os
# Image pre-processing helper functions


def get_image(image_links):
    count = 1
    for i in image_links:
        urllib.urlretrieve(i, '/Users/smoot/Desktop/category_training/TRAIN_DIR/m_dress/img_%d.jpg' % count)
        count += 1
        
def get_np_array(image_links, dest):
    count = 1
    for i in image_links:
        try:
            resp = requests.get(i)
            image = np.array(Image.open(StringIO(resp.content)))
            np.save(os.path.join(dest, 'img_%d' % count), image)
            count += 1
        except:
            pass

def resize_image(img_loc, size):
    list_dir = os.listdir(img_loc)
    list_dir = list_dir[1:]
    count = 1
    for i in list_dir:
        img = Image.open(os.path.join(img_loc, i))
        img = img.resize((size, size), Image.BILINEAR)
        img.save(os.path.join(img_loc, 'img_%d.jpg' % count), "JPEG", quality=90)
        count += 1