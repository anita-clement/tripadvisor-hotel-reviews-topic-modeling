# Writing technical documentation

Writing documentation is important. It not only helps users, contributors, and our
team(s) understand what we have produced, but can also help our future selves remember
what we have done.

But keeping documentation up-to-date is tricky. If it is stored separately from code,
there's a risk it will not be updated.

## Where to store documentation

For our projects, we recommend that all technical documentation is stored in the `docs`
folder, and updated in each pull request if it is affected by any changes.

This also ensures transparency and helps verification — reviewers can quickly see if
the documentation has been updated, as it will be in the commit history.

High-level documentation can be stored elsewhere, but it should refer to the `docs`
folder.

## Using Sphinx

We [use Sphinx, a Python document builder, to create a searchable website of our
project's documentation][sphinx]. Additional Sphinx extensions allow us to:

1. [write in Markdown][myst-parser]
2. [write mathematics][sphinx-mathjax]
3. [easily incorporate Python docstrings using `autosummary`][sphinx-autosummary]
4. [use Google- (preferred) or NumPy-style docstrings][sphinx-napoleon]

Most of the time, you will be writing as normal in Markdown. There are only a few
cases where you'll need to add Sphinx-related components, called directives. All
[Sphinx directives need to be included as a block-level in
Markdown, or within a `eval-rst` block][myst-parser-directives]. Some cases include:

- [adding/changing a Markdown file on Sphinx's table of contents (TOC) tree
  directive][sphinx-toctree]
- [including a Markdown file from outside the `docs` folder][myst-parser-outside-files]
- including Python docstrings in a Markdown file using `autosummary`

Note this list is not exhaustive. Take a look at the existing Markdown documentation,
which uses these directives.

### Deploying the documentation website

We use Drone CI to manage continuous deployment of our documentation. This happens
automatically whenever a commit is pushed into the `main` branch.

[myst-parser]: https://myst-parser.readthedocs.io
[myst-parser-directives]: https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
[myst-parser-outside-files]: https://myst-parser.readthedocs.io/en/latest/faq/index.html#include-a-file-from-outside-the-docs-folder-like-readme-md
[sphinx]: https://www.sphinx-doc.org
[sphinx-autosummary]: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
[sphinx-mathjax]: https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax
[sphinx-napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[sphinx-toctree]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-of-contents
