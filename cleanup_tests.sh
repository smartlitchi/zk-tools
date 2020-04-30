#!/usr/bin/sh
git restore --staged tests/sources/198707052100.rst
git restore --staged tests/sources/198707052100-hello-world.rst
git restore tests/sources/198707052100.rst
rm tests/sources/198707052100-hello-world.rst
git restore --staged tests/sources/202004301451-this-is-the-good-title.rst
git restore --staged tests/sources/202004301451-name-is-not-good.rst
git restore tests/sources/202004301451-name-is-not-good.rst
rm tests/sources/202004301451-this-is-the-good-title.rst
git checkout -- tests/sources/
