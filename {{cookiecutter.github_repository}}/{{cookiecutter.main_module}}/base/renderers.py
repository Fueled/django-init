from rest_framework.renderers import JSONRenderer


class {{ cookiecutter.main_module|replace('_', ' ')|replace('-', ' ')|title|replace(' ', '') }}ApiRenderer(JSONRenderer):
    media_type = 'application/vnd.{{ cookiecutter.main_module|replace('_', '')|replace('-', '') }}-com+json'
