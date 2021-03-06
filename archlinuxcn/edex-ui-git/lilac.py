#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build(maintainers=['GitSquared'])
  for l in edit_file('PKGBUILD'):
    print(l)
    if l.startswith('pkgrel'):
      print('epoch=1')

if __name__ == '__main__':
  single_main(build_prefix)
