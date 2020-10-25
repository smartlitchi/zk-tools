# Zettelkasten-Tools

I created this script to maintain my Zettelkasten. For those who don't know what a Zettelkasten is, you can go [here for more informations](https://zettelkasten.de/posts/overview/)

## Requirements

* python 3.8
* pipenv

## Installation

First, clone the repository : 

```sh
git clone git@github.com:zimhat/zettelkasten-tools.git
```

Then install required packages via ``pipenv``.

```sh
pipenv install
```

## Configuration

By default, it assumes your Zettelkasten path is ``~/Documents/zettelkasten``.  You can change that by changing this line in ``zk_tools.py``:

```py
zk_archive = os.path.expanduser("~/Documents/zettelkasten/")
# don't forget trailing slash
```

## Usage

For now, it has only two purposes : renaming zettels according to their title and checking if all links have the proper name.

```sh
pipenv run python zk_tools.py
```

## Testing

This program use [pytest](https://docs.pytest.org/en/stable/).

```sh
pipenv run pytest -v ; ./cleanup_tests.sh
```

The ``cleanup_tests.sh`` is a small script that gets rid of all the by-products of the testing process. Don't forget to run it to get a clean slate before testing again
