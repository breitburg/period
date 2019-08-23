from sys import argv, path as sys_path
from os import getcwd, mkdir
from os.path import join
from json import dumps, loads
from hashlib import md5
from time import time

argv = argv[1:]

if argv[0] == '--help':
    print('There is no help!')

elif argv[0] == 'new-project':
    path = join(getcwd(), argv[1])
    print(f'Creating new project {argv[1]} in {path}')

    mkdir(path=path)
    open(file=join(path, 'package.json'), mode='w').write(dumps({
        'name': argv[1],
        'author': 'Professional programmer',
        'version': '1.0.0',
        'keywords': [
            'period-app'
        ],
        'dependencies': {},
        'period': dict(displayName=argv[1], uuid=md5(f'{argv[1]}{path}{time()}'.encode('utf-8')).hexdigest(),
                       sdkVersion='1', watchapp=dict(watchface=False), resources=dict(media=[]))
    }))

    mkdir(path=join(path, 'src'))
    mkdir(path=join(path, 'resources'))

    open(file=join(path, 'src', '__init__.py'), mode='w').write(
        'import period\n\n@period.on_start\ndef on_load():\n\tpass\n\n@period.on_tick\ndef on_frame():\n\tperiod.draw.text(xy=(0, 0), text=\'Hello, world\', fill=True)')

elif argv[0] == 'run':
    path = getcwd()
    manifest = loads(open(file=join(path, 'package.json'), mode='r').read())
    print(f'Running {manifest.get("name")}...')

    sys_path.insert(0, path)

    app = __import__('src')
    app.period.core.run_app()