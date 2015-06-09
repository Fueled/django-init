# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased][unreleased]
### Added
- `django-flat-theme` for admin interface
- common markdown extensions for mkdocs and various improvements
- support for UML: [sequence diagrams](http://en.wikipedia.org/wiki/Sequence_diagram)
- locale_path to settings, to help facilitate translation when required
- api versioning support via Accept headers (#52)
- `favicon.ico`, `robots.txt`, `humans.txt`
- `django-versatileimagefield`
- `base` app with common re-usable code
- `newrelic` support (#36)
- `iSort` configuration (#42)
- test for cookiecutter renderning (#34)
- `django-rest-framwork-3.x`

### Removed
- celery settings, as it's hardly used.
- support for `Foundation`
- support for SaSS and Coffee via Grunt
- support for `Graphviz`
- urlize in mkdocs 

### Changed
- Make S3 media upload configurational optional and dynamic
- Replace django-configuration with django-environ
- Swap `django-storages` with `django-storages-redux`
- use redis for caching instead of memcached. (#35)

[unreleased]: https://github.com/Fueled/cookiecutter-django/compare/v0.0.1...HEAD
