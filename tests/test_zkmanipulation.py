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

def test_git_cmd():
    cmd = 'git status'
    git_process = zkmanipulation.git_cmd(cmd, zk_archive)
    assert git_process.returncode == 0

def test_get_files_to_slug():
    z_files = zkmanipulation.get_files_to_slug(zk_archive)
    assert len(z_files) == 1
    assert z_files[-1] == z_filename

def test_zk_slugify():
    zkmanipulation.zk_slugify(zk_archive)
    z_list = os.listdir(zk_archive)
    assert '198707052100-hello-world.rst' in z_list
