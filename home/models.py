# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    permissions  = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customers(models.Model):

    #__Customers_FIELDS__
    customer name = models.TextField(max_length=255, null=True, blank=True)
    customer number = models.CharField(max_length=255, null=True, blank=True)
    customer email = models.TextField(max_length=255, null=True, blank=True)
    company = models.TextField(max_length=255, null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)
    customer add date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Customers_FIELDS__END

    class Meta:
        verbose_name        = _("Customers")
        verbose_name_plural = _("Customers")


class Quotes(models.Model):

    #__Quotes_FIELDS__
    quote description = models.IntegerField(null=True, blank=True)
    attachments = models.TextField(max_length=255, null=True, blank=True)
    quote date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    quote status = models.TextField(max_length=255, null=True, blank=True)

    #__Quotes_FIELDS__END

    class Meta:
        verbose_name        = _("Quotes")
        verbose_name_plural = _("Quotes")



#__MODELS__END
