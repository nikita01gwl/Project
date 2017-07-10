# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeform', '0002_auto_20170703_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='file',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
        ),
    ]
