# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django_extensions.db.models import TimeStampedModel

from .fields import AutoUUIDField


class UUIDModel(models.Model):
    '''
    An abstract base class model that makes primary key `id` as UUID
    instead of default auto incremented number.
    '''
    id = AutoUUIDField(primary_key=True, editable=False, null=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        try:
            return self.name
        except AttributeError:
            if self.id is not None:
                return self.id
            else:
                return self.__class__.__name__+' object'


class TimeStampedUUIDModel(TimeStampedModel, UUIDModel):
    '''
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields with UUID as primary_key field.
    '''

    class Meta:
        abstract = True
