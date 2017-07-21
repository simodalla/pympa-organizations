# -*- coding: utf-8 -*-

import random

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.models import TimeStampedModel
from pautils.models import Published


class Organization(TimeStampedModel, Published):
    """Organizzazione"""
    title = models.CharField(_('title'), max_length=500)
    email_domain = models.CharField(_('email domain'), max_length=100,
                                    unique=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name=_('parent organization'))
    filter_label = models.CharField(_('filter label'), max_length=20,
                                    blank=True)
    email_background_color = models.CharField(max_length=20,
                                              default='lightskyblue',
                                              blank=True)

    class Meta:
        verbose_name = _('organization')
        verbose_name_plural = _('organizations')

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


class Place(TimeStampedModel):
    building = models.ForeignKey(Building, blank=True, null=True,
                                 verbose_name=_('building'))
    plane = models.CharField(_('room number'), blank=True, max_length=10)
    room_number = models.CharField(_('room number'), blank=True, max_length=10)


class Email(TimeStampedModel, Published):
    address = models.EmailField(_('email address'), blank=True)

    class Meta:
        verbose_name = _('email')
        verbose_name_plural = _('email')

    def __str__(self):
        return '{}'.format(self.address)


class TelephoneNumber(TimeStampedModel, Published):
    TYPES = Choices(('external', _('external')), ('internal', _('internal')),
                    ('mobile', _('mobile')), ('fax', _('fax')),)
    number = models.CharField(_('number'), max_length=30, blank=True)
    type = models.CharField(choices=TYPES, default=TYPES.external,
                            max_length=20)

    class Meta:
        verbose_name = _('telephone number')
        verbose_name_plural = _('telephone number')
        unique_together = ('number', 'type')

    def __str__(self):
        return '{}'.format(self.number)


class Person(TimeStampedModel, Published):
    """Persona"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    register_number = models.CharField(_('register number'), max_length=10,
                                       blank=True, unique=True)
    cdr_ab_id = models.CharField(_('register number'), max_length=20,
                                 blank=True)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if len(self.register_number) == 0:
            self.register_number = "_g_{}".format(
                random.randint(0, 9999999))
        super(Person, self).save(*args, **kwargs)


class Office(TimeStampedModel, Published):
    """Ufficio"""
    title = models.CharField(_('title'), max_length=200, unique=True)
    organization = models.ForeignKey(Organization,
                                     verbose_name=_('organization'))
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name=_('parent organization'))

    class Meta:
        verbose_name = _('office')
        verbose_name_plural = _('offices')

    def __str__(self):
        return '{}'.format(self.title)


class Assignment(TimeStampedModel, Published):
    """Assegnazione"""
    organization = models.ForeignKey(Organization,
                                     verbose_name=_('organization'))
    person = models.ForeignKey(Person, verbose_name=_('person'))
    email = models.ForeignKey(Email, blank=True, null=True,
                              verbose_name=_('email'))
    telephone_numbers = models.ManyToManyField(TelephoneNumber, blank=True,
                                               verbose_name=_(
                                                   'telephone numbers'))
    notes = models.TextField(_('notes'), blank=True)
    office = models.ForeignKey(Office, blank=True, null=True,
                               verbose_name=_('office'))
    # buildings = models.ManyToManyField(Building, blank=True, null=True,
    #                                    verbose_name=_('buildingss'))


    class Meta:
        verbose_name = _('assignment')
        verbose_name_plural = _('assignments')

    def __str__(self):
        return '{} {}'.format(self.organization, self.person)




