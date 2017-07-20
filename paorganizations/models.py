# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from pautils.models import Published


class Organization(TimeStampedModel, Published):
    """Organizzazione"""
    title = models.CharField(_('title'), max_length=500, unique=True)
    email_domain = models.CharField(_('email domain'), max_length=100,
                                    unique=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name=_('parent organization'))
    filter_label = models.CharField(_('filter label'), max_length=20,
                                    blank=True)
    email_background_color = models.CharField(max_length=20,
                                              default='lightskyblue',
                                              blank=True)

    def __str__(self):
        return self.title


class Building(TimeStampedModel, Published):
    """Sede"""
    title = models.CharField(_('title'), max_length=200, unique=True)
    organization = models.ForeignKey(Organization,
                                     verbose_name=_('organization'))
    verbose_address = models.TextField(_('Verbose address'), blank=True)

    class Meta:
        verbose_name = _('building')
        verbose_name_plural = _('buildings')

    def __str__(self):
        return '{}'.format(self.title)


class Person(TimeStampedModel, Published):
    """Persona"""
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True,
                                 null=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    email = models.EmailField(_('email address'), blank=True)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Office(TimeStampedModel, Published):
    """Ufficio"""
    title = models.CharField(_('title'), max_length=200, unique=True)
    organization = models.ForeignKey(Organization,
                                     verbose_name=_('organization'))
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name=_('parent organization'))
    components = models.ManyToManyField(Person, blank=True,
                                        verbose_name=_('components'))

    class Meta:
        verbose_name = _('office')
        verbose_name_plural = _('offices')

    def __str__(self):
        return '{}'.format(self.title)


