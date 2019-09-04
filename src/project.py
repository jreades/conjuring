#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script is used to configure Conjuring.
# Depending on the parameters entered you either enter an
# interactive mode or will have conjuring prepped 
# using your specified options.

import os
import imp
import string
import shutil
import argparse
from importlib.util import find_spec

def remove_existing_folder():
    return print("Not yet implemented.")

def create_template_folder(target_dir, template_dir):
    if os.path.isdir(target_dir):
        print(f"'{args.dest}' directory already exists in {os.getcwd()}")
        exit(1)
    else:
        print(f"Creating target {target_dir}")

        # Once installed via pip may need to check
        # permissions in source and destination
        #os.makedirs(target_dir, mode=0o755)
        
        # We need to build a list of files and _then_ copy them
        # because otherwise you can do something fun (as we did)
        # like recursively copy yourself!
        shutil.copytree(template_dir, target_dir)
    return None

def find_conjuring_folder():
    f = os.path.dirname(os.path.realpath(__file__)).split(os.sep)
    return os.sep.join(f[:-2])

if __name__ == '__main__':

    HOME_PATH = find_conjuring_folder()
    print(HOME_PATH)

    parser=argparse.ArgumentParser(
        description='''
        Create a new Conjuring project with a default template.
        ''',
        epilog="""Please see https://github.com/conjuring/conjuring for more help/to report issues.""")

    # Look up how to allow --force to work instead of --force True
    parser.add_argument('--dest', type=str, default="conjuring", help='Overrides the default \'destination\' directory for creating the template')
    parser.add_argument('--force', type=bool, default=False, help='Force overwriting of existing destination directory by deleting and recreating.')

    args=parser.parse_args()

    # Create destination directory from --dest
    # - Check if directory exists
    # - Check if not empty
    # - Exit
    target_dir = os.path.join(os.getcwd(),args.dest)

    if args.force is True and os.path.isdir(target_dir):
        remove_existing_folder() 
    
    #create_template_folder(target_dir, HOME_PATH)
    exit(0)