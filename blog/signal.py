from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify as django_slugify

from .models import Article


@receiver(pre_save, sender=Article)
def validate_slug_name(sender, instance: Article, **kwargs):
    instance.slug = django_slugify(instance.title)
