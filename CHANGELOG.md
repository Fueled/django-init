# ChangeLog
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## 1.1.0-dev
- Remove `pytest-pythonpath` from dependency as it's not longer needed.
- Replace `pytest-ipdb` with `pdbpp` as suggested by `pytest-ipdb`

## 1.0.0
### Added
- latest template configuration via dict
- `redistomonitor` addon on heroku setup
- `django-flat-theme` for admin interface
- common markdown extensions for mkdocs and various improvements
- support for UML: [sequence diagrams](http://en.wikipedia.org/wiki/Sequence_diagram)
- locale_path to settings, to help facilitate translation when required
- API versioning support via Accept headers (#52)
- `favicon.ico`, `robots.txt`, `humans.txt`
- `django-versatileimagefield`
- `base` app with common re-usable code
- `newrelic` support (#36)
- `iSort` configuration (#42)
- test for cookiecutter rendering (#34)
- `django-rest-framwork-3.x`
- `pytest` replacement for runtest
- Make S3 media upload configurational optional and dynamic
- Replace django-configuration with django-environ
- Swap `django-storages` with `django-storages-redux`
- Use redis for caching instead of memcached. (#35)

[unreleased]: https://github.com/Fueled/cookiecutter-django/compare/v0.0.1...v1.0.0
