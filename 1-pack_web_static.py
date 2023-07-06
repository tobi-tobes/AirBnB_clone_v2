#!/usr/bin/python3
"""
1-pack_web_static.py
This module contains a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone repo, using
the function do_pack.
"""

from fabric.api import *
import datetime
import os


def do_pack():
    """
    This function generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo
    """
    local("mkdir -p versions")

    current = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    fname = "versions/web_static_{}.tgz".format(current)

    result = local("tar -cvzf {} web_static".format(fname))
    if result.succeeded and os.path.isfile(fname) and result.return_code == 0:
        return fname
    else:
        return None
