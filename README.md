# Tripadvisor Hotel Reviews Topic Modeling

This project aims at detecting topics from negative and positive hotel reviews from Tripadvisor.

The first part of the project consists in implementing BERTopic first introduced in this [paper](https://doi.org/10.48550/arXiv.2203.05794).
The corresponding work main lies in the `notebooks` section as it is quite visual.

The second part of the project [WIP] will consist in using transformers models for zero-shot learning.

The last part [WIP] will attempt at doing some few-shot learning by manually labelling some instances.

## Getting started

First, make sure [you set up your machine to run this project
locally](#requirements-for-running-locally), or [create a virtual machine (VM) instance
for running in the cloud](#requirements-for-running-in-the-cloud).

Next, [set up your preferred IDE to use the installed Poetry
environment][docs-set-ide], or activate it in your terminal.

```zsh
cd /path/to/tripadvisor-hotel-reviews-topic-modeling
poetry shell
```

[You can find more information about using this project in the user
guide][docs-user-guide].

### Requirements for running locally

Aside from a clone of this repository, you will need the following requirements to run
this project locally:

- Python 3.9 or later installed
- [Poetry installed on your machine][poetry] for virtual environment and dependency
  management
- Python packages installed using Poetry
  ```zsh
  cd /path/to/tripadvisor-hotel-reviews-topic-modeling
  poetry install
  ```
- Have your Kaggle API token in the location ~/.kaggle/kaggle.json

[To use a specific Python version in your Poetry environment, please refer to this
guidance][docs-specifying-python-version-for-poetry].

## Contributing

We love contributions! If you want to help build and improve our project, [please read
our contributing guidelines][docs-contributing] beforehand.

[docs-contributing]: CONTRIBUTING.md
[docs-set-ide]: docs/user_guide/setting_up_your_ide.md
[docs-specifying-python-version-for-poetry]: docs/user_guide/specifying_python_version_for_poetry.md
[docs-user-guide]: docs/user_guide/user_guide.md
[poetry]: https://python-poetry.org

<!-- prettier-ignore-start -->
[project-website]: https://tripadvisor-hotel-reviews-topic-modeling.authed.rvu.cloud/
<!-- prettier-ignore-end -->
