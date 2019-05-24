from PIL import Image
from os import listdir

class IconPack:
    def __init__(self, path):
        self.icons = {}

        for icon_path in listdir(path):
            if not icon_path.endswith('.png'): continue
            self.icons[icon_path.replace('.png', '')] = Image.open(f'{path}/{icon_path}')

    def get(self, name):
        return self.icons[name]

icons = IconPack('icons/')
pictograms = IconPack('icons/pictograms')