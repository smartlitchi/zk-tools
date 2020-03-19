import os
from slugify import slugify
import subprocess
import re

zk_archive = os.path.expanduser("~/Documents/zettelkasten/")
# don't forget trailing slash

def get_title(zk_archive, filename):
    '''
    Retrieve the title

    zk_archive -- str, path of the zettelkasten
    filename -- str, name of the zettel
    '''
    z_path = zk_archive + filename
    with open(z_path, 'r') as z:
        z_title = z.readline().rstrip()
    return z_title

def gen_slug(filename, title):
    '''
    Generate the good filename from the old one + title

    filename -- str, old filename
    title -- str, first line of the zettel
    '''
    z_id = filename.split('.')[0]
    z_title_slug = slugify(title)
    z_new_filename = z_id + '-' + z_title_slug + '.rst'
    return z_new_filename

def git_cmd(cmd, zk_archive):
    '''
    Execute the specified git cmd

    cmd -- str, git command
    zk_archive -- str, path of the zettelkasten
    '''
    print(cmd)
    return subprocess.run(cmd.split(), cwd=zk_archive)

def get_all_zettels(zk_archive):
    '''
    Return a list of all zettels

    zk_archive -- str, path of the zettelkasten
    '''
    z_files = list()
    for z_filename in os.listdir(zk_archive):
        if '.rst' in z_filename:
            z_files.append(z_filename)
    return z_files

def get_files_to_slug(zk_archive):
    '''
    Return a list of all files that need to be slugified

    zk_archive -- str, path of the zettelkasten
    '''
    z_files = list()
    for z_filename in get_all_zettels(zk_archive):
        if len(z_filename.split('.')[0]) == 12:
            z_files.append(z_filename)
    return z_files

def gather_links(z_filename, zk_archive):
    '''
    Retrieve all the links inside a zettel

    z_filename -- str, name of the zettel
    zk_archive -- str, path of the zettelkasten
    '''
    with open(zk_archive + z_filename, 'r') as z:
        z_content = z.read()
    regex_links = "\[\[(.*?)\]\]"
    z_links = re.findall(regex_links, z_content)
    return z_links

def find_good_link(z_id, zk_archive):
    '''
    Find the path of the zettel beginning with the specified id

    z_id -- str, former unique ID of the zettel, like 198707052100
    '''
    for z_filename in get_all_zettels(zk_archive):
        if z_id in z_filename:
            return z_filename

def change_links(z_filename, zk_archive):
    '''
    Replace all the links in the zettel by good ones

    z_filename -- str, name of the zettel
    zk_archive -- str, path of the zettelkasten
    '''
    z_links = gather_links(z_filename, zk_archive)
    z_new_links = list()
    for link in z_links:
        z_new_link = find_good_link(link[:12], zk_archive)
        z_new_links.append(z_new_link)
    with open(zk_archive + z_filename, 'r') as z:
        z_content = z.read()
    for index, link in enumerate(z_links):
        z_content = z_content.replace(link, z_new_links[index])
    with open(zk_archive + z_filename, 'w') as z:
        z.write(z_content.rstrip())

def zk_slugify(zk_archive):
    '''
    Rename every zettel that needs it

    zk_archive -- str, path of the zettelkasten
    '''
    git_add = 'git add *.rst'
    git_cmd(git_add, zk_archive)
    z_files = get_files_to_slug(zk_archive)
    for z_filename in z_files:
        z_title = get_title(zk_archive, z_filename)
        z_new_filename = gen_slug(z_filename, z_title)
        git_mv = 'git mv {} {}'.format(z_filename, z_new_filename)
        git_cmd(git_mv, zk_archive)
        print('{} created'.format(z_new_filename))

def zk_change_all_links(zk_archive):
    '''
    Make all links valid links with the proper ID

    zk_archive -- str, path of the zettelkasten
    '''
    zettels = get_all_zettels(zk_archive)
    for zettel in zettels:
        change_links(zettel, zk_archive)


if __name__ == "__main__":
    zk_archive = 'tests/sources/'
    z_filename = '198707052100.rst'
    zk_change_all_links(zk_archive)
