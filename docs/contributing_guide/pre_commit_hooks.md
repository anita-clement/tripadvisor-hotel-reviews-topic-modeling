# Pre-commit hooks

[We use pre-commit hooks to ensure all our commits meet a minimum standard in terms of
security, type hinting, and formatting and linting][pre-commit]. You only need to
enable hooks once after you've cloned this repository, and installed the requirements.

```zsh
pre-commit install
```

These hooks are run each time you make a commit, whether that's from the command line,
or through an IDE. If any of the hooks fail, you won't be able to commit your changes
until the issues detected by the hooks have been resolved.

Some hooks will automatically fix issues for you. To incorporate these auto-fixes,
first manually fix other issues (if any), and then stage the new changes in Git, and
re-commit your code.

## Hooks currently in use

A brief summary of the pre-commit hooks we use is shown in the table below. If a hook
fails, please see its documentation on how to resolve it.

| Name                                             | Description                                                                                                                                                                                                                                        |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`detect-secrets`][detect-secrets]               | Attempt to detect secrets in your codebase. When scanning for new secrets, remember to add the `--exclude-files` argument with the regular expression pattern in `.pre-commit-config-yaml`, otherwise there will be many false positives detected. |
| [`black`][black]                                 | Automatic Python code formatter to ensure consistency.                                                                                                                                                                                             |
| [`flake8`][flake8]                               | Enforces PEP8 to Python code — note this runs more PEP8 checks than `black`.                                                                                                                                                                       |
| [`flake8-bandit`][flake8-bandit]                 | `flake8` plugin that runs [`bandit`][bandit] to identify common security issues in Python code.                                                                                                                                                    |
| [`flake8-bugbear`][flake8-bugbear]               | `flake8` plugin that tries to find bugs and design problems in Python code.                                                                                                                                                                        |
| [`flake8-docstrings`][flake8-docstrings]         | `flake8` plugin to ensure docstring conventions according to PEP 257 are met.                                                                                                                                                                      |
| [`flake8-rst-docstrings`][flake8-rst-docstrings] | `flake8` plugin to validate docstrings in ReStructuredText.                                                                                                                                                                                        |
| [`isort`][isort]                                 | Sort Python imports in a specified, and consistent order.                                                                                                                                                                                          |
| [`mypy`][mypy]                                   | Static type checker to ensure functions/classes have type hints, and they are used correctly.                                                                                                                                                      |
| [`safety`][safety]                               | Checks Python dependencies for known vulnerabilities.                                                                                                                                                                                              |
| [`nbstripout`][nbstripout]                       | Strips outputs and metadata from notebooks (Jupyter, Google Colab, Databricks) for security and to reduce data leakage.                                                                                                                            |
| [`nbqa`][nbqa]                                   | Run formatters, linters, and other tools on notebooks. Currently set for `black` and `isort`.                                                                                                                                                      |
| `end-of-file-fixer`                              | Ensure files end with a blank line.                                                                                                                                                                                                                |
| `trailing-whitespace`                            | Remove any trailing blank space in code.                                                                                                                                                                                                           |
| `check-added-large-files`                        | Prevent any large (500 KB+) files from entering version control.                                                                                                                                                                                   |
| `check-toml`                                     | Check TOML files for valid syntax.                                                                                                                                                                                                                 |
| `check-yaml`                                     | Check YAML files for valid syntax.                                                                                                                                                                                                                 |
| [`prettier`][prettier]                           | Standardise formatting for JS, TypeScript, Flow, JSX, JSON, CSS, SCSS, Less, HTML, Vue, Angular, GraphQL, Markdown, and YAML files.                                                                                                                |

[bandit]: https://bandit.readthedocs.io
[black]: https://black.readthedocs.io
[detect-secrets]: https://github.com/Yelp/detect-secrets
[flake8]: https://flake8.pycqa.org
[flake8-bandit]: https://github.com/tylerwince/flake8-bandit
[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear
[flake8-docstrings]: https://gitlab.com/pycqa/flake8-docstrings
[flake8-rst-docstrings]: https://github.com/peterjc/flake8-rst-docstrings
[isort]: https://pycqa.github.io/isort
[mypy]: https://mypy.readthedocs.io
[nbstripout]: https://github.com/kynan/nbstripout
[nbqa]: https://nbqa.readthedocs.io
[pre-commit]: https://pre-commit.com
[prettier]: https://prettier.io
[safety]: https://pyup.io/safety
