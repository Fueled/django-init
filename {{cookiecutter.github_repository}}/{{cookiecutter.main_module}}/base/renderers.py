from rest_framework.renderers import JSONRenderer


class {{ cookicutter.main_module.title() }}ApiRenderer(JSONRenderer):
    media_type = 'application/vnd.{{ cookicutter.main_module }}-com+json'