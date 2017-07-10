# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeform', '0003_employee_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='file',
        ),
    ]
