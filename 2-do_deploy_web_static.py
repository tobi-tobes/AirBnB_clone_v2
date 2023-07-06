#!/usr/bin/python3
"""
2-do_deploy_web_static.py
This module contains a Fabric script that distributes an archive
to your web servers, using the function do_deploy
"""

from fabric.api import *
import os
import datetime

env.hosts = ['54.160.124.170', '52.205.97.123']
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    This function distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False
    if not os.path.isfile(archive_path):
        return False
    if ".tgz" not in archive_path:
        return False

    result = put(archive_path, "/tmp/")
    if result.failed or result.return_code != 0:
        return False

    files = archive_path.split("/")
    file_with_ext = files[-1]
    filename = files[-1].split(".")[0]

    result = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    if result.failed or result.return_code != 0:
        return False

    result = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
                 format(file_with_ext, filename))
    if result.failed or result.return_code != 0:
        return False

    result = run("rm /tmp/{}".format(file_with_ext))
    if result.failed or result.return_code != 0:
        return False

    result = run("mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/".format(filename, filename))
    if result.failed or result.return_code != 0:
        return False

    result = run("rm -rf /data/web_static/releases/{}/web_static/".
                 format(filename))
    if result.failed or result.return_code != 0:
        return False

    result = run("rm -rf /data/web_static/current")
    if result.failed or result.return_code != 0:
        return False

    result = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                 .format(filename))
    if result.failed or result.return_code != 0:
        return False

    print("New version deployed!")
    return True
