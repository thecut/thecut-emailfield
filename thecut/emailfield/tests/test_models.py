# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import VERSION as DJANGO_VERSION
from django.core.exceptions import ValidationError
from django.test import TestCase
from dns.exception import DNSException
from mock import patch
from test_app.models import EmailModel
from unittest import skipIf


class TestEmailModelField(TestCase):

    """Tests for the EmailField model field."""

    @patch('dns.resolver.query')
    def test_rejects_domain_without_mx_record(self, fake_query):
        """Reject email address for a domain without an MX record."""
        fake_query.side_effect = DNSException()
        model = EmailModel(email='development@thecut.net.au')
        with self.assertRaises(ValidationError):
            model.full_clean()
        # Enure dns.resolver.query() was actually called.
        fake_query.assert_called_once_with('thecut.net.au', 'MX')

    @patch('dns.resolver.query')
    def test_accepts_domain_with_mx_record(self, fake_query):
        """Accept email address for a domain with an MX record."""
        model = EmailModel(email='development@thecut.net.au')
        try:
            model.full_clean()
        except ValidationError:
            self.fail('Email address was incorrectly rejected.')
        # Enure dns.resolver.query() was actually called.
        fake_query.assert_called_once_with('thecut.net.au', 'MX')
