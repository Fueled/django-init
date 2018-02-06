{% raw %}{% extends "mail_templated/base.tpl" %}
{% load i18n %}
{% load resolve_frontend_url from urls_extra %}

{# ======== Subject of email #}
{% block subject %}Reset your Password!{% endblock %}

{% block body %}
{# ======== plain text version of email body #}
{% blocktrans %}You're receiving this email because you requested a password reset
for your user account.{% endblocktrans %}

{% trans "Please go to the following page and choose a new password:" %}

{% resolve_frontend_url password-confirm token=token %}

{% trans "Thanks for using our site!" %}
{% endblock body %}


{% block html %}
{# ======== html version of email body #}
<p>{% blocktrans %}You're receiving this email because you requested a password reset
for your user account.{% endblocktrans %}</p>

<p>{% trans "Please go to the following page and choose a new password:" %}
<a href="{% resolve_frontend_url password-confirm token=token %}">{% trans "Reset Password" %}</a>
</p>

<p>{% trans "Thanks for using our site!" %}</p>
{% endblock html %}{% endraw %}
