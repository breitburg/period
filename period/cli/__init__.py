from os import getcwd
from os.path import join
from json import loads
from period import __version__
from period.cli.create import create_project
from period.cli.run import run_project


def main():
    from sys import argv
    argv = argv[1:]

    if len(argv) == 0 or argv[0] == '--help':
        print('Usage: period [OPTION]...\n\nOptions and arguments (and corresponding environment variables):\ncreate - Create new project\nrun - Run current project\nversion - Get current installed version number')

    elif argv[0] == 'version':
        print(f'Installed version: Period SDK {__version__}')

    elif argv[0] == 'create':
        name = argv[1]
        if argv[1] in ['--name', '-n']: name = argv[2]
        create_project(name=name, path=join(getcwd(), name), watchface=True if '--watchface' in argv else False)

    elif argv[0] == 'run':
        path = getcwd()
        manifest = loads(open(file=join(path, 'package.json'), mode='r').read())
        run_project(path=path, manifest=manifest)

