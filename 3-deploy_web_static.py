#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.

import os
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ["104.196.168.90", "35.196.46.172"]

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    archive_path = "versions/{}".format(file_name)

    if not os.path.exists("versions"):
        os.mkdir("versions")

    local_command = "tar -czvf {} web_static".format(archive_path)
    result = local(local_command)

    if result.failed:
        return None
    else:
        return archive_path

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

    file_name = os.path.basename(archive_path)
    remote_path = "/tmp/{}".format(file_name)

    if put(archive_path, remote_path).failed:
        return False

    release_dir = "/data/web_static/releases/"
    run("mkdir -p {}".format(release_dir))
    
    name = file_name.replace('.tgz', '')

    with cd(release_dir):
        run("tar -xzf {} -C {}/{}".format(remote_path, release_dir, name))
        run("rm {}".format(remote_path))
        run("mv {0}/{1}/web_static/* {0}/{1}/".format(release_dir, name))
        run("rm -rf {0}/{1}/web_static".format(release_dir, name))

    current_link = "/data/web_static/current"
    run("rm -rf {}".format(current_link))
    run("ln -s {} {}/".format(release_dir + name, current_link))

    return True
