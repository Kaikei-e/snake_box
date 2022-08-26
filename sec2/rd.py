from __future__ import print_function

import os
import tarfile
import uuid

import click
import traceback

import linux

def _get_iamge_path(image_name, image_dir, image_suffix='tar'):
    return os.path.join(image_dir, os.extsep.join([image_name, image_suffix]))

