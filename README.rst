========
Overview
========

.. start-badges

.. image:: https://img.shields.io/badge/python-3.8-blue
   :target: https://github.com/m0ga0/python-project-template

.. image:: https://codecov.io/gh/m0ga0/python-project-template/branch/main/graph/badge.svg?token=4XEHN8HP94
   :target: https://codecov.io/gh/m0ga0/python-project-template

.. image:: https://github.com/m0ga0/python-project-template/workflows/main-pipeline/badge.svg
   :target: https://github.com/m0ga0/python-project-template/actions?query=workflow%3Amain-pipeline

.. end-badges

This project is used as a python project / library template. It solves the problem how we
can quickly setup a new business-oriented python project with modern management tools and libraries.

This project provides below tools:

* python version and virtual environment management
* python dependencies management
* linters and formatters
* unit-testing, test env automation, and coverage reports
* a organized file structure for both source code and tests
* pre-commit configurations and github actions configs
* a matured docstring, documentation examples, and generation tool

Create a new project from this template
=======================================
Since this is a github repo template, you can use it to create a new python project project-X:

* click "Use this template" button on the top right corner
* select an account in the owner drop down
* type the name of your new project repo, choose it's public or private
* click "repository from template" button.


Git clone project-X repo
------------------------
::

    git clone <project-X repo url>

Source file structure
---------------------
In the downloaded repo folder, we've already organized the code structure as below::

    ├─ setup.py
    ├─ src/
    |   ├─ <project_name>/
    |       ├─ __init__.py
    |       ├─ app.py
    |       ├─ view.py
    ├─ tests/
        ├─ __init__.py
        ├─ foo/
        |   ├─ __init__.py
        |   ├─ test_view.py
        ├─ bar/
            ├─ __init__.py
            ├─ test_view.py

We strongly suggest you follow this structure as it helps manage source codes, tests, and docs.
For example, it allows pytest to load modules whose file names can be the same (in above example both named test_view.py),
while tools like tox can also test the ``project_name`` you will later install via ``poetry install``.

Now let's start to change our package / project name through out this new code base.

Change root folder's name
-------------------------
Go into ``src`` folder, change the root folder's name to project-X::

    ├─ setup.py
    ├─ src/
    |   ├─ project_x/
    |       ├─ __init__.py


Config pyproject.toml
---------------------
``pyproject.toml`` is a project config file managing version, dev / prod dependencies,
build system, exposed commands and other configs. If you want to create this file from scratch, remove the
existing one, and type below command::

    poetry init

This will guide you to set up project settings step by step.

Or you can just modify this file as below::

    [tool.poetry]
    name = "project-X"                          # usually a hyphenated name
    version = "0.1.0"                           # this is the version when you finally build the package
    description = "<your project description"   # detail information of your project
    authors = ["<authors>"]

.. image:: /_static/modify_pyproject_basic_info.jpg

If you have defined scripts containing ``main`` or other methods, you can add it in the ``[tool.poetry.scripts]``
section of ``pyproject.toml``::

    [tool.poetry.scripts]
    hello = "<module_path>:main"    # sample: main is the exposed entrypoint of your module

Config .coveragerc
------------------
``.coveragerc`` is the config for coverage library, you need to set correct source folder in ``[run]`` section::

    [run]
    source =
        ./src/project_x

.. highlights:: Please be noted that whenever you edit ``pyproject.toml``, please run ``poetry update``

.. _config-sphinx:

Config sphinx config
--------------------
Go to ``docs/source/conf.py``, change ``project``, ``author`` and ``release``::

    # -- Project information -----------------------------------------------------

    project = "project-X"
    copyright = "2021, <author>"    # replace <author> with your name
    author = "<author>"

    # The full version, including alpha/beta/rc tags
    release = "<version>"

Then change ``index.rst``, replace with your own package name.

Setup private repository source for python package
--------------------------------------------------
Please config private package repo and its credential first ( :ref:`config-private-repo` ).
In order to install packages from this repo, you should edit ``pyproject.toml``::

    [[tool.poetry.source]]
    name = "<pypi-repo-name>"
    url = "<pypi-repo-url>"
    secondary = true    # Pypi to be primary, while this one be the secondary

or::

    default = true  # only lookup your package in the private repo


Development environment setup
=============================
Now let's start setting up dev tools.

Install poetry
--------------
While pip is a tool to install python packages. We still need a tool to manage python package dependencies.
`Poetry <https://python-poetry.org/>`_ is a modern python project management and dependencies resolving tool,
let's install it::

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
    poetry --version

PS: Don't forget to add poetry bin into your $PATH and ~/.bashrc, more details please follow
`poetry instructions <https://python-poetry.org/docs/master/#osx--linux--bashonwindows-install-instructions>`_::

    export PATH=":$HOME/.poetry/bin:$PATH"

Install pyenv
-------------
pyenv helps setup multiple python versions in the developing system.

* If you haven't installed pyenv yet, please refer to
  `pyenv installation <https://github.com/pyenv/pyenv#installation>`_.
* If you already have a older version of pyenv, and you want to update it to the latest
  version, please refer to `pyenv-update <https://github.com/pyenv/pyenv-update>`_ tool.

Install a specific python version
---------------------------------
After you decide which python version to use, first install it via pyenv::

    pyenv install --list                    # to show all availabel python version to install
    pyenv install 3.8.12                    # pick a version to install
    pyenv virtualenv 3.8.12 venv-project-x  # define a virtualenv with an installed python version
    cd <project folder>                     # go into the project folder, use venv there
    pyenv local venv-project-x              # use the virtualenv for current dir

After activate the virtualenv, you can test current python version by::

    pyenv version

or::

    python -V

(Optional) Install / Upgrade pip
--------------------------------
Usually when you setup a python venv with pyenv, you should have a pip in it.
(if not, refer to `pip installation <https://pip.pypa.io/en/stable/installation/>`_)

Sometimes pip may be out-of-date, and warning keeps raising, update it::

    pip install --upgrade pip

Install tox
-----------
In order to run test env management tool, you need install tox::

    pip install tox

Install pre-commit
------------------
To trigger linting and formatting, you should install pre-commit::

    pip install pre-commit
    pre-commit install

Install sphinx
--------------
You can either user sphinx in poetry env or your local env, if you choose the latter, install sphinx::

    pip install sphinx

(Optional) Install restructuredtext extention for VS code
---------------------------------------------------------
In order to edit reStructuredText documentations, please refer to `reStructuredText extension <https://docs.restructuredtext.net/>`_


Start developing your new project
=================================

Install all dependencies
------------------------
Below command will read the current poetry.lock file in the current directory (or pyproject.toml),
and install all libraries into poetry's own virtualenv::

    poetry install

If you unfortunately meet error "ModuleNotFoundError: No module named 'keyring.backends.macOS'", you can
create the file ``~/.config/python_keyring/keyringrc.cfg`` with the following content
(More details `keyring error <https://github.com/python-poetry/poetry/issues/3662>`_)::

    [backend]
    default-keyring=keyring.backends.SecretService.Keyring


Add new dependencies
--------------------
When developing your own project, add new third-party libraries using below command

* If you want to add *develop* dependencies::

    poetry add -D <new pip package>

* Or if you want to add *prod* dependencies::

    poetry add <new pip package>

When Poetry has finished installing, it writes all of the packages and the exact versions
of them that it downloaded to the poetry.lock file, locking the project to those specific
versions. You should commit the poetry.lock file to your project repo so that all people
working on the project are locked to the same versions of dependencies. (More details:
`poetry lock <https://python-poetry.org/docs/basic-usage/#installing-with-poetrylock>`_)

Optionally, if you manually change any configs in ``pyproject.toml``, you can update
and lock/pinning dependencies like below::

    poetry update   # update dependencies version, and lock them
    poetry lock     # only lock current pypi package versions

If you use pip and requirements.txt previously, you can use `dephell <https://github.com/dephell/dephell>`_
to convert format to poetry::

    dephell deps convert --from-format=pip --to-format=poetry

Develop business code
---------------------
TBD..


Write and run tests
===================

Write unit-tests
----------------
TBD..

Run tests with tox
------------------
To run through unit-tests in test env management tool like tox, you can do below::

    tox

or if you want to run a paticular testenv in tox.ini::

    tox -e <env name1> <env name2>

To run simple scripts or unit-tests like pytest in specified virtual env, use below commands::

    poetry run python <your scripts>.py
    poetry run pytest   # run external commands

Poetry will rirst create a virtual env as per your config and dependencies in pyproject.toml,
and then run your scripts.

If you want to run more commands in the your specific developing virtual env, you can type::

    poetry shell

This will start a new shell with the virtual env, and you can run whatever commands you want.
(More details: `poetry env <https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment>`_)

Generate coverage report
========================
If you run tests with tox, you will find coverage report is one of its testenv. You can generate test
coverage report by::

    tox -e coverage

Pre-commit check and fix
========================
When you run ``git commit``, pre-commit hooks will be automatically triggered because we have setup pre-commit-config.yaml file.
If you want to debug or repro some check failure, you can run below commands::

    pre-commit run --all-files --show-diff-on-failure

Write docs and comments
=======================
Use one of below code styles for docstrings:

* `Google style <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google>`_
* `NumPy style <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy>`_

Use markdown or reStructuredText language for other documentations

Generate documentation with sphinx
==================================
This project use sphinx to generate documentations. For configuration, please check :ref:`config-sphinx`.
then you can start write your doc from index.rst. When you've done, run below command to build the docs::

    cd docs
    make html

html files will be created in ``build/`` folder. As per how to write a good documentation, please check next section.

Build and publish package
=========================

Build sdist and wheel
---------------------
Both sdist and wheel are python package distribution types. The difference is:

    * sdist : stands for "source distributions", directly contains all ``.py`` files and a ``setup.py`` file, which is usually
      in the form of a tarball. However sdist installation requrires the execution of arbitrary code to build the package, thus
      is slower, more difficult to maintain, a security risk.
    * wheel: is the standard archive format of pure python code, no ``.pyc`` files, much smaller than sdist, or eggs. And its installation
      avoids the intermediate step of building packages off of the source distribution.
      (More details: `Why wheel fast <https://realpython.com/python-wheels/#wheels-make-things-go-fast>`_)

You can build a wheel or a sdist via poetry by::

    poetry build

or::

    poetry build -f wheel
    poetry build -f sdist

.. _config-private-repo:

Publish to a remote repository
------------------------------
To publish to a public repo like Pypi::

    poetry publish

To publish to a private repo, you need to config the private repo first:

    * Add the private repo::

        poetry config repositories.<repo-name> <repo-url>

    * You may need to store repo credential::

        poetry config http-basic.<repo-name> <username> <password>


Contribute
==========
Remember to put your own project name below:

* Issue Tracker: github.com/<project>/<project>/issues
* Source Code: github.com/<project>/<project>

Support
=======
If you are facing issues, please let us know via email mo.gao@foxmail.com

License
=======
MIT license
