#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""example.py - example Python script wrapped by ../example via pythonize."""

import os
import shutil
import subprocess
import sys
from zipfile import ZipFile

from colorama import init, Fore, Style
import requests


def main():
    """Prints info on current Python environment to verify script worked."""

    print('\n{}example.py -> running{}'
          .format(Fore.CYAN + Style.BRIGHT, Style.RESET_ALL))
    print('\nFile path:\n{}{}{}'.format(Style.BRIGHT,
                                        os.path.realpath(__file__),
                                        Style.NORMAL))
    print('\nPython version:\n{}{}{}'.format(Style.BRIGHT, sys.version,
                                             Style.NORMAL))
    print('\nCurrent value of PATH environment variable:')
    for i in os.environ['PATH'].split(':'):
        print('    {}{}{}'.format(Style.BRIGHT, i, Style.NORMAL))
    print('\n')
    print("{}Downloading Phillip John's text adventure from github\n{}⟨⟨"
          "https://github.com/phillipjohnson/text-adventure-tut⟩⟩"
          .format(Style.BRIGHT, Style.NORMAL))
    print()
    # Just a trivial example program, so no attempts at error-detection.
    # Basically, we're freeballing.  ^.^
    try:
        zipped = 'text-adventure-tut.zip'
        extract_dir = zipped.rstrip('.zip') + '-master'
        with open(zipped, 'wb') as f:
            r = requests.get('https://github.com/phillipjohnson/text-adventure'
                             '-tut/archive/master.zip')
            for b in r.iter_content(1024):
                f.write(b)
        with ZipFile(zipped, 'r') as z:
            z.extractall()
        os.chdir(extract_dir)
        with open('.example.py.stderr', 'wb') as stderr:
            print('\n{1}{0}\nBEGIN TEXT ADVENTURE\n{0}{2}{3}'
                  .format('=' * 79, Style.BRIGHT, Style.NORMAL, Fore.CYAN))
            p = subprocess.Popen(['python', 'adventuretutorial/game.py'],
                                 stderr=stderr)
            p.communicate()
    except KeyboardInterrupt:
        print('\n\n{}Quitting at user request'.format(Fore.RESET))
        sys.exit()
    finally:
        if not os.path.exists(zipped):
            os.chdir('..')
        if os.path.exists(zipped):
            os.remove(zipped)
        if os.path.exists('.example.py.stderr'):
            os.remove('.example.py.stderr')
        if os.path.exists(extract_dir):
            shutil.rmtree(extract_dir)


if __name__ == '__main__':
    init()
    main()
