# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from thecut.emailfield.models import EmailField


class EmailModel(models.Model):

    email = EmailField()
