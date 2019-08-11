"""Tasks for management of this project."""

from __future__ import print_function

import os
import shutil
import sys

from pathlib import (
    Path)

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD_DIR = os.path.join(HERE, 'build')
JS_DIR = os.path.join(HERE, 'javascript')
IMG_DIR = os.path.join(HERE, 'img')
BUILD_IMG_DIR = os.path.join(BUILD_DIR,'img')
FAVICON_PATH = os.path.join(IMG_DIR, 'favicon.ico')


def _mkdir_if_not_present(dirname):
    """Utility to make a directory if it does not already exist."""
    Path(dirname).mkdir(parents=True, exist_ok=True)


def _rmdir_if_present(dirname):
    """Delete a directory if it is present."""
    try:
        shutil.rmtree(dirname)
    except FileNotFoundError:
        pass


def _iter_paths(directory, glob_pattern):
    """Iterate over files within a directory that match a pattern."""
    for path in Path(directory).glob(glob_pattern):
        yield path


def build():
    """Compile the site into the build directory."""
    clean()
    _mkdir_if_not_present(BUILD_DIR)

    # compile html pages
    for src_file in _iter_paths(JS_DIR, '*'):
        dest_path = os.path.join(BUILD_DIR, src_file.name)
        src_path = os.path.join(JS_DIR, src_file.name)
        shutil.copy(src_path, dest_path)
    print('[*] Compiled pages into', BUILD_DIR)

    shutil.copytree(IMG_DIR, BUILD_IMG_DIR)
    print('[*] Copied img assets into', BUILD_IMG_DIR)


def clean():
    """Remove the build directory."""
    _rmdir_if_present(BUILD_DIR)
    print('[*] Cleaning done')


def serve():
    """Run a livereload server on port 5000."""
    from livereload import Server

    watch_patterns = [
        os.path.join(JS_DIR, '**', '*'),
        os.path.join(IMG_DIR, '**', '*')
    ]

    server = Server()
    build()
    for pattern in watch_patterns:
        server.watch(pattern, build)

    print('[*] Running livereload server on port 5000')
    server.serve(root=BUILD_DIR, port=5000, host='127.0.0.1')


TASKS = {
    'build': build,
    'clean': clean,
    'serve': serve
}
TASK_KEYS = list(sorted(TASKS.keys()))


if __name__ == '__main__':
    sys.argv.pop(0)
    if len(sys.argv) != 1:
        print('Must specify task to perform', file=sys.stderr)
        sys.exit(1)

    task = sys.argv.pop()
    if task not in TASK_KEYS:
        print('Specified task must be one of:', ', '.join(TASK_KEYS))
        sys.exit(1)

    task_func = TASKS[task]
    task_func()