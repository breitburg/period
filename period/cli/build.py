import tarfile
from os.path import join, basename
from os import mkdir, listdir


def build_project(path, name, version):
    print(f'Building {name} ({version})...')
    mkdir(join(path, 'build'))
    package_path = f'{name}-{version}.ppp'

    with tarfile.open(join(path, 'build', package_path), "w:gz") as tar :
        for file in ['src', 'resources', 'package.json']:
            tar.add(join(file))
            print(f'Compressing {name}/{file}...')

    print(f'Created package as {package_path}!')