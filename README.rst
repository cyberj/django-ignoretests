django-ignoretests
==================

Application to ignore some tests from a Django project.

https://github.com/cyberj/django-ignoretests

Usage
-----

Just add add to your settings.py::

    TEST_RUNNER="ignoretests.DjangoIgnoreTestSuiteRunner"
    IGNORE_TESTS = (
        # Apps to ignore. example : 'django.contrib.auth',
        )

If you want to use `django-jenkins <http://github.com/kmmbvnr/django-jenkins>`_ also add to your settings.py::

    JENKINS_TEST_RUNNER="testignore.jenkins.JenkinsIgnoreTestSuiteRunner"
