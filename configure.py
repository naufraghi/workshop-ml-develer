#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse
import os
import sys
import urllib
import logging

miniconda = {
    "linux2": "http://repo.continuum.io/miniconda/Miniconda-3.7.0-Linux-x86_64.sh",
    "darwin": "http://repo.continuum.io/miniconda/Miniconda-3.7.0-MacOSX-x86_64.sh",
    "win32": "http://repo.continuum.io/miniconda/Miniconda-3.7.0-Windows-x86_64.exe",
}

def download():
    logging.info("Downloading miniconda ~16MB")
    ext = "exe" if sys.platform is "win32" else "sh"
    dest_name = "miniconda.%s" % ext
    def progress(num, size, tot):
        percent = int(num*size*100/tot)
        sys.stdout.write("\r" + dest_name + "...%d%%" % percent)
        sys.stdout.flush()
    urllib.urlretrieve(miniconda[sys.platform], dest_name, progress)
    sys.stdout.write("\n")


def main():
    parser = argparse.ArgumentParser("Configure your computer for the workshop")
    download()


if __name__ == '__main__':
    main()
