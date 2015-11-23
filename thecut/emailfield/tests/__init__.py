# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import VERSION as DJANGO_VERSION

if DJANGO_VERSION < (1, 4):
    from .test_forms import *  # NOQA
    from .test_models import *  # NOQA
