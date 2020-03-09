import os
from slugify import slugify
import subprocess

zk_archive = os.path.expanduser("~/Documents/zettelkasten/")
# don't forget trailing slash

for filename in os.listdir(zk_archive):
    if '.rst' in filename and len(filename.split('.')[0]) == 12:
        full_path = zk_archive + filename
        id = filename.split('.')[0]
        with open(full_path, 'r') as z:
            title = z.readline().rstrip()
        slug = slugify(title)
        new_filename = id + '-' + slug + '.rst'
        git_cmd = 'git mv {} {}'.format(filename, new_filename)
        subprocess.run(git_cmd.split(), cwd=zk_archive)
        print('{} created'.format(new_filename))
