#! /usr/bin/python
""" For now this just renames images to .png filename.

This is very dumb as it simply copies binary data, instead of actually
converting formats/encodings. Update if it doesn't work and also make it more
generic in nature, not just png renamer.
"""
import os
import sys  # Use argparse instead later.
from ipdb import set_trace

def walker(real=False, dirname='', fnames=None):
  if not fnames:
    fnames = []

  print 'Renaming files:'
  # curdir = dirname

  fpath = os.path.realpath(dirname)
  for fname in fnames:
    if '.' in fname:  # It's a file, not a dir.
      name, ext = fname.rsplit('.', 1)
      new_fname = os.path.join(fpath, '.'.join((name, 'png')))
      img = os.path.join(fpath, fname)
      print img, '-->', new_fname
      if real:
        with open(img, 'rb') as source, open(new_fname, 'wb') as dest:
          dest.write(source.read())


def main():
  root_dir = sys.argv[1]
  real = len(sys.argv) > 2  # Extra arg needed to confirm. Use argparse.
  print 'Renaming for real? {0}!'.format('yes' if real else 'no')
  # print 'Renaming for real? {0}!'.format(('no', 'yes')[real])
  return os.path.walk(top=root_dir, func=walker, arg=real)


if __name__ == '__main__':
  main()
