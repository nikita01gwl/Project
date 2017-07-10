# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\+?([0,7,8,9]{1})}?\\d{9,11}$', message="Phone number must be entered in the format: '9848281223'. Only 10 digits allowed.")])),
                ('city', models.CharField(max_length=50)),
                ('S_No', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
    ]
