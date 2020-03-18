import zkmanipulation
import os

zk_archive = os.path.expanduser("~/Projects/zettelkasten/tests/sources/")
z_filename = '198707052100.rst'

def test_get_title():
    z_title = zkmanipulation.get_title(zk_archive, z_filename)
    assert z_title == 'Hello world !'

def test_gen_slug():
    z_title = zkmanipulation.get_title(zk_archive, z_filename)
    z_slug = zkmanipulation.gen_slug(z_filename, z_title)
    assert z_slug == '198707052100-hello-world.rst'
