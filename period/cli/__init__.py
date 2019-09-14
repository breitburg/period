from os import getcwd
from os.path import join
from json import loads
from factory.create import create_project
from factory.run import run_project
from factory.build import build_project


def main():
    from sys import argv
    argv = argv[1:]

    if len(argv) == 0 or argv[0] == '--help':
        print('Usage: period [OPTION]...\n\nOptions and arguments (and corresponding environment variables):\ncreate - Create new project\nrun - Run current project\nversion - Get current installed version number\nbuild - Build current project')
    elif argv[0] == 'create':
        name = argv[1]
        if argv[1] in ['--name', '-n']: name = argv[2]
        create_project(name=name, path=join(getcwd(), name), watchface=True if '--watchface' in argv else False)

    elif argv[0] == 'run':
        path = getcwd()
        manifest = loads(open(file=join(path, 'package.json'), mode='r').read())
        run_project(path=path, manifest=manifest)

    elif argv[0] == 'build':
        path = getcwd()
        manifest = loads(open(file=join(path, 'package.json'), mode='r').read())
        build_project(path=path, name=manifest['name'], version=manifest['version'])
