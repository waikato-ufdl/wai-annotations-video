Pypi
====

Preparation:
* increment version in `setup.py`
* add new changelog section in `CHANGES.rst`
* add new plugins to `DESCRIPTION.rst`  
* update plugin section in `README.md`
* commit/push all changes

Commands for releasing on pypi (requires twine >= 1.8.0):

```
  rm -r dist src/wai.annotations.video.egg-info
  python setup.py clean sdist
  twine upload dist/*
```


Github
======

Steps:
* start new release (version: `vX.Y.Z`)
* enter release notes, i.e., significant changes since last release
* upload `wai.annotations.video-X.Y.Z.tar.gz` previously generated with `setup.py`
* publish

