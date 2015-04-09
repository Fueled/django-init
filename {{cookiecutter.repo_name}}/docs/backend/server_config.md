# Server Architecture and configurations

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
heroku create <heroku-app-name> --buildpack https://github.com/heroku/heroku-buildpack-python
heroku addons:add heroku-postgresql:dev --app=<heroku-app-name>
heroku addons:add pgbackups:auto-month --app=<heroku-app-name>
heroku addons:add sendgrid:starter --app=<heroku-app-name>
heroku addons:add redistogo --app=<heroku-app-name>
{% if cookiecutter.newrelic == 'y' %}
heroku addons:add newrelic:stark --app=<heroku-app-name>
heroku config:set NEW_RELIC_APP_NAME=<new-relic-app-name> --app=<heroku-app-name>
{% endif %}
heroku pg:promote DATABASE_URL --app=<heroku-app-name>
heroku config:set DJANGO_CONFIGURATION=Production \
DJANGO_SECRET_KEY=`openssl rand -base64 32` \
DJANGO_AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_ID_HERE \
DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_KEY \
DJANGO_AWS_STORAGE_BUCKET_NAME=YOUR_BUCKET_NAME \
SITE_DOMAIN=DJANGO_SITE_DOMAIN_HERE \
SITE_SCHEME=DJANGO_SITE_SCHEME_HERE  \
SITE_NAME=DJANGO_SITE_NAME_HERE --app=<heroku-app-name>
git push heroku master --app=<heroku-app-name>
heroku run python manage.py migrate --app=<heroku-app-name>
heroku run python manage.py createsuperuser --app=<heroku-app-name>
heroku open --app=<heroku-app-name>
```

**Note:** 
- Use `--app=<heroku-app-name>` if you have more than one heroku app configured in current project.
- Update `travis.yml`, and add the `<heroku-app-name>` to automatically deploy to this configured heroku app.

### AWS/EC2

For deploying on aws you need to configure all the addons provided and use python-dotenv to store and read enironment variables. You should using the ansible script in `provisioner` to handle the configuration and deployment on remote servers.
