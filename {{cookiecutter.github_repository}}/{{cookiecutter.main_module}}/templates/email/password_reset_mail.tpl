{% raw %}
{% extends "mail_templated/base.tpl" %}
{% load i18n %}
{% resolve_frontend_url from urls_extra %}


{% block subject %}
Reset your {{ site.name }} Password!
{% endblock %}

{% block body %}

{% blocktrans %}You're receiving this email because you requested a password reset
for your user account.{% endblocktrans %}

{% trans "Please go to the following page and choose a new password:" %}

{% resolve_frontend_url password-confirm token=token uuid=uuid %}

{% trans "Thanks for using our site!" %}

{% endblock %}

{% block html %}

{% blocktrans %}You're receiving this email because you requested a password reset
for your user account.{% endblocktrans %}

{% trans "Please go to the following page and choose a new password:" %}

<a href="{% resolve_frontend_url password-confirm token=token uuid=uuid %}">{% trans "Reset Password" %}</a>

{% trans "Thanks for using our site!" %}

{% endblock %}
{% endraw %}
