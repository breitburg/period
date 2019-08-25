from os import mkdir
from os.path import join
from json import dumps
from hashlib import md5
from time import time
from period import __version__


def create_project(name, path, watchface=False):
    print(f'Creating new project {name} in {path}')

    mkdir(path=path)
    open(file=join(path, 'package.json'), mode='w').write(dumps({
        'name' : name,
        'author' : 'Professional programmer',
        'version' : '1.0.0',
        'uuid' : md5(f'{name}{path}{time()}'.encode('utf-8')).hexdigest(),
        'sdk_version' : __version__,
        'keywords' : [
            'period-app'
        ],
        'watchapp' : {
            'watchface' : watchface
        },
        'resources' : [

        ],
        'dependencies' : {

        }
    }))

    mkdir(path=join(path, 'src'))
    mkdir(path=join(path, 'resources'))

    open(file=join(path, 'src', '__init__.py'), mode='w').write(
        'import period\n\n@period.on_start\ndef on_load():\n\tpass\n\n@period.on_tick\ndef on_frame():\n\tperiod.draw.text(xy=(0, 10), text=\'Hello, Period\', fill=True)')
