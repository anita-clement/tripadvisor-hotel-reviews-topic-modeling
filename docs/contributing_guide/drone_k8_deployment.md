# Drone and Kubernetes for CI/CD

We use Drone and Kubernetes for CI/CD in this project. The Drone configuration file is
located at `.drone.yml`, and all Kubernetes configurations are found in the `k8s`
folder.

[You should install Uswitch's U binary][notion-u] before continuing with this guide.

## Enabling Drone

To enable Drone in your project in the `data-science` namespace, open your terminal,
navigate to the project, and run:

```zsh
u drone init --namespace=data-science
```

## Adding, overwriting, or deleting Drone secrets

To add a Drone secret, open your browser and go to:

```text
https://ci.usw.co/uswitch/{REPOSITORY_NAME}
```

where `{REPOSITORY_NAME}` is the name of your GitHub repository.

Click the hamburger menu button on the top-right of your window, next to your profile
picture, and select `Secrets`. Here you can add or delete (but not view) Drone secrets.
To overwrite an existing secret, first delete it, and then add the new secret.

The secret is then accessed in your Drone pipeline step by adding a `secrets` key that
references the secret, for example:

```yaml
pipeline:
  example-step:
    secrets: [{ DRONE_SECRET }]
```

where `DRONE_SECRET` is the Drone secret environment variable name.

## Deploying documentation

The project's documentation is deployed using Kubernetes and a NGINX web server. This
is done automatically whenever there is a push into the `main` branch of this project.

## How Drone works — a general overview

```{note}
We're using an older version of Drone than currently available (v0.8.10 with additional
changes) in a [forked repository][uswitch-drone].

[Archived documentation for this version is available][drone-docs].
```

This is a brief overview of how Drone works; for further details, see the archived
documentation for our Drone version.

Drone runs the pipeline as defined by the `pipeline` field in the `.drone.yml` file.
Each nested field within `pipeline` is a step of the pipeline, and they are run
sequentially; if a step fails, none of the proceeding steps are run.

The first step the Drone always runs, even if it's not defined in `.drone.yml`, is to
clone the Git repository into a shared volume. This shared volume is persisted across
all pipeline steps. By default, [the shared volume is located at in the Drone
workspace][drone-docs-workspace] at `/drone/src/github.com/uswitch/{REPOSITORY_NAME}`,
where `{REPOSITORY_NAME}` is the name of the repository.

Here's an example pipeline that we'll use for this overview:

```yaml
pipeline:
  first-pipeline-step:
    when:
      event: push
    image: container_image:container_image_tag
    commands:
      - echo Hello
  second-pipeline-step:
    when:
      event: push
      branch: main
    image: container_image:container_image_tag
    commands:
      - echo World
  third-pipeline-step:
    when:
      event: push
      branch: main
    image: plugins/docker
    repo: registry.usw.co/uswitch/my_repository
    dockerfile: path/to/Dockerfile
    tags:
      - latest
      - "${DRONE_COMMIT}"
```

In each step, the `when` field defines when this pipeline step should be run; if the
condition is not satisfied, then the step is skipped. In the above example,
`first-pipeline-step` will run on every push to the Git repository. However,
`second-pipeline-step`, and `third-pipeline-step` will only run when the push is to the
`main` branch of the Git repository.

The `image` field defines a container image that the step will use. The Drone workspace
(shared volume) is mounted, and accessible to this image.

For `second-pipeline-step`, the image should have all the software packages needed to
run any `commands`. The `commands` field lists commands that Drone will execute in the
Drone workspace (by default). Any commands it runs must be defined in the `image`.

```{warning}
The container images are torn down between pipeline steps, so do not write anything
inside the image, instead write it to the Drone workspace.
```

For `third-pipeline-step` the `plugins/docker` image allows you to create a container
image from a Dockerfile that can be used in elsewhere both inside, and outside of this
pipeline.

The `dockerfile` field defines the path (relative to the Drone workspace) of the
Dockerfile used to create the container image. The `repo` field defines where the
created container image should be stored, along with what tags from the `tags` field;
`{DRONE_COMMIT}` is a special variable that contains the commit hash that triggered the
pipeline.

[drone-docs]: https://0-8-0.docs.drone.io
[drone-docs-workspace]: https://0-8-0.docs.drone.io/workspace
[notion-u]: https://www.notion.so/rvu/Getting-Started-with-U-ac4e2be3b0cf4ac8b880e4549bfaa1f8
[uswitch-drone]: https://github.com/uswitch/drone
