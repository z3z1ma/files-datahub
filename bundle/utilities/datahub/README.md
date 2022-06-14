# Datahub

[Datahub](https://datahubproject.io/) helps data teams centrally track, manage, and discover their data assets.

> DataHub is an open-source metadata platform for the modern data stack. Read about the architectures of different metadata systems and why DataHub excels [here](https://engineering.linkedin.com/blog/2020/datahub-popular-metadata-architectures-explained). Also read our [LinkedIn Engineering blog post](https://engineering.linkedin.com/blog/2019/data-hub), check out our [Strata presentation](https://speakerdeck.com/shirshanka/the-evolution-of-metadata-linkedins-journey-strata-nyc-2019) and watch our [Crunch Conference Talk](https://www.youtube.com/watch?v=OB-O0Y6OYDE). You should also visit [DataHub Architecture](https://datahubproject.io/docs/architecture/architecture) to get a better understanding of how DataHub is implemented.

## Adding and Installing

Install with Meltano:

```shell
meltano add utility datahub
# now try it out!
meltano invoke datahub --help
```

If you are using Datahub, you likely need specific extras which let you ingest metadata from specific sources.
Any additional packages you may want can be added too by configuring
a custom `pip_url` for the `datahub` utility:

```shell
# set the _pip_url extra setting
meltano config datahub set _pip_url "datahub[rest,bigquery,dbt]"
# re-install the datahub plugin for changes to take effect
meltano install utility datahub
```

## Getting Started

Initialise your Datahub project:

```shell
meltano config datahub set gms_host datahub.yourserver.com/api/gms
meltano config datahub set gms_token yourPAT
# Alternatively if metadata authentication is off
meltano config datahub set gms_host datahub.yourserver.com:8000
```

Congratulations, you can now interact with your datahub instance through Meltano:

```shell
# check what plugins you have installed vs whats available
meltano invoke datahub check plugins
# ingest metadata!
meltano invoke datahub ingest run -c path/to/config.yml
```

See how to start creating ingestion recipes [here](https://datahubproject.io/docs/metadata-ingestion)!

Add commands to your meltano project yml like this:

```shell
plugins:
  utilities:
  - name: datahub
    commands:
      dbt-ingest: ingest run --config ${MELTANO_PROJECT_ROOT}/utilities/datahub/dbt.dhub.yml
    # ...more commands below pointing to ingestion recipes
```
