#!/usr/bin/python
from django.db.models import get_apps, get_app
from django.test.simple import DjangoTestSuiteRunner, build_test, build_suite
from django.test.testcases import TestCase
from django.conf import settings
import unittest

try:
    from django.test.simple import reorder_suite
    
except ImportError:
    from django.test.runner import reorder_suite
    
class DjangoIgnoreTestSuiteRunner(DjangoTestSuiteRunner):
    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        suite = unittest.TestSuite()

        if test_labels:
            for label in test_labels:
                if '.' in label:
                    suite.addTest(build_test(label))
                else:
                    app = get_app(label)
                    suite.addTest(build_suite(app))
        else:
            # Get ignored tests
            ignored_labels = getattr(settings, "IGNORE_TESTS", ())
            ignored_apps = []
            for ilabel in ignored_labels:
                if "." in ilabel:
                    ilabel = ilabel.split(".")[-1]
                try:
                    app = get_app(ilabel)
                except Exception as e:
                    print e
                ignored_apps.append(app)

            for app in get_apps():
                if app not in ignored_apps:
                    suite.addTest(build_suite(app))

        if extra_tests:
            for test in extra_tests:
                suite.addTest(test)

        return reorder_suite(suite, (TestCase,))
