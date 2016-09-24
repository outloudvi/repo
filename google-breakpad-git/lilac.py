#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends = ['depot-tools-git']

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
    aur_pre_build("google-breakpad-git", do_vcs_update=False)

    for line in edit_file("PKGBUILD"):
        if not line.strip().startswith("mkdir"):
            print(line)
        else:
            print(line.replace("mkdir ", "mkdir -p "))

    vcs_update()

if __name__ == '__main__':
    single_main(build_prefix)
