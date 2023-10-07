#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.

import os.path
from fabric.api import env, put, run

env.hosts = ["54.87.172.124", "54.84.66.24"]

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False

    # Extract the filename and name without extension
    file_name = os.path.basename(archive_path)
    name = os.path.splitext(file_name)[0]

    # Upload the archive to /tmp
    put(archive_path, "/tmp/{}".format(file_name))

    # Create the necessary directory structure
    run("mkdir -p /data/web_static/releases/{}/".format(name))

    # Unpack the archive
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, name))

    # Delete the uploaded archive
    run("rm /tmp/{}".format(file_name))

    # Move contents to the proper location
    run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name))

    # Remove the old symlink
    run("rm -rf /data/web_static/current")

    # Create a new symlink
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name))

    print("New version deployed!")
    return True
