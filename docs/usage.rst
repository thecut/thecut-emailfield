=====
Usage
=====


Validating a model field
------------------------

You can use ``thecut-emailfield`` to validate email addresses on a model by
using :class:`~thecut.emailfield.models.EmailField`.

An example ``models.py``::

    # -*- coding: utf-8 -*-
    from __future__ import absolute_import, unicode_literals
    from django.db import models
    from thecut.emailfield.models import EmailField


    class EmailModel(models.Model):

        email = EmailField()


Validating a form field
------------------------

You can use ``thecut-emailfield`` to validate email addresses on a form by
using :class:`~thecut.emailfield.forms.EmailField`.

An example ``forms.py``::

    # -*- coding: utf-8 -*-
    from __future__ import absolute_import, unicode_literals
    from django import forms
    from thecut.emailfield.forms import EmailField


    class EmailForm(forms.Form):

        email = EmailField()
