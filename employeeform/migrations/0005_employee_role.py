# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeform', '0004_remove_employee_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Role',
            field=models.CharField(max_length=5, null=True, choices=[(b'Rider', b'RIDER'), (b'Admin', b'ADMIN')]),
        ),
    ]
