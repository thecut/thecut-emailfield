# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import validators
from django.db.models import EmailField as DjangoEmailField


class EmailField(DjangoEmailField):

    default_validators = [validators.validate_email]
