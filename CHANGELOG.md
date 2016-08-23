# ChangeLog
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [1.2.0-dev]

## Added
- Support for request-id via django-log-request-id (@vikalpj)
- Add `ssl_params` support in nginx
- Add `letsencrypt` support.
- Add `SASS` and `Django Compressor` support.
- Add documentation for Drone.io CI
- Add Circle CI Support (@jasonrfarkas)

### Changed
- Dropped support for Python2 (@akarambir).
- Improved project level logging support (@vikalpj)
- Remove factoryboy, use [django-dynamic-fixtures] for factories.
- Update SERVER_EMAIL settings to default to DEFAULT_FROM_EMAIL
- Use `setup.cfg` instead of `.bumpversion`
- Use `setup.cfg` instead of `.coveragerc`
- Upgrade whitenoise to 3.0
- anisble: Update supervisor init script
- travis: Use `pip-accel` on travis along with caching
- Removed 'pages' app
- Project renamed to `django-init`.
- Make ansible generation optional.
- Fix `Http404` and `PermissionDenied` error handling format.
- Add configurable support for `adding/removing DRF Browsable apis`



[django-dynamic-fixtures]: https://github.com/paulocheque/django-dynamic-fixture

### Added
- Livereload support via devrecargar

## [1.1.0]
### Added
- Provide a basic override for `admin/base_site.html`
- `base.utils.pagination.paginated_response` now accepts and additional `extra_context` parameter.
- Add Postgresql postgis support for Geo-django.
- Add `REDIS_MAX_CONNECTIONS` parameter with default reduced to 10.
- Add custom branding for drf's api browser login page.
- Allow admin email to be set via environment variable `DJANGO_ADMIN_EMAIL`
- Use `bin/post_compile` to handle database migration on Heroku.
- Switch to stable version of mkdocs
- Add custom user app with email as username
- Make use of `pytest-cov` plugin for generating coverage reports.
- Remove `pytest-pythonpath` from dependency as it's not longer needed.
- Replace `pytest-ipdb` with `pdbpp` as suggested by `pytest-ipdb`
- Use virtualenv in ansible provisioner to install project dependencies.
- Add variable in Nginx site configuration for max body size a client can send/upload.

### Changed
- Use `REDIS_URL` instead of `REDISTOGO_URL` for production redis connection.
- Replace redistogo with heroku-redis as default redis provider
- Use Official Postgresql apt-repo instead of Ubuntu's default.
- Upgrade to Django 1.9
- Use `django_extensions` only in development
- Default SMTP server to mailgun
- Use `cache_db` as `SESSION_ENGINE` instead of simple `cache`
- Use in-built `SecurityMiddleware` instead of django-secure
- Remove dependency on `django_extensions` for `TimeStampUUIDModel`

## [1.0.0]
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

[1.2.0-dev]: https://github.com/Fueled/django-init/compare/v1.1.0...master
[1.1.0]: https://github.com/Fueled/django-init/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Fueled/django-init/compare/v0.0.1...v1.0.0
