# Project conventions

```{note}
These conventions are guidelines; please following them whenever possible.
```

## Coding practices

All code must be version-controlled, and pushed to GitHub. Git branches are
inexpensive, and commits can be squashed or fixed-up at a later date. Therefore, it's
strongly recommended that even work-in-progress code is pushed up at regular intervals.

Also consider merging/rebasing from the `main` branch at regular intervals to ensure
you have the latest features, bug fixes, and other changes in your development branch.
The contributor is responsible for ensuring their development code works with the
`main` branch.

Any files that need to be kept, such as model outputs, should be stored on Google Cloud
Storage (GCS), or another appropriate place. For example, tabular data could be stored
on GCS or Google BigQuery (GBQ), depending on your use case.

```{warning}
Do not store code/files that need to be kept either locally or on virtual machines, as
they are not accessible by other team members, and/or may be destroyed at any point.
```

Be careful about the separation between development, testing, and production
environments.

```{warning}
Do not develop/test in a production environment.
```

## Project-specific service accounts on Google Cloud Platform

Before you start a new project on Google Cloud Platform (GCP), you should [create a
project-specific service account (SA) with only the minimum IAM roles
needed][create-service-account] for security purposes.

You will need to grant at least the following IAM roles for your service account:

- `Storage Object Viewer` to access the startup script
- `Logs Writer` to write to Cloud Logging
- `BigQuery User` to access your default project's GBQ datasets

If you need to read/write access to Google Cloud Storage using the Python SDK, replace
`Storage Object Viewer` with `Storage Admin`.

If you need GBQ read access to data on another GCP project, ask that you are granted
`BigQuery Data Viewer`, and `BigQuery Job User` IAM roles on this project in the
`#data-engineering-support` Slack channel with the following information:

- the GCP project you want to access
- your SA ID

Attach the project-specific SA to all GCP resources you use for this project.

## Google Compute Engine, and Vertex AI Workbench virtual machine instances

All virtual machine (VM) instances on Google Compute Engine (GCE), and Vertex AI
Workbench must be considered temporary.

VMs should be used for development purposes only and, once development has been
paused or completed, they should be torn down. [Code, and files should be backed up
elsewhere](#coding-practices).

This is for both security, and maintenance purposes. Vulnerabilities may be identified
in packages (Linux and/or Python) installed on a VM over time, and it can become
difficult to identify, and patch insecure VMs.

We recommend tearing down, and rebuilding VM instances at least once a month in any
case.

## Google Cloud Platform resource naming conventions

Please follow these naming conventions for different GCP resources:

- GCE/Vertex AI Workbench VMs: `{PROJECT_NAME}`
- GBQ datasets, GCS buckets, GCR top-level folders:
  - Development environments: `dev_{FIRST_NAME}_{LAST_NAME}_{PROJECT_NAME}`
  - Testing environments: `test_{FIRST_NAME}_{LAST_NAME}_{PROJECT_NAME}`
  - Production environments: `{PROJECT_NAME}`
- Vertex AI pipelines:
  - Development environments: `dev_{FIRST_NAME}_{LAST_NAME}_{PROJECT_NAME}_{TIMESTAMP}`
  - Testing environments: `test_{FIRST_NAME}_{LAST_NAME}_{PROJECT_NAME}_{TIMESTAMP}`
  - Production environments: `{PROJECT_NAME}_{TIMESTAMP}`

where `{PROJECT_NAME}` is the name of your project, `{FIRST_NAME}` and `{LAST_NAME}`
are the first and last names of the contributor, and `{TIMESTAMP}` is a timestamp of
when the relevant job or code was submitted.

[create-service-account]: https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount
