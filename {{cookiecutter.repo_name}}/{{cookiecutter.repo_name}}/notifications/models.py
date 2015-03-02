# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from {{ cookiecutter.repo_name }}.base.models import TimeStampedUUIDModel


class Device(TimeStampedUUIDModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, related_name='devices')
    token = models.CharField(max_length=255, db_index=True, unique=True)

    def __unicode__(self):
        return u"Device <Token: %s>" % self.token

