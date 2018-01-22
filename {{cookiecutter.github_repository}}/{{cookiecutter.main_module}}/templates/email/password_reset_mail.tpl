{% endraw %}
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
{{ frontend_domain }}/{{ url }}
{% endblock %}

{% trans "Thanks for using our site!" %}

- {{ site.name }}

{% endblock %}

{% block html %}

{% blocktrans %}You're receiving this email because you requested a password reset
for your user account.{% endblocktrans %}

{% trans "Please go to the following page and choose a new password:" %}

<a href="{{ frontend_domain }}/{{ url }}">Reset Password</a>

{% trans "Thanks for using our site!" %}

- {{ site.name }}

{% endblock %}
{% endraw %}
