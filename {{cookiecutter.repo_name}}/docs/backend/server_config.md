## Deploying Project

The deployment are managed via travis, but for the first time you'll need to set the configuration values on each of the server. Read this only, if you need to deploy for the first time.

### Heroku

Run these commands to deploy a new project to Heroku:

```
TODO: add commands here..

```

### AWS/EC2

For deploying on aws you need to configure all the addons provided and use python-dotenv to store and read enironment variables. You should using the ansible script in `provisioner` to handle the configuration and deployment on remote servers.
