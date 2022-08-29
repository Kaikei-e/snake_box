from __future__ import print_function

# import linux
import tarfile
import uuid

import click
import traceback
import os
import stat


def _get_image_name(image_name, image_dir, image_suffix='tar'):
    return os.path.join(image_dir, os.extsep.join([image_name, image_suffix]))


def _get_container_path(container_id, container_dir, *subdir_names):
    return os.path.join(container_dir, container_id, *subdir_names)
