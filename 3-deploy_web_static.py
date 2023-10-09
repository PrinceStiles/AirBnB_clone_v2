#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy"""
import os
from datetime import datetime
from fabric.api import *


env.hosts = ['18.233.62.245', '35.175.63.68']


def do_pack():
    """Creates archive from web_static directory"""
    local("mkdir -p versions")
    file = 'versions/web_static_{}.tgz'\
