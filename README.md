# files-datahub

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [Datahub](https://datahubproject.io/docs/).

Files:
- [`utilities`](./bundle/utilities/) (directory)
- [`utilities/datahub/`](./bundle/utilities/datahub/) (directory)
- [`utilities/datahub/README.md`](./bundle/utilities/datahub/README.md)
- [`utilities/datahub/dbt.dhub.yml`](./bundle/utilities/datahub/dbt.dhub.yml)

```py
# add datahub to your Meltano project (including this file bundle)
meltano add utility datahub
# add only this file bundle to your Meltano project
meltano add files datahub
```

We ship a predefined ingestion recipe for dbt artifacts. You must change the target_platform to your database [platform name](https://github.com/datahub-project/datahub/blob/master/metadata-service/war/src/main/resources/boot/data_platforms.json)

```yaml
source:
  type: "dbt"
  config:
    # Coordinates
    manifest_path: ${MELTANO_PROJECT_ROOT}/.meltano/transformers/dbt/target/manifest.json
    catalog_path: ${MELTANO_PROJECT_ROOT}/.meltano/transformers/dbt/target/catalog.json
    sources_path: ${MELTANO_PROJECT_ROOT}/.meltano/transformers/dbt/target/sources.json

    # TODO: Change me to the appropriate platform, ie. bigquery, postgres, etc.
    # https://github.com/datahub-project/datahub/blob/master/metadata-service/war/src/main/resources/boot/data_platforms.json
    target_platform: "CHANGE ME"
sink:
  type: datahub-rest
  config:
    server: ${DATAHUB_GMS_HOST}
    token: ${DATAHUB_GMS_TOKEN}
```
