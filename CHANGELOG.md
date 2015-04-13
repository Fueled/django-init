# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased][unreleased]
### Added
- Removed celery settings, as it's hardly used.
- Add api versioning support via Accept headers (#52)
- Add `favicon.ico`, `robots.txt`, `humans.txt`
- Add `django-versatileimagefield`
- Add `base` app with common re-usable code
- Add `newrelic` support (#36)
- Add `iSort` configuration (#42)

### Changed
- Swap `django-storages` with `django-storages-redux`
- Add test for cookiecutter renderning (#34)
- upgrade to django-rest-framwork-3.0
- use redis for caching instead of memcached. (#35)

[unreleased]: https://github.com/Fueled/cookiecutter-django/compare/v0.0.1...HEAD
