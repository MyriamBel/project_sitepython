# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
class Founders(models.Model):
    id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    birth_date = models.DateField('date of birth')
