Contributing
============

We welcome contributions to pytennisscorer! This document provides guidelines for contributing to the project.

Getting Started
---------------

1. Fork the repository on GitHub
2. Clone your fork locally:

   .. code-block:: bash

      git clone https://github.com/your-username/pytennisscorer.git
      cd pytennisscorer

3. Install development dependencies:

   .. code-block:: bash

      uv sync --all-extras --dev

Development Setup
-----------------

We use `uv` for dependency management. Make sure you have it installed:

.. code-block:: bash

   curl -LsSf https://astral.sh/uv/install.sh | sh

Install the package in development mode:

.. code-block:: bash

   uv sync --all-extras --dev

This installs all development tools:

* **pytest** - Testing framework
* **pytest-cov** - Coverage reporting
* **mypy** - Type checking
* **ruff** - Linting and formatting
* **hypothesis** - Property-based testing

Code Style
----------

We follow strict code quality standards:

Python Code
~~~~~~~~~~~

* **Formatting**: We use ``ruff`` with double quotes and 100-character line length
* **Type hints**: All functions must have type hints
* **Docstrings**: All public functions need docstrings
* **Naming**: Follow PEP 8 naming conventions

Run formatting:

.. code-block:: bash

   make format

Check code style:

.. code-block:: bash

   make lint

Type Checking
~~~~~~~~~~~~~

We use ``mypy`` in strict mode. All code must pass type checking:

.. code-block:: bash

   make type-check

Testing
-------

Writing Tests
~~~~~~~~~~~~~

* Write tests for all new functionality
* Follow Test-Driven Development (TDD) when possible
* Place tests in the ``tests/`` directory
* Name test files as ``test_<module>.py``
* Use descriptive test names: ``test_<function>_<scenario>_<expected>``

Running Tests
~~~~~~~~~~~~~

Run all tests:

.. code-block:: bash

   make test

Run with coverage:

.. code-block:: bash

   make test-cov

Run specific test files:

.. code-block:: bash

   uv run pytest tests/test_scorer.py -v

Test Coverage
~~~~~~~~~~~~~

We maintain a minimum of 80% test coverage. Check coverage:

.. code-block:: bash

   make test-cov

Making Changes
--------------

1. Create a new branch for your feature or fix:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

2. Make your changes following the code style guidelines

3. Write or update tests for your changes

4. Run the full test suite:

   .. code-block:: bash

      make check

5. Commit your changes with a descriptive message:

   .. code-block:: bash

      git add .
      git commit -m "feat: add new feature description"

Commit Message Format
~~~~~~~~~~~~~~~~~~~~~

We follow conventional commits:

* ``feat:`` - New feature
* ``fix:`` - Bug fix
* ``docs:`` - Documentation changes
* ``test:`` - Test additions or changes
* ``refactor:`` - Code refactoring
* ``chore:`` - Maintenance tasks

Submitting Changes
------------------

1. Push your branch to GitHub:

   .. code-block:: bash

      git push origin feature/your-feature-name

2. Open a Pull Request against the ``main`` branch

3. Ensure all CI checks pass

4. Wait for code review

Pull Request Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~

* Keep PRs focused on a single change
* Update documentation if needed
* Add tests for new functionality
* Ensure all tests pass
* Update the changelog if applicable

Development Commands
--------------------

The Makefile provides convenient commands:

.. code-block:: bash

   make help          # Show all available commands
   make install       # Install package in editable mode
   make test          # Run all tests
   make test-unit     # Run unit tests only
   make test-cov      # Run tests with coverage
   make lint          # Run linter
   make format        # Format code
   make type-check    # Run type checker
   make check         # Run all checks
   make clean         # Clean build artifacts
   make build         # Build distribution packages

Continuous Integration
----------------------

All pull requests trigger GitHub Actions workflows that:

1. Run tests across Python 3.9-3.12
2. Check code formatting with ruff
3. Verify type hints with mypy
4. Calculate test coverage
5. Build documentation
6. Test on multiple operating systems (Linux, Windows, macOS)

Areas for Contribution
-----------------------

We especially welcome contributions in these areas:

* **New match formats**: Support for additional tennis formats
* **Serialization**: Save/load match state
* **Statistics**: Match statistics and analytics
* **Performance**: Optimizations for large-scale simulations
* **Documentation**: Improvements and examples
* **Internationalization**: Support for multiple languages

Questions?
----------

If you have questions about contributing:

1. Check existing issues and discussions
2. Open a new issue for clarification
3. Join the discussion in pull requests

Thank you for contributing to pytennisscorer!