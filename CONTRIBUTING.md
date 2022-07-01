# Contributing guidelines

We love contributions! If you want to help build and improve our project, please read
the following guidelines before submitting your contributions.

## Conventions

[Please see our guide on the conventions we follow for this
project][docs-project-conventions].

## Requirements

Set up your system as described in the README requirements. Then:

- for local development only, [install multiple Python versions on your
  machine](#installing-multiple-versions-of-python) (3.9, 3.10)
- install all optional packages
  ```zsh
  poetry install --extras "all"
  ```
- install pre-commit hooks
  ```zsh
  cd /path/to/tripadvisor-hotel-reviews-topic-modeling
  pre-commit install
  ```

We use [pre-commit hooks to ensure consistency, and security in our code before it
enters version control][docs-pre-commit].

### Automatically installing pre-commit hooks for any pre-commit-enabled project

[To auto-install pre-commit hooks for all future pre-commit-enabled
projects][pre-commit-auto], run these commands in the terminal:

```zsh
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir ~/.git-template
```

You should only need to do this once per machine, or if you reinstall Git.

### Installing multiple versions of Python

[We use pyenv to handle Python version management][pyenv] on our machines. Follow their
documentation to install it on your system, remembering to add it to your PATH.

Once pyenv is set up, you can install different Python version one at a time from your
terminal.

```zsh
pyenv install --list  # to see all available {PYTHON_VERSION}s
pyenv install {PYTHON_VERSION}
```

You should then use the `pyenv global` command to set the global Python versions that
pyenv manages. [This helps other project features find the correct Python version as
needed](#testing-against-different-python-versions).

For example, to install and globally set (in order) Python 3.9.10, 3.10.2, open
your terminal and run:

```zsh
pyenv install 3.9.10
pyenv install 3.10.2
pyenv global 3.9.10 3.10.2
```

## Testing against different Python versions

We use [nox to test this project against different Python versions to ensure
compatibility][nox]. To run these tests, open your terminal, navigate to this project,
run nox.

```zsh
cd /path/to/tripadvisor-hotel-reviews-topic-modeling
poetry run nox
```

## Continuous integration/continuous deployment

The CI/CD process is managed by Drone and Kubernetes. This:

- runs pre-commit hook checks on all files
- runs the testing suite on Python 3.9-3.10
- builds the [Sphinx documentation as a website accessible by RVU
  employees][project-website]

[Further details can be found in the "Drone and Kubernetes for CI/CD"
guide][docs-drone-k8].

## Viewing the latest documentation

To view the latest changes you’ve made to this project’s documentation, open the
terminal, navigate to the project, run the `sphinx-build` command.

```zsh
cd /path/to/tripadvisor-hotel-reviews-topic-modeling
sphinx-build -b html docs docs/_build
```

Then open the `docs/_build/index.html` file in your favourite web browser, or open it
directly from the terminal.

```zsh
open docs/_build/index.html
```

## Updating the project structure

[The project's structure is based on the RVU Data Science Cookiecutter
template][rvu-ds-cc]. You may wish to update this project's structure with any new
changes in the template.

```{note}
Update the project structure regularly. Security fixes, amongst other changes, are
regularly introduced into the template.

Also, there's a higher chance of conflicts if you have not updated your project in
awhile.

When you restart development of a project, we recommend first submitting a pull request
with only project structure updates, before starting any new developments.
```

To update the project structure, open your terminal, navigate to this project, and
run the `cruft update` command.

```zsh
cd /path/to/tripadvisor-hotel-reviews-topic-modeling
cruft update
```

At the prompt, enter `v` to view the proposed changes; these changes will be shown in
a similar output to running `git diff` command. `cruft` compares the difference between
the latest template commit hash against the template commit hash when your project was
first created or last updated (whichever is later).

Review these changes to ensure you know what the impact might be on your project. When
you're happy with the upcoming changes, exit the comparison by pressing `q`, and enter
`y` at the prompt to apply all changes as a patch.

`cruft` will then attempt to apply the changes. On occasion, `cruft` may not be able
to apply certain changes. This will result in either Git conflicts, which should be
resolved as normal, or the creation of Git rejected (`.rej`) files.

`.rej` files are created when the named project file has been changed, and Git is
unable to determine where to apply the patch, as the underlying code has been changed.
The files are named identically the project file to be patched, with the `.rej` file
extension added. For example, a `.rej` file for `CONTRIBUTING.md` would be called
`CONTRIBUTING.md.rej`.

To fix this, open the `.rej` file to see what changes were trying to be applied. Decide
if these changes are relevant for your project (they may not be!), and copy them into
the relevant location of the project file. You can then safely delete the `.rej` file.
Repeat this process for all `.rej` files.

Once all the changes have been applied, use Git to stage, and commit them. [For more
information, and troubleshooting, take a look at `cruft`'s documentation][cruft].

[cruft]: https://cruft.github.io/cruft/
[docs-drone-k8]: docs/contributing_guide/drone_k8_deployment.md
[docs-pre-commit]: docs/contributing_guide/pre_commit_hooks.md
[docs-project-conventions]: docs/contributing_guide/project_conventions.md
[nox]: https://nox.thea.codes
[poetry]: https://python-poetry.org
[pre-commit-auto]: https://pre-commit.com/#automatically-enabling-pre-commit-on-repositories

<!-- prettier-ignore-start -->
[project-website]: https://tripadvisor-hotel-reviews-topic-modeling.authed.rvu.cloud/
<!-- prettier-ignore-end -->

[pyenv]: https://github.com/pyenv/pyenv
[rvu-ds-cc]: https://github.com/uswitch/rvu-data-science-cookiecutter
