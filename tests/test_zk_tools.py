import zk_tools
import os

zk_archive = os.path.expanduser("~/Projects/zk_tools/tests/sources/")
z_filename = '198707052100.rst'

def test_get_title():
    z_title = zk_tools.get_title(zk_archive, z_filename)
    assert z_title == 'Hello world !'

def test_gen_slug():
    z_title = zk_tools.get_title(zk_archive, z_filename)
    z_slug = zk_tools.gen_slug(z_filename, z_title)
    assert z_slug == '198707052100-hello-world.rst'

def test_git_cmd():
    cmd = 'git status'
    git_process = zk_tools.git_cmd(cmd, zk_archive)
    assert git_process.returncode == 0

def test_get_all_zettels():
    z_files = zk_tools.get_all_zettels(zk_archive)
    assert len(z_files) == 5
    assert z_files == ['198707052100.rst', '202003191044-coronavirus-is-live.rst', '202008200807-good-link.rst', '202004301451-name-is-not-good.rst', '199110141020-happy-birthday.rst']

def test_zk_slugify():
    zk_tools.zk_slugify(zk_archive)
    z_list = os.listdir(zk_archive)
    assert '198707052100-hello-world.rst' in z_list
    assert '202004301451-this-is-the-good-title.rst' in z_list

def test_find_filename():
    z_id = z_filename.split('.')[0]
    z_link = zk_tools.find_filename(z_id, zk_archive)
    assert z_link == '198707052100-hello-world.rst'

def test_gather_links():
    z_id = z_filename.split('.')[0]
    z_slugified = zk_tools.find_filename(z_id, zk_archive)
    z_links = zk_tools.gather_links(z_slugified, zk_archive)
    assert len(z_links) == 4
    assert z_links == ['202003191044.rst', '199110141020.rst', '202004301451-name-is-not-good.rst', '202008200807-good-link.rst']
    assert 'sources/202003191513.pdf' not in z_links

def test_change_links():
    z_id = z_filename.split('.')[0]
    z_slugified = zk_tools.find_filename(z_id, zk_archive)
    zk_tools.change_links(z_slugified, zk_archive)
    z_lines = ['Hello world !', '=============', '', '[[202003191044-coronavirus-is-live.rst]]', '[[199110141020-happy-birthday.rst]]', '[[sources/202003191513.pdf]]', '[[ -z $test ]]', '[[202004301451-this-is-the-good-title.rst]] text between links [[202008200807-good-link.rst]]']
    with open(zk_archive + z_slugified, 'r') as z:
        z_content = z.readlines()
    for index, line in enumerate(z_content):
        assert line.rstrip() == z_lines[index]

def test_zk_change_all_links():
    zk_tools.zk_change_all_links(zk_archive)
    z_slugified = '202003191044-coronavirus-is-live.rst'
    z_lines = ['Coronavirus is live', '===================', '', '[[199110141020-happy-birthday.rst]]']
    with open(zk_archive + z_slugified, 'r') as z:
        z_content = z.readlines()
    for index, line in enumerate(z_content):
        assert line.rstrip() == z_lines[index]

def test_find_orphans():
    zk_tools.zk_change_all_links(zk_archive)
    orphans = zk_tools.zk_find_orphans(zk_archive)
    assert len(orphans) == 1
    assert orphans == ['198707052100-hello-world.rst']
