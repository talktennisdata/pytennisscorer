Installation
============

Requirements
------------

pytennisscorer requires Python 3.9 or higher and has zero runtime dependencies.

Installation Methods
--------------------

Using pip
~~~~~~~~~

The simplest way to install pytennisscorer is using pip:

.. code-block:: bash

   pip install pytennisscorer

Using uv (Recommended)
~~~~~~~~~~~~~~~~~~~~~~

For better dependency management and faster installation, we recommend using `uv <https://github.com/astral-sh/uv>`_:

.. code-block:: bash

   # Install uv if you haven't already
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install pytennisscorer
   uv pip install pytennisscorer

From Source
~~~~~~~~~~~

To install the latest development version from source:

.. code-block:: bash

   git clone https://github.com/seidlr/pytennisscorer.git
   cd pytennisscorer
   pip install -e .

Or using uv:

.. code-block:: bash

   git clone https://github.com/seidlr/pytennisscorer.git
   cd pytennisscorer
   uv pip install -e .

Development Installation
------------------------

For development, install with all development dependencies:

.. code-block:: bash

   git clone https://github.com/seidlr/pytennisscorer.git
   cd pytennisscorer
   uv sync --all-extras --dev

This will install:

* pytest - for running tests
* pytest-cov - for code coverage
* mypy - for type checking
* ruff - for linting and formatting
* hypothesis - for property-based testing
* jupyter - for running example notebooks

Verifying Installation
----------------------

After installation, verify that pytennisscorer is installed correctly:

.. code-block:: python

   import pytennisscorer
   print(pytennisscorer.__version__)

   # Test basic functionality
   from pytennisscorer import TennisScorer, MatchType
   scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)
   print("Installation successful!")

Troubleshooting
---------------

Python Version Issues
~~~~~~~~~~~~~~~~~~~~~

If you encounter issues related to Python version, ensure you have Python 3.9 or higher:

.. code-block:: bash

   python --version

Import Errors
~~~~~~~~~~~~~

If you get import errors, ensure pytennisscorer is installed in the active environment:

.. code-block:: bash

   pip list | grep pytennisscorer

Or with uv:

.. code-block:: bash

   uv pip list | grep pytennisscorer

Getting Help
------------

If you encounter any issues during installation:

1. Check the `GitHub Issues <https://github.com/seidlr/pytennisscorer/issues>`_
2. Create a new issue with details about your environment and the error
3. Join the discussion in existing issues