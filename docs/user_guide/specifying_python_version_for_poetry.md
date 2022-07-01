# Specifying the Python version for the Poetry environment

You may have multiple versions of Python installed on your system, but wish to use a
specific (non-default) version for your Poetry environment.

[If the Python versions are installed using `pyenv`][pyenv], follow these steps to use
a specific Python version for your Poetry environment.

First, find out what Python versions are installed on your system using:

```zsh
pyenv versions
```

in your terminal, For example, this may print out:

```zsh
3.9.10
3.10.2
```

which means Python 3.9.10, and 3.10.2 are installed.

Next invoke the `pyenv shell` command, supplying the Python version you want to use.
For example, to use `3.9.10`, enter this into your terminal:

```zsh
pyenv shell 3.9.10
```

You can then check the correct Python version is selected using:

```zsh
python --version
```

which should print `Python 3.9.10` in the above example. Alternatively, if the pyenv
shell integration is not set up, you can use the `pyenv local` command for a similar
effect:

```zsh
pyenv local 3.9.10
```

Note this will create a `.python-version` file in your repository — this should not be
tracked by Git, as container images may use different patch versions of Python.

Now set Poetry to use this Python version with the `poetry env use` command.

```zsh
poetry env use $(which python{X}.{Y})
```

where `{X}` and `{Y}` are the major, and minor Python version numbers. For example, for
Python 3.9.10, this command would be:

```zsh
poetry env use $(which python3.9)
```

Running this command will create a (relatively) empty Poetry environment, and print
its name in your terminal, for example:

```zsh
{NAME}-{HASH}--py{X}.{Y}
```

where `{NAME}` is defined in the `name` variable of `pyproject.toml`, `{HASH}` is a
Poetry-generated hash, and `{X}` and `{Y}` are the major, and minor Python version
numbers of the Python version you selected.

Running `poetry install` will now install your package dependencies in your chosen
Python version.

[pyenv]: https://github.com/pyenv/pyenv
