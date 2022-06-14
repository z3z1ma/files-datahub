from setuptools import setup, find_packages

setup(
    name="files-datahub",
    version="0.1",
    description="Meltano project files for Datahub",
    packages=find_packages(),
    package_data={
        "bundle": [
            "utilities/datahub/dbt.dhub.yml"
            "utilities/datahub/README.md"
        ]
    },
)
