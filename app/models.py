# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.core.validators import RegexValidator

class Zone(models.Model):

    name=models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class riders(models.Model):

    name=models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?([0,7,8,9]{1})}?\d{9,11}$',
                                 message="Phone number must be entered in the format: '9848281223'. Only 10 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=10)
    zone=models.ForeignKey(Zone,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class adm(models.Model):

    name=models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?([0,7,8,9]{1})}?\d{9,11}$',
                                 message="Phone number must be entered in the format: '9848281223'. Only 10 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=10)
    city=models.CharField(max_length=50)
    S_No=models.AutoField(primary_key=True)

    def __str__(self):
        return self.name