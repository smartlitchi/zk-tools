import os
from slugify import slugify
import subprocess

zk_archive = os.path.expanduser("~/Documents/zettelkasten/")
# don't forget trailing slash

def get_title(zk_archive, filename):
    z_path = zk_archive + filename
    with open(z_path, 'r') as z:
        z_title = z.readline().rstrip()
    return z_title

def gen_slug(filename, title):
    z_id = filename.split('.')[0]
    z_title_slug = slugify(title)
    z_new_filename = z_id + '-' + z_title_slug + '.rst'
    return z_new_filename

def zk_slugify(zk_archive):
    for z_filename in os.listdir(zk_archive):
        if '.rst' in z_filename and len(z_filename.split('.')[0]) == 12:
            z_title = get_title(zk_archive, z_filename)
            z_new_filename = gen_slug(z_filename, z_title)
            git_cmd = 'git mv {} {}'.format(z_filename, z_new_filename)
            subprocess.run(git_cmd.split(), cwd=zk_archive)
            print('{} created'.format(z_new_filename))
