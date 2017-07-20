=====
Usage
=====

To use Pympa Organizations in a project, add it to your `INSTALLED_APPS`:

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
