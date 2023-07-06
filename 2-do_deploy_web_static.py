#!/usr/bin/python3
"""
2-do_deploy_web_static.py
This module contains a Fabric script that distributes an archive
to your web servers, using the function do_deploy
"""

from fabric.api import *
import os

env.hosts = ['54.160.124.170', '52.205.97.123']
env.user = "ubuntu"
env.key_filename = "/alx-system_engineering-devops/\
0x04-loops_conditions_and_parsing/0-RSA_public_key"


def do_deploy(archive_path):
    """
    This function distributes an archive to your web servers
    """
    if not os.path.isfile(archive_path):
        return False
    if ".tgz" not in archive_path:
        return False
    if not put(archive_path, "/tmp/").succeeded:
        return False
    files = archive_path.split("/")
    file_with_ext = files[-1]
    filename = files[-1].split(".")[0]
    if not run("mkdir -p /data/web_static/releases/{}/".format(filename))\
       .succeeded:
        return False
    if not run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
               format(file_with_ext, filename)).succeeded:
        return False
    if not run("rm /tmp/{}".format(file_with_ext)).succeeded:
        return False
    if not run("mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/".format(filename, filename)).succeeded:
        return False
    if not run("rm -rf /data/web_static/releases/{}/web_static/".
               format(filename)).succeeded:
        return False
    if not run("rm -rf /data/web_static/current").succeeded:
        return False
    if not run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
               format(filename)).succeeded:
        return False
    print("New version deployed!")
    return True
