History
----------------------

### 2021-09-22
 - Multiple fixes ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/de902b9))
 - Fix: cookiecutter tests ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/215d3be))

### 2021-08-28
 - Apply black formatting and add `make fmt` command ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9766e5a))
 - update default suffix for repo to be 'backend' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9e5b615))

### 2021-08-18
 - Upgrade python dependencies to latest (#435) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/edf842b))

### 2021-06-03
 - fix(users/auth): pyjwt requires the algorithm when calling decode() (#434) ([Akash Mishra](https://github.com/Fueled/django-init/commit/8d9aa0d))

### 2021-05-12
 - fix(installation): Upgrade pip before installing requirements (#433) ([Mayank Singhal](https://github.com/Fueled/django-init/commit/eb405c9))

### 2021-04-20
 - Upgrade python libraries to their latest except Django (#432) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8b62269))
 - feat() - make limit offset pagination default and add cursor pagination as optional (#430) ([Mayank Jain](https://github.com/Fueled/django-init/commit/eb053f4))
 - chore: cleanup ansible host file (#431) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/0d84ea3))

### 2021-03-23
 - Update python dependencies to their latest (#428) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/146fd07))

### 2021-03-02
 - fix(provisioner): celery beat start command for systemd service (#427) ([Akash Mishra](https://github.com/Fueled/django-init/commit/b9388d0))

### 2021-03-01
 - upgrade(requirements): Celery 4.4.7 -> 5.0.2 (#426) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/3bb660d))

### 2021-01-15
 - Tweak uwsgi config to allow for dyanamic number of workers (#424) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8b84481))

### 2020-12-22
 - Add github action CI on projects PR (#425) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/b30916d))
 - chore(*): Upgrade to Python 3.9, Postgres 13, PostGIS 3.0, Ubuntu 20 (#423) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/39651f7))
 - fix(ansible): fix celery startup ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4c878d5))
 - fix(bumpversion): make it work nicely with pre-commit hooks ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/17d839b))

### 2020-12-14
 - Update base pip packages (#422) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/b265d76))
 - fix(users/auth): Add validation for name & password in registration ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/c8f9e9e))

### 2020-11-04
 - docs - add documentation for MultipleSerializerMixin (#419) ([Akash Mishra](https://github.com/Fueled/django-init/commit/f237f76))
 - Fix the startup for celery and uwsgi-emperor on Ubuntu 20 (#418) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/dc094d3))
 - fix(postgis): ensure that gdal binary is installed ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2d9cdee))

### 2020-11-03
 - hotfix(nginx): fix port 80 config for nginx ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7fc3dcc))
 - feat(*) - add api mixin for permission per action on drf viewsets (#417) ([Akash Mishra](https://github.com/Fueled/django-init/commit/50f1d01))

### 2020-11-02
 - settings: make DJANGO_SECURE_SSL_REDIRECT configurable via environment variable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/401d23a))
 - feat(system) - replace python commit sorter with isort hook (#416) ([Akash Mishra](https://github.com/Fueled/django-init/commit/1e76850))

### 2020-09-29
 - feat(pre-commit) - configure black (#403) ([Akash Mishra](https://github.com/Fueled/django-init/commit/de3b64d))
 - Fix formatting for failed validation for one of the items in ListField (#413) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/10f662e))

### 2020-09-22
 - PyTest: Run failed test and then new test cases first (#414) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/47abf1a))

### 2020-09-07
 - update dependencies to latest (#412) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9eebcc7))

### 2020-08-14
 - Add "django.contrib.postgres" to list of INSTALLED_APPS ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/61b2657))
 - docs: improve setup docs on mac ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9ebae29))

### 2020-07-01
 - docs(): automate generating the latest db schema on deployment in docs (#408) ([Mayank Jain](https://github.com/Fueled/django-init/commit/c320db1))

### 2020-06-22
 - update readme ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/857c150))
 - Add artwork ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/85cadb7))

### 2020-06-07
 - chore - upgrade django (#407) ([Akash Mishra](https://github.com/Fueled/django-init/commit/074c08c))

### 2020-05-28
 - feat: upgrade python dependencies to latest stable (#406) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/db214aa))

### 2020-05-26
 - Upgrade django 3.0.5 -> 3.0.6 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/bef5376))
 - Update documentation (#405) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/441c5d1))

### 2020-05-20
 - Remove web pack + replace fabric with makefile (#404) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3a09db9))

### 2020-05-06
 - docs(auth): Update user registration API docs (#401) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/2468d21))
 - fix(users/serializers): Add first_name and last_name (#400) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/e72d09c))

### 2020-05-01
 - Fix travis config for postgresql 11 (#399) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b755b57))

### 2020-04-29
 - upgrade whitenoise to work with django 3 (#398) ([Anuvrat Parashar](https://github.com/Fueled/django-init/commit/316794e))

### 2020-04-16
 - Add support for Django 3.x (#397) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/b9963ff))

### 2020-04-09
 - Remove circle CI support (#395) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/5be90e0))

### 2020-04-08
 - fix(travis): Remove docker and install Postgres 11 directly on Travis (#394) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/4ec048c))

### 2020-04-07
 - feat(provisioner) - install python3 psycopg2 (#393) ([Akash Mishra](https://github.com/Fueled/django-init/commit/84e1fd3))

### 2020-04-06
 - chore(): upgrade django to 2.2.10 for security fix (#389) ([Mayank Jain](https://github.com/Fueled/django-init/commit/5ef7aa7))
 - chore(deps): bump acorn in /{{cookiecutter.github_repository}} (#390) ([dependabot[bot]](https://github.com/Fueled/django-init/commit/36cc2cb))
 - set python3 as default interpretor for ansible (#392) ([Mayank Jain](https://github.com/Fueled/django-init/commit/785c90b))

### 2020-01-29
 - fix(swagger) - include default schema class settings for swagger ui (#388) ([Akash Mishra](https://github.com/Fueled/django-init/commit/64e5fec))

### 2020-01-20
 - chore - use actively maintained bump2version instead of bumpversion (#387) ([Akash Mishra](https://github.com/Fueled/django-init/commit/67bd5bd))

### 2020-01-10
 - fix(provisioner) - typo for letsencrypt_challenge_root in defaults (#386) ([Akash Mishra](https://github.com/Fueled/django-init/commit/976e057))

### 2019-12-18
 - fix(requirements): Update Django to 2.2.9 for security fix (#385) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/58bb634))

### 2019-12-05
 - chore(): Update django-log-request-id to 1.4.0 (#384) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/5408a61))
 - Fix typo of variable "letsencrypt_challenge_root" (#383) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/00f2a25))
 - chore(requirements) - update django to 2.2.8 for security fix (#382) ([Akash Mishra](https://github.com/Fueled/django-init/commit/647a49c))

### 2019-11-20
 - chore(): Update dependencies (#381) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/6a60910))

### 2019-10-24
 - chore - update pillow due to security vulnerability (#379) ([Akash Mishra](https://github.com/Fueled/django-init/commit/ca1b415))

### 2019-10-16
 - feat(*) - vendor media type for Accept header (#377) ([Akash Mishra](https://github.com/Fueled/django-init/commit/34639e0))

### 2019-10-15
 - chore - update django, django rest framework, cors headers (#378) ([Akash Mishra](https://github.com/Fueled/django-init/commit/ee2016f))

### 2019-10-04
 - feat(users/auth) - Use standard Bearer authentication scheme (#375) ([Akash Mishra](https://github.com/Fueled/django-init/commit/e532e62))

### 2019-09-25
 - Add black in pre-commit and also formatted exiting code as per black (#374) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8b6aa96))

### 2019-08-21
 - fix(changelog): Cleanup changelog and add links. (#373) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/c8fe2cb))
 - feat(): upgrade to use python 3.7 (#371) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3e2bc23))
 - fix(coding_rules): Fix formatting for rules for field lists (#372) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/3c21181))
 - refractor: improve variable naming and standardize log and venv dirs (#370) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e1a58eb))

### 2019-08-20
 - hotfix(webpack): fix missing variable name "webpack_node_version" ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b266e9e))

### 2019-08-06
 - chore - upgrade django for security fix (#369) ([Akash Mishra](https://github.com/Fueled/django-init/commit/1c965e9))

### 2019-07-30
 - fix(nginx): let nginx configure it's no. of workers based on no. of CPUs (#368) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/06b03eb))

### 2019-07-29
 - docs(): add concepts section in backend architecture ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6c07085))
 - Update celery concurrency to default to number of CPUs (#367) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/660357c))
 - Update mkdocs to use mkdocs-material and update structure (#366) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/89644c0))

### 2019-07-25
 - fix(template): use 'static' tag properly ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/09231c4))

### 2019-07-16
 - fix(cookiecutter/pre-commit): remove the complete file instead of just commenting content ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/05d33f7))
 - add updated and verified package-lock.json ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3b24b43))
 - Update babel/core to latest to fix security issue in lodash <= 4.17.13 (#365) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0dad864))
 - chore(ansible): remove unused webpack related variables ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6a52f53))

### 2019-07-10
 - refractor(urls): update urls.py to use new 'path' and 're_path' (#364) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c0efe68))

### 2019-07-08
 - fix(heroku): update post_compile file for webpack ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/005463b))

### 2019-07-04
 - chore - update django for security fix (#363) ([Akash Mishra](https://github.com/Fueled/django-init/commit/39ef59b))

### 2019-06-25
 - fix(pre-commit-config.yml): Minor indentation fixes (#362) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/57c619e))
 - Fix celerybeat run dir (#357) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/f049214))
 - fix(logger): use ServerFormatter for request logs in runserver (#360) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d0d6cee))

### 2019-06-11
 - Update requirements to their latest, Django 2.2.x (#358) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/5b0734b))

### 2019-06-10
 - chore(pytest): remove @set_settings decorator as pytest-django provide equivalent settings fixture ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/baf5c7d))
 - fix(ansible): fix for Ubuntu 18 for ansible 2.5 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b7a4f63))
 - fix(ansible): add task to build documentation on server ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/451c307))
 - feat(postgres): Upgrade to Postgres 11 Postgis 2.5 (#349) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/4495aab))

### 2019-06-03
 - docs(readme): Add articles section with sanyam post in it ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7b2015e))
 - chore: add .github folder ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/09783b8))
 - fix(security): update fstream ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0b582ae))

### 2019-05-30
 - upgrade(requirements/dev): Upgrade to ansible 2.5.15 (#356) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/7bdfebe))

### 2019-05-28
 - chore(deps): update requirements to it's latest stable (except django) (#354) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f396a97))
 - chore(docs): minor changes to README ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/aec7b68))
 - chore(docs): update travis-ci.org to travis-ci.com ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/508b5d8))

### 2019-05-27
 - fix(webpack): ensure node_modules are installed locally ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/242e93a))
 - chore(webpack/ansible): adjust webpack path to run from local installation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/aacd626))

### 2019-05-24
 - chore - upgrade django rest framework to latest (#353) ([Akash Mishra](https://github.com/Fueled/django-init/commit/1f7eb71))

### 2019-05-21
 - feat(pre-commit): Add pre-commit hooks (#345) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/02c2ee8))
 - fix(webpack/security): update dependencies ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/477b0ff))
 - Add CORS_ORIGIN_WHITELIST in .env.sample ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9571c46))

### 2019-05-20
 - feat(webpack): Add webpack support and remove django-compressor support. (#184) ([Mayank Jain](https://github.com/Fueled/django-init/commit/7714df6))

### 2019-05-12
 - style(): make coding-style consistent ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3abf835))

### 2019-04-22
 - feat(requirements): upgrade django-rest-swagger to 2.2.0 (#348) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/030d72c))

### 2019-04-17
 - Update docs for Postgres and PostGIS updates (#347) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/d83d1da))
 - chore(*): Upgrade Postgres to 10 and PostGIS to 2.4 (#346) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/c369ea8))

### 2019-03-27
 - fix(celery.py): Sort import for celery (#343) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/9c8c804))
 - fix(*): Sort-import statements (#344) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/99b20c2))

### 2019-02-28
 - docs - make markdown header notation in docs consistent (#341) ([Akash Mishra](https://github.com/Fueled/django-init/commit/f489966))

### 2019-02-26
 - fix - remove raven import when sentry is not being used (#342) ([Akash Mishra](https://github.com/Fueled/django-init/commit/b620445))

### 2019-02-14
 - chore(requirements): Upgrade Django to 2.1.7 (#340) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/bd12275))

### 2019-02-13
 - chore(requirements): Upgrade Django from 2.1.5 to 2.1.6 (#339) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/d0f953d))

### 2019-01-30
 - fix(settings/common): Set-up IS_RAVEN_INSTALLED variable (#338) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/97eafa3))
 - refactor(settings/common) - do string comparison using "!=" instead of "is not" (#337) ([Akash Mishra](https://github.com/Fueled/django-init/commit/f10c496))

### 2019-01-24
 - fix(settings): Add 'access-control-allow-origin' to CORS headers (#336) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/d20ff75))
 - fix(common/production): Fix spelling for assets (#335) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/9a04f68))
 - fix(requirements): Upgrade Django to prevent content spoofing (#333) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/8b9923d))
 - fix(settings/production): Minor spell fix (#334) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/0d4b054))

### 2019-01-10
 - fix(settings/dev): Added MEDIA_URL configuration (#324) ([Shashank Kumar](https://github.com/Fueled/django-init/commit/4b9794f))

### 2018-12-17
 - fix(provisioner/roles/redis): Update ansible state from installed to present (#332) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/97a7586))

### 2018-12-13
 - chore(requirements): Downgrade Swagger to 2.1.2 from 2.2.0 (#331) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/ece771d))

### 2018-12-11
 - chore(requirements): Update requirements to latest stable (#329) ([Saurabh](https://github.com/Fueled/django-init/commit/0735c17))

### 2018-12-10
 - chore(requirements): Upgrade Django=2.1.4 & DRF 3.9.0 (#328) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/c970ac8))
 - fix(user/auth/backends.py): Minor spell fix (#327) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/5dc3c48))

### 2018-11-12
 - feat(provisioner) - password protect the project documentation (#312) ([Akash Mishra](https://github.com/Fueled/django-init/commit/778be01))
 - fix(provisioner) - install gettext for compilemessages (#326) ([Akash Mishra](https://github.com/Fueled/django-init/commit/5b7640b))

### 2018-11-01
 - fix(whitenoise): for django whitenoise must not be added to wsgi.py now ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f5eceb7))

### 2018-10-31
 - chore(ansible/nginx): de-duplicate the cert part creation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e8affe2))

### 2018-10-23
 - chore(requirements) - pin pytest version to avoid attrs incompatability (#325) ([Akash Mishra](https://github.com/Fueled/django-init/commit/0e5f33d))
 - fix(base/api/routers): Deprecating DynamicListRoute (#322) ([Shashank Kumar](https://github.com/Fueled/django-init/commit/27b07af))

### 2018-10-17
 - Update dependencies to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0929291))

### 2018-10-02
 - fix(): auth test ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f51afa1))
 - Remove depreciation warning for staticfiles templatetags ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d116d98))

### 2018-08-17
 - change `pages` option in `mkdocs.yml` file to `nav` (#320) ([Aniket Maithani](https://github.com/Fueled/django-init/commit/4262825))

### 2018-08-13
 - Upgrade to Django 2.1.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/403324e))

### 2018-08-09
 - fix(system) - Update celery to avoid kombu incompatibility (#318) ([Akash Mishra](https://github.com/Fueled/django-init/commit/ebbe147))

### 2018-08-07
 - fix(provisioner/nginx.conf): Minor typo fix (#317) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/379c5b7))

### 2018-08-03
 - feat(localization): Add compilemessages & fix default pypi mirror (#316) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/9518384))
 - Add LocaleMiddleware in settings to add multi-language support (#310) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/43e1584))

### 2018-07-13
 - migrated COMPRESS_CSS_FILTERS to COMPRESS_FILTERS as per the documentation - https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS (#314) ([Anirudh Goel](https://github.com/Fueled/django-init/commit/e70ab05))

### 2018-05-31
 - feat(system) - Upgrade to Django Rest Framework 3.8.x (#311) ([Akash Mishra](https://github.com/Fueled/django-init/commit/7e1bd0c))

### 2018-05-07
 - hotfix - revert celery import cleanup (#309) ([Akash Mishra](https://github.com/Fueled/django-init/commit/bbdf10b))

### 2018-04-16
 - Fix tests ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/febe301))
 - Add ansible and fabric3 as local development requirement ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b557741))
 - fix test, remove 2to3 check ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e67f4b6))
 - fixup! chore(provisioner/roles/nginx): remove ` State 'installed' is deprecated.` warning (#308) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/308cd79))
 - chore(provisioner/roles/nginx): remove ` State 'installed' is deprecated.` warning (#308) ([Aniket Maithani](https://github.com/Fueled/django-init/commit/6427422))

### 2018-04-07
 - chore: minor cleanup settings -> common ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ac38555))

### 2018-03-16
 - chore(celery): minor cleanup ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ad98f11))
 - Move  utility to ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/77ec9b2))
 - feat(current_user_view): Adds API for modifying and getting logged-in user profiles (#278) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/fa1bbdc))
 - Add flake8 in travis builds of django-init (#307) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/1c7a133))

### 2018-03-14
 - Add list of related project by @pydanny, @wemake-services & @lionheart ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/47d2cc6))
 - fix(base/models): Fix naming in TimeStampedUUIDModel (#306) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/68b9c84))

### 2018-03-11
 - Update all the requirements to latest stable (#304) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/72bd4ba))
 - Fix issue with permission class at /schema url (#305) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2649dca))

### 2018-03-09
 - Security release django 2.0.3 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/04bf78b))

### 2018-03-07
 - Add .pytest_cache to ignore ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/5a6d011))

### 2018-03-06
 - Add swagger settings, as per current drf configuration (#302) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/86ed725))
 - feat(provisioner) - remove extra uwsgi build from common tasks (#303) ([Akash Mishra](https://github.com/Fueled/django-init/commit/90e0a65))

### 2018-03-05
 - Remove python2 compatibility from User model ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8735d69))

### 2018-03-01
 - Add media_root fixture to force media in temp folder ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4aa661f))
 - fix(celery-beat): Fix celery beat service (#301) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/9d97635))

### 2018-02-28
 - hotfix(provisioner/uwsgi): fix file path ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a76697d))
 - refractor(ansible): move uwsgi setup to it own file (#299) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/bf73ad1))
 - fix(api/auth): add UserTokenAuthentication in default authentication classes ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6fb34ee))

### 2018-02-20
 - fix(tests): Use pytest instead of py.test (#300) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/a313d08))

### 2018-02-18
 - Install uwsgi as project dependency only on heroku servers (#298) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/99882d0))

### 2018-02-16
 - Ansible: make the log output human readable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/292742a))

### 2018-02-15
 - chore(requirement): use psycopg2-binary ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e03e5b1))
 - chore(test): Add docs for client fixture, update to use native django client ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/74c43fa))
 - fix(ansible): remove depreciation warning ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4586a8b))
 - fix(provisioner): handle the incorrect rendering if celery is selected ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/421289f))

### 2018-02-14
 - Update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a97a4c9))
 - feat(system): upgrade from python 3.5.x to python 3.6.x (#283) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d31bdc6))

### 2018-02-07
 - Password management rest APIs for custom user app (from #290) (#294) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0ff84e7))
 - Optional heroku support (#296) ([Akash Mishra](https://github.com/Fueled/django-init/commit/ebdb1c5))

### 2018-02-06
 - fix(settings): Fix django-sites config along with MEDIA_URL (#295) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/858f22c))
 - Make whitenoise optional (#291) ([Akash Mishra](https://github.com/Fueled/django-init/commit/3b7253b))

### 2018-01-22
 - Add timezone information to datetime displayed. (#289) ([Saurabh](https://github.com/Fueled/django-init/commit/ccd24b6))

### 2018-01-18
 - fixing pep8 W391 blank line at end of file in user app (#288) ([Akash Mishra](https://github.com/Fueled/django-init/commit/d51da39))

### 2018-01-17
 - Add fix for nested api error ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ab6e360))
 - Django 2.0 support (#284) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/75ac3b5))
 - Renamed environment var to deploy_environment (#287) ([Akash Mishra](https://github.com/Fueled/django-init/commit/d398f5c))

### 2018-01-07
 - Update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f4c5c38))

### 2018-01-02
 - chore(users/services.py): removed unused import (#285) ([Aniket Maithani](https://github.com/Fueled/django-init/commit/c3f341d))

### 2017-12-28
 - feat(drf): upgrade drf to 3.7.x (#282) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c6ee8cb))

### 2017-12-27
 - fix(cookiecutter/test): ensure that postgres version is same as internal requirement ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/076dc7d))
 - fix(requirement): upgrade celery 4.0.2 -> 4.1.x ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/cfc2bea))
 - feat(isort): skip applying isort for the 'migrations' folder ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/85484b7))

### 2017-12-13
 - fix(auth): Add routers for auth viewsets (#276) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/8c1488d))

### 2017-12-07
 - feat(auth): Add custom user auth based on JWT tokens (#272) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/d5d7dbf))
 - update postgresql, add postgis addon and remove pip accel (#273) ([Mayank Jain](https://github.com/Fueled/django-init/commit/08002f4))
 - Upgrade node dependencies (#269) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/55d131a))

### 2017-12-03
 - Add support for static type hinting check via flake8-mypy (#270) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/728adea))
 - feat(.travis.yml): Removes pip-accel (#271) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/1aafe3b))

### 2017-11-30
 - fix(nginx): update the default client_max_body_size value ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b5f516b))

### 2017-11-12
 - fix(ansible): add official nginx and certbot repo and configuration ([Mayank Jain](https://github.com/Fueled/django-init/commit/5c5664f))

### 2017-11-08
 - fix(celery): Separates out celery beat process as different worker (#264) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/506d22a))
 - feat(logging): Add Error level logging to sentry mails (#267) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/c1637da))

### 2017-11-06
 - Add support for case insensitive emails (#261) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/c22dc59))
 - fix(settings): make s3 region default null (#265) ([Mayank Jain](https://github.com/Fueled/django-init/commit/7af8a8a))

### 2017-10-30
 - fix(celery): celery beat scheduler issue (#263) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/f5736e4))

### 2017-10-23
 - nginx: enable ngx_http_charset_module to add default utf-8 encoding to content-type headers (#260) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3d6e4a5))
 - nginx: enable ipv6 support (#259) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2d5d8fa))

### 2017-10-11
 - Add automatic documentation build when using ansible and make it available at `/docs/` urls (#258) ([Saurabh](https://github.com/Fueled/django-init/commit/aadae2b))

### 2017-09-24
 - fix(pages) Fix typos: comming > coming (#257) ([Joe Richardson](https://github.com/Fueled/django-init/commit/98274e9))

### 2017-09-13
 - Update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/791549d))

### 2017-08-22
 - settings: make putting up ALLOWED_HOSTS compulsory in production (#253) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c2498fc))
 - uwsgi: Ignore os write errors in django-uwsgi (#254) ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/19f725f))

### 2017-08-17
 - Update README.md ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2b8f713))
 - feat(nginx): Add security improvements for ssl. (#252) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4f53649))
 - enhance security by disabling deprecated ciphers (#248) ([Anuvrat Parashar](https://github.com/Fueled/django-init/commit/fbd8fca))
 - Enable http2 (#246) ([Anuvrat Parashar](https://github.com/Fueled/django-init/commit/fb9849f))
 - Minor spell fixes in coding_rules.md (#247) ([Sanyam Khurana](https://github.com/Fueled/django-init/commit/0b90c85))
 - fix(base): update multi serializer mixin (#245) ([Mayank Jain](https://github.com/Fueled/django-init/commit/51f3242))
 - Update requirements to latest stable / Django 1.11.4 (#250) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e0d1925))

### 2017-08-03
 - feat(cors): add `django-cors-headers` integration (#233) ([Mayank Jain](https://github.com/Fueled/django-init/commit/a05b514))

### 2017-07-12
 - fix(fabfile): minor typo in dev() function ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d675818))
 - docs(travis): add minor note on documentation reference ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a105edd))

### 2017-07-10
 - fix(requirements): remove duplicate requirement (#242) ([Mayank Jain](https://github.com/Fueled/django-init/commit/bd1d9d6))

### 2017-07-06
 - fix(nginx/letsencrypt): ensure nginx is reloaded after renewal of cert (#241) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/5be9349))

### 2017-07-05
 - Upgrade requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7a935a6))
 - docs(coding_rules): update sample code as per python 3 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4b5c50f))
 - cleanup(docs): remove drone.io docs ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d0273b2))

### 2017-06-13
 - update requirements to latest stable ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/a3dae02))
 - feat(exceptions): handle nested serializer errors in our exception handler ([Mayank Jain](https://github.com/Fueled/django-init/commit/0284d61))
 - Remove mock dependency, replace with standard unittest.mock library (#238) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2dc65b8))

### 2017-05-23
 - update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/77dcc6e))
 - Add some default "AUTH_PASSWORD_VALIDATORS" ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b8a15c9))
 - chore(): use python3 notation for calling super() ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4a45eab))
 - chore(.env): add 'django_settings_module' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a96d0ad))

### 2017-05-17
 - Add django-rest-swagger integration ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/59e66dd))
 - fix(settings/celery): update CELERY_BROKER_URL to properly respect REDIS_URL (#229) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9e589d9))

### 2017-05-10
 - Update bumpversion logic to make it simple (#228) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b10dabc))

### 2017-05-05
 - chore(ansible/nginx): Check nginx config before reload/restart (#227) ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/aa5ba8e))

### 2017-05-03
 - Add support for multiple deployments on same machine (#223) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a66dde3))

### 2017-05-01
 - Log SHA of last and new commit being deployed by ansible provisioner ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/70526e3))

### 2017-04-26
 - docs: Add explaination for '* text=auto' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a640432))
 - Update requirements to latest stable version ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f1571b8))
 - Fix depreciation warnings - RemovedInDjango20Warning (#224) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/eca2e1e))
 - feat(celery): add celery configuration (#225) ([Mayank Jain](https://github.com/Fueled/django-init/commit/da83200))

### 2017-04-04
 - fix(provisioner): make sure python is available before setting hostname ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3e866f6))
 - Update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c2081aa))

### 2017-03-07
 - Add release policy ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/285e88b))
 - Add .env.sample (#221) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/502a810))
 - Normalize double quotes to single quotes (#220) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/946cef1))
 - Add .env.sample (#221) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/619f128))
 - Update requirements to latest [security release] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c62a51a))

### 2017-02-24
 - Update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e6c8101))

### 2017-02-14
 - Update `ALLOWED HOSTS` and `INTERNAL_IPS` in dev settings (#219) ([Abhishek Kumar Singh](https://github.com/Fueled/django-init/commit/7ae0622))

### 2017-02-13
 - fix(settings): Fix flake8 issues with wsgi and settings (#217) ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/b9a5e05))
 - fix(provisioner/project): Give uwsgi group the ownership of project dir (#216) ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/b3e5512))

### 2017-02-08
 - enable aws signature_version 4 for newer regions ([Anuvrat Parashar](https://github.com/Fueled/django-init/commit/39a881d))

### 2017-02-02
 - fix(nginx): update gzip compression file list ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7b8aa2e))

### 2017-01-26
 - Fix 'py.test' to load values from .env (#212) ([Abhishek Kumar Singh](https://github.com/Fueled/django-init/commit/68e4c93))
 - Minor Typo fix. (#211) ([Abhishek Kumar Singh](https://github.com/Fueled/django-init/commit/a7f3f6a))

### 2017-01-25
 - Fix imports for raven and pytest (#209) ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/91c6c0a))
 - Update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/60a026f))

### 2017-01-11
 - Fix celery log dir issue with logging module ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/d7e692c))
 - Update readme to ubuntu version supported ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/edd29dc))
 - Update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/bba5cff))

### 2016-12-28
 - fix(celery): Change celery role to use systemd init system ([Mayank Jain](https://github.com/Fueled/django-init/commit/c3369ec))

### 2016-12-17
 - Update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2e6d14e))

### 2016-12-13
 - Add PS1 to display fqdn & set hostname via ansible (#205) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c7844db))

### 2016-12-07
 - fix(nginx): Fix vagrant nginx file (#203) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/2f83c95))

### 2016-12-06
 - fix(nginx_role): Fix the ansible condition to generate dhparam file (#202) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/935a803))
 - fix(django_compressor): Fix issues with nodejs setup django compressor (#201) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/ab8e94d))

### 2016-11-30
 - Fix letsencrtypt, make certbot-auto run in non-interactive mode (#200) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7a5cab9))

### 2016-11-28
 - Add django-flat-responsive to give django-admin a responsive touch (#199) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c71fbfc))

### 2016-11-27
 - Update Python requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/41fbf2d))

### 2016-11-18
 - fix(debug-toolbar): As per django-debug-toolbar 1.6 we need to manually add the url in url.py (#198) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/edf89df))
 - Add staging site protection with Basic Auth ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d962cbc))
 - Ubuntu16 (#181) ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/b36fe17))
 - feat(sentry): Add sentry support. (#190) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/72e82fd))

### 2016-11-10
 - Update requirements to latest, Django 1.10.3 (security udpate) (#194) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/271eb43))

### 2016-11-01
 - feat(uwsgi): replace gunicorn with uwsgi ([Vikalp Jain](https://github.com/Fueled/django-init/commit/80c8744))

### 2016-09-29
 - Update requirements to latest stable. (#187) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fb50fa4))

### 2016-09-08
 - Update README.md ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6bcde30))

### 2016-09-07
 - Update Node Dependency (#186) ([Pulkit Pahwa](https://github.com/Fueled/django-init/commit/b08cd30))

### 2016-09-02
 - Upgrade to Django 1.10.x (#180) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e55c367))

### 2016-08-31
 - chore(pytest-warning): removed WC1 pytest warning in CI (#185) ([Aniket Maithani](https://github.com/Fueled/django-init/commit/7552751))

### 2016-08-25
 - Prevent error pages from being archived/crawled ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7d8388a))

### 2016-08-23
 - Update docs ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3c10eef))
 - feat(python3): Remove usage of python2 from project code. Use only python3 (#179) ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/5259aa8))

### 2016-08-19
 - Update third-party requirement to latest (#178) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4257749))

### 2016-08-10
 - Make sure DJANGO_ADMINS is set via environment variable in production (#174) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/92f38e8))
 - Upgrade to flake8==2.6.*, handle F405 warnings (#175) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f296099))

### 2016-07-21
 - Add coc ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ac827a2))
 - Update readme ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3d1e23c))
 - style(base/views): update comment and indentation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/af39d08))
 - style(base/views): update comment and indentation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d447fc3))
 - Update django-debug-toolbar to 1.5 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/abedf04))
 - Update requirements to latest. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/432cc50))

### 2016-07-01
 - chore(settings/logging): update copy of comments for request_id filter ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/af70d64))
 - update changelog ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/5d23a25))
 - Add support for `Logging` (#169) (#172) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/40dd52c))

### 2016-06-18
 - Add support of `ssl_dhparam` in nginx (#171) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/98c6683))

### 2016-06-07
 - Add cleared_cache fixture to clear cache before running test + some refractoring ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f05f760))

### 2016-06-03
 - feat(sass): Add sass and django compressor ([Mayank Jain](https://github.com/Fueled/django-init/commit/392d7b0))
 - feat(ansible/letsencrypt): add letsencrypt support ([Mayank Jain](https://github.com/Fueled/django-init/commit/a24d127))

### 2016-05-31
 - fix(provisioner/project_data): make sure .env file is not created with root user ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4719a29))

### 2016-05-30
 - fix(provisioner): Add a global default VM=0, in order to get rid of undefined var error ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a3beca6))
 - fix(ansible/project_data): make sure get_data is run always ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d6f7784))

### 2016-05-25
 - refractor(tests): use django-dynamic-fixtures instead of factory-boy ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/99c9ffc))
 - Update requirements - whitenoise, django-redis, gunicorn, boto ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2a23225))

### 2016-05-23
 - Update SERVER_EMAIL settings to default to DEFAULT_FROM_EMAIL ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ebc6315))

### 2016-05-22
 - feat(django/admin): Allow customizing admin url path via environ (#164) ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/1b34375))
 - Update virtualbox config to use min 1GB RAM, default is 512MB. (#161) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c7f2777))
 - Move .bumpversion.cfg –> setup.cfg (#163) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b63fd57))

### 2016-05-10
 - chore(coverage.py): Move .coveragerc config to setup.cfg ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/cafe70b))

### 2016-05-04
 - Upgrade django, django-extensions, python-dotenv ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b2d85d5))

### 2016-05-03
 - chore(api-settings): remove browsable api from prod environments (#158) ([Vikalp Jain](https://github.com/Fueled/django-init/commit/8df3b2e))

### 2016-05-02
 - fix(exceptions): fixed django exceptions error handling format. (#157) ([Mayank Jain](https://github.com/Fueled/django-init/commit/3442f02))

### 2016-04-27
 - Update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a2fc248))

### 2016-04-26
 - Add dump.rdb to .gitignore ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6617897))

### 2016-04-17
 - Remove unused setting "AUTOSLUG_SLUGIFY_FUNCTION" ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7ca0930))

### 2016-04-12
 - Fix incorrect rendering of travis.yml file ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/109e6a9))

### 2016-04-11
 - Add ansible's 'site.retry' file in gitignore ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f2e3d85))
 - Remove duplicate settings value ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a91654c))

### 2016-04-05
 - Update to django 1.9.5 and pillow 3.2.0 to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/033c0a4))

### 2016-04-04
 - feat(ci): add circle.yml to use circle ci ([Jason](https://github.com/Fueled/django-init/commit/f50d99c))
 - docs(continuous integration): add documention as to how to use drone.io with screenshots ([Jason](https://github.com/Fueled/django-init/commit/3ecc9c8))
 - feat(staticfiles): Upgrade to whitenoise 3.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c7b5ef6))

### 2016-03-31
 - feat(cookiecutter): make generation of ansible related stuff optional ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a7e4dca))
 - Update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6e65482))

### 2016-03-18
 - Remove gunicorn as ansible role & move it as task in project_data ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f2f4fd1))

### 2016-03-16
 - chore(): Remove references to fueled inside generated project ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/81cc6eb))

### 2016-03-15
 - Update supervisor init script to include supervisorctl status ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ac37f0f))
 - Enable livereload of frontend pages/assets in Development ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d962e93))
 - Use `pip-accel` on travis along with caching ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f3badd0))

### 2016-03-14
 - Improve 'post_gen_project' docs ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/29dc7fb))
 - Make the setup instrunctions a bit clearer ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/937588c))
 - refractor(apps): remove pages app ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b20abe0))

### 2016-03-11
 - Add pull-request template ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/05fae7e))

### 2016-03-10
 - feat(base/exceptions): Change how custom exception handler display error ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/9e81e89))
 - fix(fab): use `runserver` instead of 'runserver_plus' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/cfc158e))

### 2016-03-08
 - fix(testing): while running use 'settings.testing' module ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/60c4607))
 - Add licence ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/bcbddad))
 - Rename the project to "django-init" ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9cc4a21))
 - Release 1.1.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3c18886))

### 2016-03-07
 - Upgrade to django 1.9.4 [security release] ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/fed6d32))

### 2016-03-04
 - Upgrade to django 1.9.3 [security release] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2e8b7e1))

### 2016-03-01
 - Improve python3 support ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/73b6eb1))
 - Update python imports to be iSort friendly ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/eccfd09))

### 2016-02-29
 - Procfile: simplify logic to inject the newrelic executor ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ce5a6c5))
 - Update changelog ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6862c50))
 - feat(utils/pagination): Add `extra_context` in pagination class ([Mayank Jain](https://github.com/Fueled/django-init/commit/8d16ef8))
 - feat(admin/template): Add admin base template ([Mayank Jain](https://github.com/Fueled/django-init/commit/3274e8b))
 - chore(nginx): Add placeholder to disable SSLv3 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4f7cb5f))

### 2016-02-24
 - Update ansible commands which were giving warnings ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/d9bd656))
 - fix(provisioner): use '--reload' flag in gunicorn inside virtualenv ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e3da118))
 - Update .gitignore, add 'htmlcov/' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2ba4783))
 - chore(users): remove redundant check for persence of email property ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/be2d28d))
 - Update docstrings to use double quotes ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/de64447))
 - chore(settings): move INTERNAL_IPS to debug section ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3c17605))
 - Replace redistogo with heroku-redis on redis ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3780776))

### 2016-02-23
 - Update migration for users app as per Django==1.9.2 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/188fbb8))

### 2016-02-22
 - fix(vagrant/provisioner): Make ansible provisioner run in vagrant ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/b9f83b5))

### 2016-02-12
 - feat(ansible/postgresql): Add postgis support for postgresql role ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/25dd9ee))

### 2016-02-11
 - fix(ansible/nginx): remove unnecessary declarations ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f97b42c))
 - fix(ansible/gunicorn): remove duplicate line ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/11ac3d3))

### 2016-02-08
 - Remove memcache related libraries (libmemcached-dev and python-memcache) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2bbe1be))
 - Fix ansible, .inputrc is now created if not present. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ff0b317))
 - chore(docs): fix link to django_sites documentation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/de4c570))

### 2016-02-04
 - Update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c698153))

### 2016-01-22
 - feat(ansible): update ansible to use virtualenv ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/e7a32ba))
 - chore(test): add travis to use postgres 9.4 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fe81ec9))

### 2016-01-19
 - feat(settings): Add `REDIS_MAX_CONNECTIONS` parameter with default reduced to 10. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/dacf979))

### 2016-01-12
 - chore(docs/api): fix indentation in the overview section [ci skip] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/003cc17))

### 2016-01-09
 - Upgrade pillow to 3.1.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/359a408))

### 2016-01-03
 - Upgrade to Django 1.9.1 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/770cff8))

### 2015-12-30
 - Remove dependency on django_extensions for TimeStampUUIDModel ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9ad0e0c))

### 2015-12-21
 - feat(drf/api-browser): add custom branding on api login page ([srinivasulureddy](https://github.com/Fueled/django-init/commit/cc4789e))

### 2015-12-17
 - Upgrade to Django 1.9 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/1290e53))
 - fixing the css. Branding block ([srinivasulureddy](https://github.com/Fueled/django-init/commit/9a795ef))

### 2015-12-16
 - Move django-extensions to dev settings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3ae75c2))
 - Update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3d80bce))

### 2015-12-11
 - fix(requirements): Use django_extensions only as development requirement ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/bff7bdc))
 - Update cookiecutter.json, make it dynamic based of previous inputs ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f492057))
 - feat(settings): Allow ADMINS to be set via environment variable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f2c49d9))
 - Use `/bin/post_compile` to run migration and deployment checks ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3e8f469))

### 2015-12-10
 - feat(settings): use in-built `SecurityMiddleware` instead of django-secure ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6e4e7e3))
 - chore(docs/js): inline external helper javascript, reduce external dependency ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/79dc875))

### 2015-12-09
 - style(settings): minor spacing refractor ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0e05534))
 - fix(tests): update to use 'testing' settings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b2ba099))
 - docs(server-config): remove sequence-diagram, not very useful ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/aa7a0aa))

### 2015-12-08
 - chore(settings): Remove gevent library for production environments ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/ca6f932))
 - Update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9b789f1))
 - feat(settings): use `cache_db` as `SESSION_ENGINE` instead of simple `cache` ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e873053))

### 2015-12-04
 - fix(django1.9): change urls, log.NullHandler, context_processors ([Mayank Jain](https://github.com/Fueled/django-init/commit/d2993f4))

### 2015-11-29
 - Update django to 1.8.7 [security release] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/1efe6f2))

### 2015-11-17
 - refractor(email/smtp): switch to mailgun as SMTP server ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f3f9e60))

### 2015-11-09
 - chore(settings): use cache as sessions in production ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/0e63b50))
 - Upragde to django 1.8.6 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c0b8006))

### 2015-10-29
 - chore(deps): switch to stable version of mkdocs ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/cbffbd4))

### 2015-10-28
 - feat(app/users): add custom user model with email as USERNAME_FIELD ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/862ad9e))
 - chore(docs): remove the mention of the fact that sass is required ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/83e1a08))

### 2015-10-26
 - Revert use of pytest-pythonpath as it's required while working with venv ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6cfe98b))

### 2015-10-25
 - Make use of pytest-cov plugin for running coverage reports ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/92c2a50))
 - Use version 9.4 of postgres to run the test on travis ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fe62d1e))
 - Replace `pytest-ipdb` with `pdbpp` as suggested by `pytest-ipdb` ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/dce4466))
 - Remove `pytest-pythonpath` from dependency as it's not longer needed. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/046b58d))

### 2015-10-21
 - chore(testing): use new setup to run tests ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/10c1a14))
 - chore: Update readme to me it little concise ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/51c3e5f))
 - Add stub for release 1.1.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0e49d39))
 - Prepare for release 1.0.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7d2b017))

### 2015-10-20
 - Fix fabfile, restart server only when running task on remote server ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7db2e41))
 - feat(base/models): add image mixin to base models ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/b734d88))
 - fix(exceptions): drf exception handler needs to accept two variables ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/cd0042b))
 - Remove unsed unicode slugification ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2303255))

### 2015-10-15
 - Make the migration succeed everytime from CI deployment ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9c820d1))
 - docs(): update travis status badge ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/68bcab4))

### 2015-10-13
 - fix(provisioner): separate configure and deploy process ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/929c69d))

### 2015-10-12
 - fix(settings/boto): switch to default AWS_S3_CALLING_FORMAT ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/973fc63))
 - chore(styles): add rules for html,css,scss,json files ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e48f255))
 - chore(testing): update testing setup and minor doc beautification ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/deb3541))
 - chore(requirements): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/25e35a4))
 - chroe(settings/docs): minor update to template config ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e19e52a))
 - fix(ansible/celery): improvise overall celery role ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d37995a))

### 2015-10-09
 - fix(ansible): add production host and how to setup doc ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2664dbf))
 - Add syntax check for ansible script on travis CI ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fe55606))

### 2015-10-08
 - fix(docs): remove reference to 'backend/db.md' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4d37d7a))
 - Update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d6b7064))
 - feat(setttings): use new/updated template configuration ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d461402))

### 2015-10-06
 - refractor(pytest): cleanup factoryboy code which is now fixed in main lib ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7e5fe04))

### 2015-10-01
 - refractor(cookie): Use better cookiecutter context variables ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d5196d7))

### 2015-09-22
 - chore(deps): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0c9e661))

### 2015-08-21
 - feat(tests): upgrade test runner to `pytest` ([Aniket Maithani](https://github.com/Fueled/django-init/commit/6212264))
 - chore(deps): update requirements to latest stable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/96c00a5))
 - fix(fabfile): activate virtualenv before executing docs related fab commands ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/1498cc9))

### 2015-08-20
 - fix(gitignore): ignore vim and virtualenv files ([Karambir Singh Nain](https://github.com/Fueled/django-init/commit/63666bc))
 - chore(docs/heroku): make SITE_* more predictable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/24d8327))
 - fix(docs/heroku): update the install instruction for newrelic ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/47b60df))
 - chore(docs/heroku): no need to specify buildpack python now, it will detected automatically ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3b9492d))
 - chore(travis): Use simplified pip install command ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2e1e617))
 - fix(nginx): remove worker_connections from root directive ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3b55a12))

### 2015-08-19
 - Upgrade django to 1.8.4 [security release] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/09dbce9))

### 2015-08-12
 - feat(cache): switch to django_cache as cache backend. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/62ad3e6))

### 2015-08-06
 - chore(deps): upgrade dependencies to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ad6089f))

### 2015-07-12
 - chore(dep): mock and gevent to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/43b4df4))
 - security(dep): upgrade django to 1.8.3 (Security Release) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e07ff2a))

### 2015-07-08
 - chore(setup): update requirements to latest ([Aniket Maithani](https://github.com/Fueled/django-init/commit/b4c6e64))

### 2015-06-25
 - chore(deps): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8d9893a))

### 2015-06-17
 - feat(scafold): bumpversion 0.1.0-dev to indicate that current code is dev version ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6692180))

### 2015-06-15
 - feat(heroku): add monitoring for cache and queues via RedisMonitor ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2748bc9))

### 2015-06-11
 - fix(docs): typo corrected ([Aniket Maithani](https://github.com/Fueled/django-init/commit/dfe5b67))

### 2015-06-10
 - fix(mkdocs): remove /docs/db.md ([Aniket Maithani](https://github.com/Fueled/django-init/commit/01e1121))

### 2015-06-09
 - fix(mkdocs): remove urlize  - removed urlize as it was not working properly and was throwing config error ([Aniket Maithani](https://github.com/Fueled/django-init/commit/88ff568))
 - chore(deps): upgrade to Pillow==2.8.2 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/130b95e))
 - refactor(docs):removed pygraphviz support ([Aniket Maithani](https://github.com/Fueled/django-init/commit/7ee4def))

### 2015-05-23
 - feat(deps): upgrade to django==1.8.2 [security release] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6ef4728))

### 2015-05-22
 - chore(compat): make use of 'from __future__ import absolute_import' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3aa18c1))

### 2015-05-21
 - feat(settings/production): adding S3 media upload optional ([Aniket Maithani](https://github.com/Fueled/django-init/commit/7e36853))

### 2015-05-20
 - chore(docs/setup): update depreciated 'addons:add' command to 'addons:create' ([Aniket Maithani](https://github.com/Fueled/django-init/commit/64986dd))
 - chore(setup): make 'manage.py' executable for easy access via cli ([Aniket Maithani](https://github.com/Fueled/django-init/commit/cb9492c))
 - fix(README): Correct the dcoumentation in `fab serve` command ([aniketmaithani](https://github.com/Fueled/django-init/commit/ebceb87))

### 2015-05-19
 - fix(dotenv): do not reload of .env file twice ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e630233))
 - chore(flake8): fix flake8 issue in settings/testing.py ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/80ff5c9))

### 2015-05-18
 - fix(static): rename 'project.css' to 'main.css' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e246071))
 - chore(templates): make templates translation friendly ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8acc679))

### 2015-05-17
 - chore(templates/errors): make the structure consistent ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e64523c))
 - fix(template/404): use secure protocal and make the page i18n friendly ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c038bf6))
 - chore(pages): add appropriate title to about/home page ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/87e3560))
 - fix(views/500): handle the case where 500 might not be due to an exception ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/1c1750e))
 - refractor(root_files): organize/route `robots.txt`, `humans.txt`, etc. in better way ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6617565))
 - chore(pages): add better support for body_classes ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/13fbeb8))
 - feat(frontend): apply a natural box model to all elements ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/601b66b))
 - feat(frontend): Add normalize.css as per html5boilerplate ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4c9bbe3))

### 2015-05-14
 - Add support for 'flat' django admin theme ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/bd0bb46))
 - Update all the dependency to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6437739))
 - chore(config): update the source url of django_sites ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/5ee9b4e))
 - fix(settings): remove the sites config from common.py ([aniketmaithani](https://github.com/Fueled/django-init/commit/282bbc1))
 - fix(frontend_setup): deleted un-necessary files ([aniketmaithani](https://github.com/Fueled/django-init/commit/be3ff8d))

### 2015-05-13
 - chore(docs): update 'pages' config of mkdocs as per latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a93ec2c))
 - chore(docs): remove unused 'theme_center_lead' config [ci-skip] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4764911))

### 2015-05-09
 - chore(urls): cleanup urlpattern, use of 'pattern' is optional now ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d458240))

### 2015-05-05
 - refractor(grunt): removed grunt support ([aniket@fueled.co](https://github.com/Fueled/django-init/commit/f41a804))
 - chore(docs): update features list to latest [ci skip] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a09bc28))

### 2015-05-02
 - feat(django/core): replace core of UUIDModel to use native postgres UUID ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fe0b3e7))
 - Upgrade django-versatileimagefield to 0.6.2 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9cfc61a))
 - Upgrade to django 1.8.1 (Bugfix release) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/31ebf30))

### 2015-04-29
 - fix(requirements): move whitenoise to common, required for runserver ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/30ca556))

### 2015-04-28
 - refractor(apps): move static to apps_dir level ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/af23c0f))
 - fix(heroku): add missing DJANGO_SETTINGS_MODULE variable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/38dc80e))
 - chore(heroku): update deploy instructions to use ssh-git ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/5f75fc5))
 - feat(settings): Replace django-configuration with django-environ ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/5ecaa44))
 - chore(editorconfig): add rules for *.md and Makefile ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e0261f8))
 - fix(heroku): update deploy instruction for pg:backups and manage.py check ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3778314))
 - feat(mkdocs): Add support for site_author meta ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b71118b))
 - feat(mkdocs): github issue linking is now available site wide ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4644741))
 - feat(mkdocs): Make sure that all the pages have a menu item ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8e399e7))
 - feat(mkdocs): enable 'smarty' and 'sane_lists' markdown extensions ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e95670c))
 - feat(mkdocs): Use dev_addr to serve at 8001 instead of fabfile cmd ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d2c79a5))

### 2015-04-24
 - feat(cookie/setup): add option to automagically setup project or not ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/128ecd4))

### 2015-04-23
 - Remove support for any specific css/js framework ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/432ea14))
 - feat(docs): add support for UML: sequence diagram ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9e977be))

### 2015-04-22
 - feat(security/nginx): add proper security headers ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/555b494))

### 2015-04-14
 - feat(drf/throttling): add basic throttling for anonymous requests 10000/day/IP ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c755208))
 - feat(template/base): use dynamic "LANGUAGE_CODE", better internationalization ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/37c534b))

### 2015-04-13
 - docs(readme): simplify docs a bit [skip ci] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/548e67f))
 - Add locale_path to settings, to help facilitate translation when required ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2a9e868))
 - Add the "LANGUAGES" django setting explicitly ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/de62ded))
 - style(imports): apply isort on /settings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/99614ff))
 - Removed celery settings, as it's hardly used. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/957cf5f))

### 2015-04-11
 - Add changelog file ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a3daf2f))
 - chore(deps): swap to django-storages-redux, an py3 compatible fork ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/813f095))

### 2015-04-09
 - Add url for the release diff compare ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/306a826))
 - feat(docs): add third party services/products requirements [ci skip] ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/70635c9))
 - Update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/15d96e4))

### 2015-04-06
 - chore(deps): upgrade pillow to 2.8.1 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8f0ed91))

### 2015-03-29
 - fix(base/models): correct the import path ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/13ea426))

### 2015-03-26
 - feat(API): add api versioning support via Accept headers ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/03f704b))

### 2015-03-24
 - chore(deps): update requirements ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/32012d8))

### 2015-03-17
 - feat(deps): upgrade to django rest framework 3.1.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0ea839e))
 - fix(settings): update order of 'collectfast' in Installed apps. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/914c217))
 - fix(tests): update the cookiecutter interface as per latest cookiecutter ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f3b62ec))

### 2015-03-10
 - refractor(settings): make setting more logically organized. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4529288))
 - chore(deps): upgrade to django 1.7.6 (security release) ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/dcd1a47))

### 2015-03-03
 - chore(deps): upgrade ipython to 3.0.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e1f5fd3))

### 2015-02-27
 - chore(settings): make sure django-secure middleware is only in prod ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6a31a6b))
 - chore(deps): update django 1.7.4 -> 1.7.5 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/10ab297))

### 2015-02-26
 - chore(api/errors): make the unhandled exception response consistent. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/77b9349))

### 2015-02-25
 - chore(): update django-versatileimagefield 0.5.2->0.5.3 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a23d1f0))

### 2015-02-24
 - chore(): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c57c63b))
 - add link to wiki ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3048782))
 - chore(docs): mention how to activate virtualenv ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fd1b508))
 - chore(docs): mention that UUIDModel is supported ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8794f86))
 - refractor(): move project level templates at main templates folder ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/48cbcf5))
 - chore(docs): update readme with latest features ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7db55b4))

### 2015-02-23
 - feat(docs): add api error format with documentation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e21f541))
 - fix(fab/test): add 'capture=no' option to 'py.test' with 'ipdb' option ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3d066e7))

### 2015-02-19
 - fix(wsgi): make sure the get_wsgi_application is below env getter ([Saurabh](https://github.com/Fueled/django-init/commit/d6531a9))
 - fix(Procfile): make sure only one worker is populated ([Saurabh](https://github.com/Fueled/django-init/commit/96851b7))

### 2015-02-17
 - feat(base): add base timestamped UUID model ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/f24a46e))
 - feat(setup): add iSort configuration ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a2c679a))

### 2015-02-13
 - feat(docs/mkdocs): add 'urlize' markdown extension ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/47fdd40))
 - chore(docs): update initial copy of `release_notes.md` ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/28eb54a))
 - chore(setup): hard code SECRET_KEY for test setting ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/30d1880))
 - fix(flake8): fix the flake8 error produced in generates files ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0744394))
 - chore(requirements): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b18e4b2))

### 2015-02-12
 - fix(bumpversion): update config to include release status ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/89e810d))
 - chore(docs): add travis badge ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8c1a3b8))
 - chore(templating): initialize the repo with version 0.0.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/1ba7ad4))

### 2015-02-05
 - chore(): remove domain name ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/dfff56f))
 - chore(): prefer newrelic-admin as gunicorn spawner, remove middleware ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/be41cd7))
 - feat(new relic): add new relic support ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/5a6bdcf))

### 2015-02-03
 - keep on using '.bumpversion.cfg' until this PR[1] is fixed. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/16ae907))

### 2015-01-29
 - refractor(pytest): move settings from 'pytest.ini' to 'setup.cfg' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/021159d))
 - refractor(bumpversion): move settings from .bumpversion.cfg to setup.cfg ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c3fc02d))
 - chore(requirments): update to drf 3.0.4, django-versatileimagefield 0.5.1 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d6f3fd6))
 - fix(templating): remove use of `{{cookie cutter.domain_name}}` ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fa3bc2a))
 - update requirements - django 1.7.4, boto 2.36.0, unicode-slugify 0.1.3 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c4bdea4))

### 2015-01-24
 - chore(anisable/common): add `update-locale` command ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ca34202))

### 2015-01-16
 - chore(security): update django 1.7.2 -> 1.7.3 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3edebd4))

### 2015-01-14
 - feat(docs/release-notes): add release notes page with github issue autolink. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fa87785))

### 2015-01-12
 - chore(docs): fix typo in readme ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b40bb56))
 - chore(mkdocs): update copyright year to 2015 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/cb40d3e))

### 2015-01-10
 - fix(cookiecutter): fix the variable name ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9dedf78))
 - chore(): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ad91a8d))

### 2015-01-04
 - fix(settings): make it python2 compatible ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/08fd3ce))

### 2015-01-03
 - upgrade to django 1.7.2 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4e79c8c))

### 2015-01-02
 - chore(requirements): update to pillow 2.7.0 and DRF 3.0.2 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d2bcaa5))

### 2014-12-29
 - chore(requirements): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3ec5cf6))

### 2014-12-24
 - settings: add console and Null log handler ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/36c0236))
 - chore(docs/settings): update and make settings docs more readable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c2709b5))

### 2014-12-22
 - docs: update coding conventions ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/15b6d31))

### 2014-12-18
 - feat(cache): replace redis as cache backend ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/bd97a18))
 - api/docs: correct max page_size to 1000 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a4a62ad))
 - feat(travis): use container based infrastructure ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ebe3fd1))
 - chore(docs): add system level dev dependencies ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/995e903))
 - fix(fabric): make the fabric local command always use 'bash' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ca274aa))
 - feat(test): add test for checking generate errors ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ea42bd9))
 - update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7c6a120))

### 2014-12-13
 - chore(docs): remove 'ghp-import' lib in favor or 'mkdocs gh-deploy' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d7f9643))

### 2014-12-09
 - chore(docs): added a note for installing Graphiz ([Paul Oostenrijk](https://github.com/Fueled/django-init/commit/a160f25))

### 2014-12-05
 - feat(drf): updgrade django rest framework to 3.0.0 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a24a03a))
 - update python requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/031ffcd))
 - chore(grunt): update packages to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4532684))

### 2014-12-04
 - chore(docs): update readme ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b4e6e2c))
 - fix(s3): correct the value of 'AWS_S3_CALLING_FORMAT' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b4f810c))

### 2014-12-03
 - fix(config): use native os.environ instead of values.Value ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/56fe46b))
 - feat(apps): add base app with common re-usable code ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/00b3658))
 - refactor(docs): move server setup to docs/backend/server_config ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2035391))
 - fix(travis): correct path of manage.py for running migrations ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4331534))

### 2014-11-25
 - fix(heroku): fix wsgi path in Procfile ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d7d768b))
 - fix(travis): add postgres and add caching for PIP ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/1848848))

### 2014-11-24
 - chore(settings): add optimised settings for testing ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a69f1c2))
 - fix(fab/test): fix params to coverage ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c3395bd))
 - feat(model-util): add django-versatile image field ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ed9a45c))
 - feat(pages): add support for 'humans.txt' and 'robots.txt' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b6b44f9))
 - fix(bumpversion): update locations of version ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/aa269f7))
 - refactor(pages): move main templates and static into pages app. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/909fb53))

### 2014-11-21
 - refrator(settings): move `{{repo_name}}/{{repo_name}}/config` to `{{repo_name}}/settings` ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7a7db15))
 - fix(requirements): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/87236a4))

### 2014-11-20
 - fix(test): add missing __init__.py ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/1b00a85))
 - fix(fabfile): add mixing create_graph_model function ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fe09591))
 - fix(requirement): resolve the conflict of markdown with mkdocs ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e56c997))
 - chore(): fix merge ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d2d93ab))
 - feat(docs): generate model graph as part of doc build process ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c47c49a))
 - fix(ansible): cleanup and fixes, view full commit for details. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7b76934))
 - fix(wigs): move wsgi.py to manage.py’s location ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/fd5c5e6))
 - fix(config): register ‘rest_framework’ ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/b687116))
 - fix(urls): fix urls to use router.py ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/9815d16))
 - fix(config): fix wsgi settings ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/e899331))
 - fix(config): add missing import ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/fe9132d))

### 2014-11-17
 - fix(travis): update the deploy strategy to 'api' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c53503f))
 - fix(docs): update image url for database diagram ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ce1ded0))
 - minor cleanup and updates ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b1d8890))
 - chore(versioning/docs): include ‘index.md’ under bumpversion. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b5a4ca7))
 - feat(docs): add github_url and copyright info ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0127e12))
 - chore(project/versioning): add __version_info__ ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/811172c))
 - add check for 'manage.py test' ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6a331cc))

### 2014-11-13
 - refactor(manage.py): move 'manage.py' to project root folder ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3ca7d6b))
 - fix(travis): use email notifications instead of hipchat ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/1f19417))
 - chore(docs): add default documentation and structure ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4af2019))
 - feat(tests): add py.test and coverage ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/733e21f))
 - feat(versioning): add bumpversion for applying version and tags. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/697efc6))

### 2014-11-06
 - feat(django/app): replace django.contrib.sites with django_sites. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/07d6839))
 - chore(deps): update dependecies to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/004ed64))

### 2014-10-07
 - fix(editorconfig): don't trim trailing whitespace for *.md ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/00742ec))
 - fix(travis): enable postgres test setttings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/11db332))
 - feat(requirement): add pytz add default ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f4419db))
 - fix(settings): fix import in manage.py for heroku ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3fa9f1f))
 - fix(settings): fix import error in wsgi.py ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a10eef4))
 - fix(deploy): fix deploy instructions on readme ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2fcb0f4))

### 2014-10-06
 - feat(DRF): add base settings for django-rest-framework ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/262a907))

### 2014-10-02
 - style(PEP): fix PEP8 issues ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ee68088))
 - fix(readme): correct typo of cookie variable ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c04e3dd))
 - fix(cookie): fix variable name ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4b59a2e))
 - style(ansible): lets have pip in ‘requirements’ and ansible in ‘provisioner’ ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b914df9))
 - fix(travis): add missing quotes on post deploy script ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3556664))
 - fix(config): read database config only in common.py ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d0f54b5))
 - feat(flake): add sane defaults for flake8 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c37228a))
 - chore(docs): update docs to reflect the latest config ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/70dd0f1))
 - fix(foundation): prevent jinja from alterning the output ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2e5e335))
 - fix(celery): install celery setting only if required ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f2a4c23))
 - feat(foundation): foundation is now 5.4.1 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/75db8c5))
 - fix(fab): fix string formating typo ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/540c471))
 - feat(hooks): add pre/post hooks ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e12c3b2))

### 2014-10-01
 - feat(fab): update the commands to work with virtualenv ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/94bdee2))
 - chore(): minor formating ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4fde56c))
 - chore(fab): clean up the python-dotenv settings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d8bdee1))
 - feat(celery): add celery settings to settings module ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/4b08044))
 - fix(celery): fix celery settings ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/e361c9a))
 - fix(celery): move celery to correct location ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/a1f0203))

### 2014-09-22
 - feat(packages): add ipdb and django-uuid-upload-path ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/86ae5f7))
 - chore(packages): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/1c88c78))
 - feat(dj/upgrade): upgrade django to 1.7 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0260379))

### 2014-09-16
 - feat(CI): add travis file ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f354b82))
 - chore(cleanup): remove section on approved libraries and git breaching ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8e2f35e))
 - chore(cleanup): these are set using .env file now ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0a7f591))

### 2014-09-12
 - fix(security): Enable force-ssl on heroku. ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/48434b3))

### 2014-09-04
 - chore(read): add ref for DJ-Database-URL format ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/31bbf77))
 - refactor(readme): change order of steps ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/d81bcbb))
 - chore(readme/fab): update readme and fabfile ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/3ce36b0))
 - feat(configurations): move environment configuration to django-dotenv-rw ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/a2bd48a))

### 2014-09-03
 - feat(guidelines): add contributing.md a/c to github convention ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/036e6d3))

### 2014-09-02
 - fix(requirements): update them to latest version ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/38f3743))

### 2014-08-31
 - style(urls): supress pep8 warning ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/2bb4992))
 - feat(fab): add startapp command ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/6230c40))
 - fix(config): fix import of settings in manage.py ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4dc599d))
 - fix(config/celery): fix import issue for celery ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4328b3d))

### 2014-08-27
 - fix(configuration): syntax changes ([Your Name](https://github.com/Fueled/django-init/commit/6169e07))

### 2014-08-19
 - fix(configurations): fix typo in pip production ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/afce73a))

### 2014-08-14
 - fix(configurations): added repo version to ‘git’ role ([Vikrant Pogula](https://github.com/Fueled/django-init/commit/1d11412))

### 2014-08-12
 - chore(docs): add fueled attribution ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/11476da))

### 2014-07-28
 - fix(configurations): fix typo in template ([Vikrant Pogula](https://github.com/Fueled/django-init/commit/65fae92))

### 2014-07-22
 - fix(configuration): make use of ‘domain_name’ comprehensive ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3ce4ba9))
 - fix(configurations): added ansible support to supporting files ([Vikrant Pogula](https://github.com/Fueled/django-init/commit/0c2cd6e))
 - fix(configurations): added to allow j2 templates for ansible ([Vikrant Pogula](https://github.com/Fueled/django-init/commit/c9cc9e6))
 - fix(configurations): added ansible variable for domain_name ([Vikrant Pogula](https://github.com/Fueled/django-init/commit/d683563))
 - fix(ansible): use {{ celery_app }} in celery task instead ([Saurabh](https://github.com/Fueled/django-init/commit/20fff08))

### 2014-07-21
 - feat(ansible): added various ansible roles ([Vikrant Pogula](https://github.com/Fueled/django-init/commit/634e541))

### 2014-06-13
 - update documentation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/839d5d9))
 - fix(docs): update documentation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/cc1783e))
 - fix(fabric): fabric can now be run from project subdirectory ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ce53924))
 - fix(favicon): use self hosted version of favicon ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/569492d))
 - feat(fronted): add browsehappy for IE < 8 ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/0659121))
 - feat(dev_server): use `runserver_plus` for `run server` ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c9a84e4))
 - chore(requirements): update to latest version ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a4c7ff0))
 - chore(error_pages): update 400, 403, 404 & 500 pages ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/afce549))
 - refactor(config): use differnt file for develop/production settings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/817b394))

### 2014-05-25
 - fix(settings): fix depreciation warning of dj Debug toolbar ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b7d53b5))
 - fix(docs): update heroku deploy instructions ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/e8092da))
 - fix - unable debug in development settings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8619cda))
 - feat(command): add 'fab shell' command ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/5f642ed))
 - update settings file ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/d249b6b))

### 2014-05-24
 - chore(dependency): update dependencies to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/fb13bb7))
 - fix(docs): fix template variable name ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a8c0eeb))
 - chore(): fix typos ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/8cb29d8))
 - fix(cookiecutter): fix jinja conflicts ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3369b24))
 - chore(docs): update documentation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/13faffa))

### 2014-05-04
 - feat(docs): add django versatile Image field ([Saurabh](https://github.com/Fueled/django-init/commit/4708e03))

### 2014-04-25
 - chore(requirements): update requirements to latest ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/4dfdc41))

### 2014-04-22
 - chore(docs): add list of approved libraries ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3388bbd))

### 2014-03-26
 - feat(sass): added foundation scss style files files ([Vikrant Pogula | Fueled](https://github.com/Fueled/django-init/commit/03550a4))

### 2014-03-19
 - feat(Favicon): fixes the favicon 404 error ([Saurabh](https://github.com/Fueled/django-init/commit/82081e8))
 - fix(grunt): add gruntfile.coffee to watch dir ([Saurabh](https://github.com/Fueled/django-init/commit/7f22ca2))

### 2014-03-10
 - fix(settings): fix dependencies + fix settings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/3853e10))
 - fix(pages): fix urls of pages app and urls ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f77129b))

### 2014-03-08
 - refactor(grunt): use coffeescript instead of js ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/77b6ce3))

### 2014-03-04
 - feat(config): add django setup configuration ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/16395f6))
 - feat(config): add postgessql database ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/61596b3))
 - chore(docs): updates docs and variables name ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c1c0786))
 - refractor(config): make pip configs map directly to django settings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/a92f2d7))
 - feat(settings): add pages app and proper settings ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/34e8553))
 - refactor(vagrant): share the folder as project_name ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/c1df80b))
 - feat(heroku): add Procfile ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/b124327))
 - feat(frontend): add grunt task runner ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9f2aca8))
 - feat(app): add core & config django apps ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/454543b))
 - feat(template): add default 404/500 pages ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/9f06b14))
 - fix(vagrant): can't use `.1` in IP address, fixit! ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/ef77918))
 - feat(docs): add mkdocs for writing documentation ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/dd545fd))

### 2014-03-03
 - feat(vagrant): add basic vagrantbox setup config ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f58d003))
 - chore(doc): how to scafold a new project ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/7e29830))
 - feat(init): add base file for cookiecutter ([Saurabh Kumar](https://github.com/Fueled/django-init/commit/f36e71a))
