=============================
Pympa Organizations
=============================

.. image:: https://badge.fury.io/py/pympa-organizations.svg
    :target: https://badge.fury.io/py/pympa-organizations

.. image:: https://travis-ci.org/simodalla/pympa-organizations.svg?branch=master
    :target: https://travis-ci.org/simodalla/pympa-organizations

.. image:: https://codecov.io/gh/simodalla/pympa-organizations/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/simodalla/pympa-organizations

Your project description goes here

Documentation
-------------

The full documentation is at https://pympa-organizations.readthedocs.io.

Quickstart
----------

Install Pympa Organizations::

    pip install pympa-organizations

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'paorganizations.apps.PaorganizationsConfig',
        ...
    )

Add Pympa Organizations's URL patterns:

.. code-block:: python

    from paorganizations import urls as paorganizations_urls


    urlpatterns = [
        ...
        url(r'^', include(paorganizations_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
