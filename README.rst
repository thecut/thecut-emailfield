=================
thecut-emailfield
=================


.. image:: https://travis-ci.org/thecut/thecut-emailfield.svg
  :target: https://travis-ci.org/thecut/thecut-emailfield

.. image:: https://codecov.io/github/thecut/thecut-emailfield/coverage.svg
  :target: https://codecov.io/github/thecut/thecut-emailfield

.. image:: https://readthedocs.org/projects/thecut-emailfield/badge/?version=latest
  :target: http://thecut-emailfield.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

A Django email field which validates by checking for an MX record on the domain.


Documentation
-------------

The full documentation is at https://thecut-emailfield.readthedocs.org.


Quickstart
----------

Install ``thecut-emailfield`` using the installation instructions found in the project documentation.

An example ``models.py``::

    # -*- coding: utf-8 -*-
    from __future__ import absolute_import, unicode_literals
    from django.db import models
    from thecut.emailfield.models import EmailField


    class EmailModel(models.Model):

        email = EmailField()


An example ``forms.py``::

    # -*- coding: utf-8 -*-
    from __future__ import absolute_import, unicode_literals
    from django import forms
    from thecut.emailfield.forms import EmailField


    class EmailForm(forms.Form):

        email = EmailField()


Credits
-------

See ``AUTHORS.rst``.
