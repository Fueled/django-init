## Deploying Project

The deployment are managed via travis, but for the first time you'll need to set the configuration values on each of the server. Read this only, if you need to deploy for the first time.

### Heroku

Run these commands to deploy a new project to Heroku:

```
heroku create <heroku-app-name> --buildpack https://github.com/heroku/heroku-buildpack-python
heroku addons:add heroku-postgresql:dev --app=<heroku-app-name>
heroku addons:add pgbackups:auto-month --app=<heroku-app-name>
heroku addons:add sendgrid:starter --app=<heroku-app-name>
heroku addons:add memcachier:dev --app=<heroku-app-name>
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
