#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script is used to configure Conjuring for a deployment.
# Depending on the parameters entered you will either enter an
# interactive mode or will have conjuring prepped for deployment
# using your specified options.

import os
import csv 
import string
import secrets
import argparse

# Where to find Conjuring's custom directory.
custom_dir = 'custom'

parser=argparse.ArgumentParser(
    description='''
    This script is used to configure Conjuring for a deployment.
    Depending on the parameters entered you will either enter an
    interactive mode or will have conjuring prepped for deployment
    using your specified options.
    ''',
    epilog="""Please see https://github.com/conjuring/conjuring for more help/to report issues.""")
parser.add_argument('--num', type=int, default=20, help='The number of users to create (defaults to 20).')

args=parser.parse_args()

print(args.num)

exit()