#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `django-error-views` package."""

from click.testing import CliRunner

import django_error_views
from django_error_views import cli

django_error_views.__version__


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'django_error_views.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
