# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import VERSION as DJANGO_VERSION
from django.core.exceptions import ValidationError
from django.test import TestCase
from test_app.models import EmailModel
from unittest import skipIf


class TestEmailField(TestCase):

    """Tests for the EmailField model field."""

    @skipIf(DJANGO_VERSION >= (1, 5), 'This validation is handled by Django.')
    def test_rejects_address_without_at_sign(self):
        """Reject email addresses without an '@' sign."""
        model = EmailModel(email='INVALID')
        with self.assertRaises(ValidationError):
            model.full_clean()
