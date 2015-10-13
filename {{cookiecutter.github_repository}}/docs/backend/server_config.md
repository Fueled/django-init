# Server Architecture and configurations

```sequence
title: Client Server Interactions
iOS/\nClient->Web\nServer: API Request
Web\nServer-->Redis: Cache
Redis-->Web\nServer: 
Web\nServer->Postgres: Persistent Storage
Postgres->Web\nServer: 
Web\nServer-->Redis: Update cache
Web\nServer-->SMTP: Enqueue emails
Web\nServer->iOS/\nClient: API Response
SMTP->iOS/\nClient: Email
Note over Web\nServer: Django Framework
```

# Third Party Services

Following third-party services are required in order to setup/deploy this project successfully.

## Heroku

Heroku is platform as a service provider. We use to host the primarily web server along with different services required by this project like postgres database, newrelic, redis. See getting started docs [here][heroku-docs], you'll require to create an account and install the [cli-tool][heroku-cli] to successfully deploy this project.

[heroku-docs]: https://devcenter.heroku.com/
[heroku-cli]: https://devcenter.heroku.com/articles/heroku-command

Note: Alternatively, you should be able configure a linux instance to run the same project as well, heroku like settings can be added via `.env` file. (refer: `settings/common.py`). Just that, this documentation and project is focused more with Heroku as platform of choice.

## Amazon S3

Amazon Simple Storage Service ([Amazon S3]) is used to store the uploaded media files and static content. It is a scalable and cost-efficient storage solution. 

After [signing up][s3-signup] for Amazon S3, [setup][s3-iam-setup] an IAM user with access to a S3 bucket, you'll need `BUCKET_NAME`, and `AWS_ACCESS_ID` & `AWS_ACCESS_SECRET` of IAM user to setup the project.

[Amazon S3]: http://aws.amazon.com/s3/
[s3-signup]: http://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html
[s3-iam-setup]: https://rbgeek.wordpress.com/2014/07/18/amazon-iam-user-creation-for-single-s3-bucket-access/

Note: 
- Heroku doesn't provide a persistent storage for uploaded content, best practise is to store the uploaded files in S3 buckets.
- IAM user must have permission to list, update, create objects in S3.

# Deploying Project

The deployment are managed via travis, but for the first time you'll need to set the configuration values on each of the server. Read this only, if you need to deploy for the first time.

### Heroku

Run these commands to deploy a new project to Heroku:

```
heroku create --ssh-git <heroku-app-name>

heroku addons:create heroku-postgresql --app=<heroku-app-name>
heroku pg:backups schedule DATABASE_URL --at '04:00 UTC' --app=<heroku-app-name>
heroku pg:promote DATABASE_URL --app=<heroku-app-name>

heroku addons:create sendgrid:starter --app=<heroku-app-name>

heroku addons:create redistogo --app=<heroku-app-name>
heroku addons:create redismonitor --url `heroku config:get REDISTOGO_URL --app=<heroku-app-name>` --app=<heroku-app-name>

{% if cookiecutter.newrelic == 'y' -%}
heroku addons:create newrelic --app=<heroku-app-name>
heroku config:set NEW_RELIC_APP_NAME=<new-relic-app-name> --app=<heroku-app-name>
{%- endif %}

heroku config:set DJANGO_SETTINGS_MODULE='settings.production' \
DJANGO_SECRET_KEY=`openssl rand -base64 32` \
SITE_DOMAIN=<heroku-app-name>.herokuapp.com \
SITE_SCHEME=https \
SITE_NAME=DJANGO_SITE_NAME_HERE --app=<heroku-app-name>

git push heroku master
heroku run python manage.py migrate --app=<heroku-app-name>
heroku run python manage.py check --deploy --app=<heroku-app-name>
heroku run python manage.py createsuperuser --app=<heroku-app-name>
heroku open --app=<heroku-app-name>
```

The following configuration doesn't allow you to "by default" upload the media on the heroku server as heroku does
not support persistent storage. We use S3 for storing uploaded media. If you want to enable media upload:

- Create S3 bucket and get AWS access key and secret that has access to this bucket.
- Follow the instructions below to enable S3 upload configuration on heroku.

```
heroku config:set ENABLE_MEDIA_UPLOAD_TO_S3=true \
DJANGO_AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_ID_HERE> \
DJANGO_AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_KEY_HERE> \
DJANGO_AWS_STORAGE_BUCKET_NAME=<YOUR_BUCKET_NAME_HERE>
```


**Note:**
- Use `--app=<heroku-app-name>` if you have more than one heroku app configured in current project.
- Update `travis.yml`, and add the `<heroku-app-name>` to automatically deploy to this configured heroku app.

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

    fab prod configure

This will setup os dependencies, services like supervisor, nginx and fetch our code from github. Our production environment requires 
some environment variables in `.env`. So you can write a file `prod.env` locally and upload it to server with

    scp prod.env {{ cookiecutter.main_module }}.com:/home/ubuntu/{{ cookiecutter.github_repository }}/.env

You can also use fab to set environment variables one by one:

    fab prod config:set,<VAR_NAME>,<VAR_VALUE>

Now that you have `.env` setup, you can deploy your code and start services:

    fab prod deploy
