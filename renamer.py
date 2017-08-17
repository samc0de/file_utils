#! /usr/bin/python
"""Renames an image to a .png format with same name at same path."""
import os
import sys  # Use argparse instead later.
from ipdb import set_trace
import Image

def walker(real=False, dirname='', fnames=None):
  if not fnames:
    fnames = []

  fpath = os.path.realpath(dirname)
  for fname in fnames:
    if '.' in fname:  # It's a file, not a dir.
      name, _ = fname.rsplit('.', 1)
      new_fname = os.path.join(fpath, '.'.join((name, 'png')))
      img = os.path.join(fpath, fname)
      print img, '-->', new_fname
      if real:
        with Image.open(img) as image_file:
          image_file.save(new_fname)


def main():
  root_dir = sys.argv[1]
  real = len(sys.argv) > 2  # Extra arg needed to confirm. Use argparse.
  print 'Renaming for real? {0}!'.format('yes' if real else 'no')
  # print 'Renaming for real? {0}!'.format(('no', 'yes')[real])
  return os.path.walk(top=root_dir, func=walker, arg=real)


if __name__ == '__main__':
  main()
