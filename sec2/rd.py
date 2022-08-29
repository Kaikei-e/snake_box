from __future__ import print_function

import os
import tarfile
import uuid

import click
import os
import traceback


def _get_image_path(image_name, image_dir, image_suffix):
    return os.path.join(image_dir, os.extsep.join([image_name, image_suffix]))


