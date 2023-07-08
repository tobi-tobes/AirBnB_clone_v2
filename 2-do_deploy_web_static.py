#!/usr/bin/python3
"""
2-do_deploy_web_static.py
This module contains a Fabric script that distributes an archive
to your web servers, using the function do_deploy
"""

from fabric.api import *
import os
import datetime


def do_deploy(archive_path):
    """
    This function distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False
    if not os.path.isfile(archive_path):
        return False

    filename = os.path.basename(archive_path)
    filename_no_ext = os.path.splitext(filename)[0]

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/"
            .format(filename_no_ext))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(filename, filename_no_ext))
        run("sudo rm /tmp/{}".format(filename))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data\
/web_static/releases/{}/".format(filename_no_ext, filename_no_ext))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(filename_no_ext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename_no_ext))
        print("New version deployed!")
    except Exception as e:
        return False

    return True
