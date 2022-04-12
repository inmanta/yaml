# yaml Module

## Using this module

To load a yaml file
```inmanta
import yaml

# This loads the file in this module under 'files/test.yaml'
yaml_dict_a = yaml::load("test.yaml")

# This does the same
yaml_dict_b = yaml::loads(std::source("test.yaml"))

# This load from a string
yaml_dict_c = yaml::loads("""key: value""")

```

## Using this module to load a yaml inventory

[see examples/network_inventory](examples/network_inventory/README.md)

## Running tests

1. Setup a virtual env

```bash
mkvirtualenv inmanta-test -p python3
pip install -r requirements.dev.txt
pip install -r requirements.txt

mkdir /tmp/env
export INMANTA_TEST_ENV=/tmp/env
export INMANTA_MODULE_REPO=git@github.com:inmanta/
```

2. Run tests

```bash
pytest tests
```
