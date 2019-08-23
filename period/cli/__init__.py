from sys import argv, path as sys_path
from os import getcwd, mkdir
from os.path import join
from json import dumps, loads
from hashlib import md5
from time import time
from PIL import Image
from period import __version__

argv = argv[1:]

if len(argv) == 0 or argv[0] == '--help':
    print('Usage: period [OPTION]...\n\nOptions and arguments (and corresponding environment variables):\ncreate - Create new project\nrun - Run current project\nversion - Get current installed version number')

elif argv[0] == 'version':
    print(f'Installed version: Period SDK {__version__}')

elif argv[0] == 'create':
    name = argv[1]
    if argv[1] in ['--name', '-n']: name = argv[2]

    path = join(getcwd(), name)
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
            'watchface' : True if '--watchface' in argv else False
        },
        'resources' : [

        ],
        'dependencies' : {

        }
    }))

    mkdir(path=join(path, 'src'))
    mkdir(path=join(path, 'resources'))

    open(file=join(path, 'src', '__init__.py'), mode='w').write('import period\n\n@period.on_start\ndef on_load():\n\tpass\n\n@period.on_tick\ndef on_frame():\n\tperiod.draw.text(xy=(0, 0), text=\'Hello, world\', fill=True)')

elif argv[0] == 'run':
    path = getcwd()
    manifest = loads(open(file=join(path, 'package.json'), mode='r').read())
    print(f'Running {manifest.get("name")}...')

    sys_path.insert(0, path)

    app = __import__('src')

    for resource in manifest['resources']:
        if resource['type'] == 'bitmap_image':
            app.period.resources.media[resource['name']] = Image.open(join(path, 'resources', resource['file']))

    app.period.core.run_app()
