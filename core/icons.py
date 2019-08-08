from PIL import Image
from os import listdir
from os.path import join


class ImagePack:
    def __init__(self, path):
        self.images = {}

        for image_path in listdir(path):
            if image_path.endswith('.png'):
                self.images[image_path.replace('.png', '')] = Image.open(join(path, image_path))

    def get(self, name):
        return self.images[name]


icons = ImagePack('assets/icons')
pictograms = ImagePack('assets/pictograms')