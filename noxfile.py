"""Nox sessions."""

from pathlib import Path
from tempfile import TemporaryDirectory

import nox
from nox_poetry import Session, session

PYTHON_VERSIONS = [
    "3.9",
    "3.10",
]

# Set nox to fail on the first error — prevents long running session(s) even after a
# failure
nox.options.stop_on_first_error = True


@session(name="pre-commit")
def pre_commit_hooks(nox_session: Session) -> None:
    """Test pre-commit hooks pass.

    Args:
        nox_session (Session): A ``nox_poetry.Session`` object.

    """
    # Export the Poetry lock file as a `requirements.txt` file, and `pip install` all
    # packages in the nox virtual environment
    nox_session.install("-r", str(nox_session.poetry.export_requirements()))
    args = nox_session.posargs or ["run", "--all-files", "--show-diff-on-failure"]
    nox_session.run("pre-commit", *args)


@session(name="pytest", python=PYTHON_VERSIONS)
def pytest_suite(nox_session: Session) -> None:
    """Check the testing suite passes.

    Test suite passes only if all tests pass, or there are no tests.

    Args:
        nox_session (Session): A ``nox_poetry.Session`` object.

    """
    # Export the Poetry lock file as a `requirements.txt` file, and `pip install` all
    # packages in the nox virtual environment. Also install the project's root
    # package(s)
    nox_session.install("-r", str(nox_session.poetry.export_requirements()))
    nox_session.poetry.installroot()

    # Set the session arguments, and run the `pytest` command
    args = nox_session.posargs or []
    nox_session.run("pytest", *args, success_codes=[0, 5])


@session(name="sphinx")
@nox.parametrize("builder", ["html", "linkcheck"])
def validate_sphinx_documentation(nox_session: Session, builder: str) -> None:
    """Check Sphinx documentation is valid.

    Args:
        nox_session (Session): A ``nox_poetry.Session`` object.
        builder (str): A valid Sphinx builder.

    """
    # Export the Poetry lock file as a `requirements.txt` file, and `pip install` all
    # packages in the nox virtual environment. Also install the project's root
    # package(s)
    nox_session.install("-r", str(nox_session.poetry.export_requirements()))
    nox_session.poetry.installroot()

    # Define the current documentation directory
    docs_directory = Path().cwd().joinpath("docs")

    # Create a temporary directory to store the Sphinx link check
    with TemporaryDirectory() as temporary_directory:
        nox_session.chdir(Path(temporary_directory))

        # Check the documentation
        nox_session.run(
            "sphinx-build",
            "-b",
            builder,
            "-W",
            str(docs_directory),
            temporary_directory,
        )
