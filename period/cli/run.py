from sys import path as sys_path
from PIL import Image
from os.path import join


def run_project(manifest, path):
    print(f'Running {manifest.get("name")}...')

    sys_path.insert(0, path)

    app = __import__('src')

    for resource in manifest['resources'] :
        if resource['type'] == 'bitmap_image' :
            app.period.resources.media[resource['name']] = Image.open(join(path, 'resources', resource['file']))

    app.period.core.run_app()