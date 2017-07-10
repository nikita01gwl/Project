# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='riders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\+?([0,7,8,9]{1})}?\\d{9,11}$', message="Phone number must be entered in the format: '9848281223'. Only 10 digits allowed.")])),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='riders',
            name='zone',
            field=models.ForeignKey(blank=True, to='app.Zone', null=True),
        ),
    ]
