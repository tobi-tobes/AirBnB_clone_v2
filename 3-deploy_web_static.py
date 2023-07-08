#!/usr/bin/python3
"""
3-deploy_web_static.py
This module contains a Fabric script that creates and distributes
an archive to your web servers, using the function deploy
"""

from fabric.api import *
import datetime
import os

env.hosts = ['54.160.124.170', '52.205.97.123']
env.user = "ubuntu"
env.key_filename = "/alx-system_engineering-devops/\
0x04-loops_conditions_and_parsing/0-RSA_public_key"
current = datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def do_pack():
    """
    This function generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo
    """
    local("mkdir -p versions")

    fname = "versions/web_static_{}.tgz".format(current)

    result = local("tar -cvzf {} web_static".format(fname))

    if result.succeeded:
        file_stats = os.stat(fname)
        file_size = file_stats.st_size
        print("web_static packed: {} -> {}Bytes".format(fname, file_size))
        local("chmod 664 {}".format(fname))
        return fname
    else:
        return None


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
