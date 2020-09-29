# Server Architecture and configurations

## Concepts

Our overall stack looks like this:

```
the web client <-> the web server (nginx) <-> the socket <-> uWSGI <-> Django
```

A web server faces the outside world. It can serve files (HTML, images, CSS, etc) directly from the file system. However, it can’t talk directly to Django applications; it needs something that will run the application, feed it requests from web clients (such as browsers) and return responses.

uWSGI is a [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) implementation, it creates a Unix socket, and serves responses to the web server via the uwsgi protocol.

## Third Party Services

Following third-party services are required in order to setup/deploy this project successfully.

{%- if cookiecutter.enable_heroku_deployment.lower() == 'y' %}
### Heroku

Heroku is platform as a service provider. We use to host the primarily web server along with different services required by this project like postgres database, newrelic, redis. See getting started docs [here][heroku-docs], you'll require to create an account and install the [cli-tool][heroku-cli] to successfully deploy this project.

[heroku-docs]: https://devcenter.heroku.com/
[heroku-cli]: https://devcenter.heroku.com/articles/heroku-command

Note: Alternatively, you should be able configure a linux instance to run the same project as well, heroku like settings can be added via `.env` file. (refer: `settings/common.py`). Just that, this documentation and project is focused more with Heroku as platform of choice.
{%- endif %}

### Amazon S3

Amazon Simple Storage Service ([Amazon S3]) is used to store the uploaded media files and static content. It is a scalable and cost-efficient storage solution. 

After [signing up][s3-signup] for Amazon S3, [setup][s3-iam-setup] an IAM user with access to a S3 bucket, you'll need `BUCKET_NAME`, and `AWS_ACCESS_ID` & `AWS_ACCESS_SECRET` of IAM user to setup the project.

[Amazon S3]: http://aws.amazon.com/s3/
[s3-signup]: http://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html
[s3-iam-setup]: https://rbgeek.wordpress.com/2014/07/18/amazon-iam-user-creation-for-single-s3-bucket-access/

Note: 
{% if cookiecutter.enable_heroku_deployment.lower() == 'y' %}
- Heroku doesn't provide a persistent storage for uploaded content, best practise is to store the uploaded files in S3 buckets.
{% endif %}
- IAM user must have permission to list, update, create objects in S3.

## Deploying Project

The deployment are managed via travis, but for the first time you'll need to set the configuration values on each of the server. Read this only, if you need to deploy for the first time.

{%- if cookiecutter.enable_heroku_deployment.lower() == 'y' %}
### Heroku

Run these commands to deploy this project on Heroku (substitue all references of `<heroku-app-name>` with the name your heroku application.)

```
heroku create --ssh-git <heroku-app-name>

heroku buildpacks:set heroku/python --app=<heroku-app-name>

{% if cookiecutter.postgis == 'y' %}heroku addons:create heroku-postgresql:standard-0 --app=<heroku-app-name>
{% else %}heroku addons:create heroku-postgresql --app=<heroku-app-name>{% endif %}
heroku pg:backups schedule DATABASE_URL --at '04:00 UTC' --app=<heroku-app-name>
heroku pg:promote DATABASE_URL --app=<heroku-app-name>

heroku addons:create mailgun --app=<heroku-app-name>
heroku config:set EMAIL_HOST="\$MAILGUN_SMTP_SERVER" \
                  EMAIL_HOST_USER="\$MAILGUN_SMTP_LOGIN" \
                  EMAIL_HOST_PASSWORD="\$MAILGUN_SMTP_PASSWORD" --app=<heroku-app-name>

heroku addons:create heroku-redis:hobby-dev --app=<heroku-app-name>
heroku addons:create redismonitor --url `heroku config:get REDIS_URL --app=<heroku-app-name>` --app=<heroku-app-name>

{% if cookiecutter.newrelic == 'y' -%}
heroku addons:create newrelic --app=<heroku-app-name>
heroku config:set NEW_RELIC_APP_NAME=<new-relic-app-name> --app=<heroku-app-name>
{%- endif %}

heroku config:set DJANGO_SETTINGS_MODULE='settings.production' \
DJANGO_SECRET_KEY=`openssl rand -hex 64` \
SITE_DOMAIN=<heroku-app-name>.herokuapp.com \
ALLOWED_HOSTS=<heroku-app-name>.herokuapp.com \
SITE_SCHEME=https \
SITE_NAME=DJANGO_SITE_NAME_HERE --app=<heroku-app-name>

heroku config:set DJANGO_ADMINS='webmaster@yourdomain.com' --app=<heroku-app-name>

git push heroku master
heroku run python manage.py createsuperuser --app=<heroku-app-name>
heroku open --app=<heroku-app-name>
```

The following configuration doesn't allow you to "by default" upload the media on the Heroku server as Heroku does not support persistent storage. We use S3 for storing uploaded media. If you want to enable media upload:

- Create S3 bucket and get AWS access key and secret that has access to this bucket.
- Follow the instructions below to enable S3 upload configuration on Heroku.

```
heroku config:set ENABLE_MEDIA_UPLOAD_TO_S3=true \
DJANGO_AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_ID_HERE> \
DJANGO_AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_KEY_HERE> \
DJANGO_AWS_STORAGE_BUCKET_NAME=<YOUR_BUCKET_NAME_HERE>
```


__Note:__
- Use `--app=<heroku-app-name>` if you have more than one Heroku app configured in current project.
- Update `travis.yml`, and add the `<heroku-app-name>` to automatically deploy to this configured Heroku app.
{% endif %}

{%- if cookiecutter.add_ansible.lower() == 'y' %}

{% if cookiecutter.add_django_auth_wall.lower() == 'y' -%}
### Protecting staging site with Basic Authentication

The project include [django-auth-wall](https://github.com/theskumar/django-auth-wall) which can be used to protect the site with Basic authentication during development. To enable the protection, add the following two variables in system environment or in django settings.

```
AUTH_WALL_USERNAME=<your_basic_auth_username_here>
AUTH_WALL_PASSWORD=<your_basic_auth_password_here>
AUTH_WALL_REALM=<your_basic_auth_message(optional)>
```
{%- endif %}

### AWS/EC2

For deploying on aws you need to configure all the addons provided and use python-dotenv to store and read enironment variables.

Add the following to your `~/.ssh/config` file.

```
Host {{ cookiecutter.main_module }}.com
    hostname <server_ip_or_>
    user ubuntu
    ForwardAgent yes
    identityfile <PATH_OF_SERVER_PRIVATE_KEY_HERE>
```

Add your github private key to your local ssh-agent, which will be used by ansible on remote server to fetch the code using `ForwardAgent`

    ssh-add <PATH_TO_YOUR_GITHUB_PRIVATE_KEY>

Now you can run the ansible script to setup the machine.

    make configure ENV=prod
    make configure ENV=staging

This will setup os dependencies, services like supervisor, nginx and fetch our code from Github. Our production environment requires 
some environment variables in `.env`. So you can write a file `prod.env` locally and upload it to server with

    scp prod.env {{ cookiecutter.main_module }}.com:/home/ubuntu/{{ cookiecutter.github_repository }}/.env

Now that you have `.env` setup, you can deploy your code and start services:

    make deploy ENV=prod
    make deploy ENV=staging
{% endif %}
