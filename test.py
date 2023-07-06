#!/usr/bin/python3
"""
3-deploy_web_static.py
This module contains a Fabric script that creates and distributes
an archive to your web servers, using the function deploy
"""

from fabric.api import *
import datetime
import os

def do_test():
    return_val = local("ls", capture=True)
    return_list = return_val.split("\n")
    print(return_val)
    print(return_list)
