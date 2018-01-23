{% raw %}
{% extends "mail_templated/base.tpl" %}
{% load i18n %}

{% block subject %}
Reset your {{ site.name }} Password!
{% endblock %}

{% block body %}

{% blocktrans %}You're receiving this email because you requested a password reset
for your user account.{% endblocktrans %}

{% trans "Please go to the following page and choose a new password:" %}
{% block reset_link %}
{{ password_reset_url }}
{% endblock %}

{% trans "Thanks for using our site!" %}

- {{ site.name }}

{% endblock %}

{% block html %}

{% blocktrans %}You're receiving this email because you requested a password reset
for your user account.{% endblocktrans %}

{% trans "Please go to the following page and choose a new password:" %}

<a href="{{ password_reset_url }}">Reset Password</a>

{% trans "Thanks for using our site!" %}

- {{ site.name }}

{% endblock %}
{% endraw %}
