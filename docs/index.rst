django-newapp
=============

{{DESCRIPTION}}

Instalação
----------

.. code-block:: bash

   pip install django-newapp

Adicione a aplicação ao ``INSTALLED_APPS`` e aplique as migrações:

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       "django_newapp",
   ]

.. code-block:: bash

   python manage.py migrate

Compatibilidade: Django 5.2 LTS, 6.0 e 6.1; Python 3.10 ou posterior (Django 6 exige Python 3.12+).

.. toctree::
   :maxdepth: 2

   api
