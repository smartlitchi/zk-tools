import os
import datetime
import pathlib

zk_archive = os.path.expanduser("~/Documents/zettelkasten/")

creation_date = datetime.datetime.now()
z_id = creation_date.strftime('%Y%m%d%H%M')
z_filename = z_id + '.rst'

z_fullpath = zk_archive + z_filename
pathlib.Path(z_fullpath).touch()
print('{} created'.format(z_fullpath))
