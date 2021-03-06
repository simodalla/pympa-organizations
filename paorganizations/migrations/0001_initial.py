# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 13:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('published_from', models.DateTimeField(default=django.utils.timezone.now, verbose_name='published from')),
                ('published_to', models.DateTimeField(blank=True, null=True, verbose_name='published from')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='title')),
                ('verbose_address', models.TextField(blank=True, verbose_name='Verbose address')),
            ],
            options={
                'verbose_name_plural': 'buildings',
                'verbose_name': 'building',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('published_from', models.DateTimeField(default=django.utils.timezone.now, verbose_name='published from')),
                ('published_to', models.DateTimeField(blank=True, null=True, verbose_name='published from')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name_plural': 'offices',
                'verbose_name': 'office',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('published_from', models.DateTimeField(default=django.utils.timezone.now, verbose_name='published from')),
                ('published_to', models.DateTimeField(blank=True, null=True, verbose_name='published from')),
                ('title', models.CharField(max_length=500, unique=True, verbose_name='title')),
                ('email_domain', models.CharField(max_length=100, unique=True, verbose_name='email domain')),
                ('filter_label', models.CharField(blank=True, max_length=20, verbose_name='filter label')),
                ('email_background_color', models.CharField(blank=True, default='lightskyblue', max_length=20)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='paorganizations.Organization', verbose_name='parent organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('published_from', models.DateTimeField(default=django.utils.timezone.now, verbose_name='published from')),
                ('published_to', models.DateTimeField(blank=True, null=True, verbose_name='published from')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'people',
                'verbose_name': 'person',
            },
        ),
        migrations.AddField(
            model_name='office',
            name='components',
            field=models.ManyToManyField(blank=True, to='paorganizations.Person', verbose_name='components'),
        ),
        migrations.AddField(
            model_name='office',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paorganizations.Organization', verbose_name='organization'),
        ),
        migrations.AddField(
            model_name='office',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='paorganizations.Office', verbose_name='parent organization'),
        ),
        migrations.AddField(
            model_name='building',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paorganizations.Organization', verbose_name='organization'),
        ),
    ]
