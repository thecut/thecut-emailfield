# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from thecut.emailfield.forms import EmailField


class EmailForm(forms.Form):

    email = EmailField()
