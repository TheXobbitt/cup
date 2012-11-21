from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from center.models import Domain, Tariff

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    domains = models.ManyToManyField(Domain)
    tariff = models.ForeignKey(Tariff, null=True, blank=True)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
