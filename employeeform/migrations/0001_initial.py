# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('Adhaar', models.IntegerField()),
                ('Licence_Number', models.IntegerField()),
                ('RC_Card_No', models.IntegerField()),
                ('Mobile_No', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\+?([0,7,8,9]{1})}?\\d{9,11}$', message=b"Phone number must be entered in the format: '9848281223'. Only 10 digits allowed.")])),
                ('Current_Address', models.TextField(max_length=500)),
                ('Permanent_Address', models.TextField(max_length=500)),
                ('Father_spouse_Name', models.CharField(max_length=100)),
                ('Address', models.TextField(max_length=500)),
                ('Employee_Id', models.CharField(default=b'Id', max_length=100)),
                ('Hub', models.CharField(default=b'Hub', max_length=100)),
                ('Date_of_Joining', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
