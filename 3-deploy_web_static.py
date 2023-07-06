#!/usr/bin/python3
"""
3-deploy_web_static.py
This module contains a Fabric script that creates and distributes
an archive to your web servers, using the function deploy
"""

from fabric.api import *

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """
    This function calls the do_pack() function and stores
    the path of the created archive, then calls the
    do_deploy(archive_path) function, using the new path
    of the new archive
    """
    filepath = do_pack()
    if filepath is None:
        return False
    result = do_deploy(filepath)
    return result
