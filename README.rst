shatoru-backend
===============

::

   A mobile application to keep up-to-date with the Shuttle

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code style: black

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://pycqa.github.io/isort/
    :alt: imports: isort

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit

Prerequisites
-------------

-  Python ≥ 3.10.0
-  Conda ≥ 4.12.0
-  PostgreSQL ≥ 14
-  GNU Make ≥ 3.75

Python
~~~~~~

First make sure that you have python 3.10 or greater installed in your
system.

.. code:: bash

     python --version

If not then first `download <https://www.python.org/downloads/>`__ and
install the appropriate version of python in your system.

Conda
~~~~~

You can download miniconda from
`here <https://docs.conda.io/en/latest/miniconda.html>`__. Check the
conda version using this command after your installation.

.. code:: bash

   conda --version

PostgreSQL
~~~~~~~~~~

Download PostgreSQL and PgAdmin (optional) from
`here <https://www.postgresql.org/download/>`__

GNU Make
~~~~~~~~

Usually, GNU Make comes installed by default on a Linux based system. If
you do not have GNU Make installed in your system then you can skip to
the next part.

Check the version of GNU Make of your system

.. code:: bash

     make --version

Getting Started
---------------

First setup and create a database named ``shatoru``.

Now, create a ``.env`` file from ``.env.sample``. Fill in your database
details and email information. To generate a secret key execute the
command below:

.. code:: bash

   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

After that, create a conda virtual environment

.. code:: bash

   conda create --name shatoru-backend python=3.10 -y

Once the installations have been completed activate the virtual
environment that you just created.

.. code:: bash

   conda activate shatoru-backend

Always remember to activate your virtual environment before running the
backend server.

Now that we have the virtual environment activated, execute the commands
below to setup your backend and start the server

.. code:: bash

       make init
       make server
