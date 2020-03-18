#!/usr/bin/sh
git restore --staged tests/sources/198707052100.rst
git restore --staged tests/sources/198707052100-hello-world.rst
git restore tests/sources/198707052100.rst
rm tests/sources/198707052100-hello-world.rst
