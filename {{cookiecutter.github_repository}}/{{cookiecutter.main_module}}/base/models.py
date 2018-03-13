# Standard Library
import uuid

# Third Party Stuff
from django.db import models
from uuid_upload_path import upload_to
from versatileimagefield.fields import PPOIField, VersatileImageField


class UUIDModel(models.Model):
    """ An abstract base class model that makes primary key `id` as UUID
    instead of default auto incremented number.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(UUIDModel):
    """An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields with UUID as primary_key field.
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    """An abstract base class model that provides a VersatileImageField Image with POI
    """

    image = VersatileImageField(upload_to=upload_to, blank=True, null=True, ppoi_field='image_poi',
                                verbose_name="image")
    image_poi = PPOIField(verbose_name="image's Point of Interest")  # point of interest

    class Meta:
        abstract = True
