# ChangeLog
All notable changes to this project will be documented in this file.

## [2.x]

- Change `created` and `modified` to `created_at` & `modified_at` respectively in `TimeStampedUUIDModel`. ([@CuriousLearner])
- Add `SWAGGER_SETTINGS` as per current drf setup ([@theskumar])
- Fix celerybeat service to be started/stopped correctly from systemctl. ([@CuriousLearner])
- Use new `pytest` instead of `py.test`. ([@CuriousLearner])
- Upgrade all the systems to use python 3.6. ([@theskumar])
- Add timezone information to datetime displayed in admin. ([@theskumar])
- Support for Django 2.0.x ([@theskumar])
- Make whitenoise optional, add static and media routes to nginx if whitenoise is not enabled. ([@tucosaurus])
- Make heroku deployment optional. ([@tucosaurus])
- Add api views (and docs) for password change, password reset and confirmation to the user app. ([@tucosaurus], [@theskumar])
- Ansible: make the log output human readable ([@theskumar])


## [1.11]
- Upgrade to Django RestFramework 3.7 (@theskumar)
- Adds custom Token based authentication for user login and registration. (@CuriousLearner)
- Separates out celery beat process as different worker for multi-node setups. (@CuriousLearner)
- Adds `ERROR` level logging to sentry mails. (@CuriousLearner)
- Fixes celery beat scheduler issue & makes celery role consistent across deployments. (@CuriousLearner)
- Add automatic documentation build when using ansible and make it available at `/docs/` url.
- Handle nested serializer errors in our custom exception handler. (@jainmickey)
- Remove mock dependency, replace with standard unittest.mock library
- Add `django-cors-headers` integration (@jainmickey)
- Add default 'AUTH_PASSWORD_VALIDATORS' in settings
- Add django-rest-swagger integration
- Use simplified bumpversion rules, remove requirement of intermediate release tags e.g. `0.1.0-dev`.
- Add multiple environment support on a single machine (@theskumar)
- Add .env.sample file (@theskumar)
- Add django-flat-responsive to give django-admin a responsive touch (@theskumar)
- Add django_auth_wall to protect staging environments (@theskumar)
- Replace gunicorn with uwsgi as wsgi handler (@vikalpj)

### Fixes
- Make default s3 region null.
- RemovedInDjango20Warning: Update admin url to new style url include (@theskumar)
- RemovedInDjango20Warning: Use new-style MIDDLEWARE settings (@theskumar)
- Fix letsencrtypt, make certbot-auto run in non-interactive mode.
- Fix `py.test` to load values from .env

## [1.9.0]

### Added

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

[@theskumar]: https://github.com/theskumar
[@CuriousLearner]: https://github.com/CuriousLearner
[@tucosaurus]: https://github.com/tucosaurus
