from PIL import Image
from os import listdir
from os.path import join


class Pictogram:
    def __init__(self, image: Image):
        assert image.size == (8, 8)
        self.image = image


class Icon:
    def __init__(self, image: Image):
        assert image.size == (16, 16)
        self.image = image


class ImagePack:
    def __init__(self, path):
        self.images = {}

        for image_path in listdir(path):
            if image_path.endswith('.png'):
                image = Image.open(join(path, image_path))
                self.images[image_path.replace('.png', '')] = Pictogram(image) if image.size == (8, 8) else Icon(image)

    def get(self, name):
        return self.images[name]


icons = ImagePack('images/')
pictograms = ImagePack('images/pictograms')