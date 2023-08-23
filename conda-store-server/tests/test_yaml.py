import pytest

from conda_store_server.yaml import Yaml, YamlError


def test_yaml_round_trip():
    env_str = """\
channels:
  - conda-forge
dependencies:
  - python
  - pip:
    - nothing
  - ipykernel
  # tests
  - pytest

  - requests  # for app

# other fields
description: ''
name: test-env    # required
prefix: null
variables: null
"""
    # Note: comments and empty lines are preserved. But the number of spaces
    # before the first comment is different and null is not present.
    env_str_expected = """\
channels:
- conda-forge
dependencies:
- python
- pip:
  - nothing
- ipykernel
  # tests
- pytest

- requests    # for app

# other fields
description: ''
name: test-env    # required
prefix:
variables:
"""
    yaml = Yaml()
    env_yaml = yaml.load(env_str)
    env_str_actual = yaml.dump(env_yaml)
    assert env_str_actual == env_str_expected


YAML_NO_KEY = """\
:
"""


def test_yaml_load_error():
    # only an error with safe parsing
    yaml = Yaml(typ='safe')
    with pytest.raises(YamlError) as e:
        yaml.load(YAML_NO_KEY)
    assert "failed to load yaml" in str(e.value)


def test_yaml_load_no_error():
    # not an error with rt parsing
    yaml = Yaml(typ='rt')
    res = yaml.load(YAML_NO_KEY)
    assert res == {None: None}


def test_yaml_dump_error():
    class Foo:
        pass
    data = Foo()  # cannot handle arbitrary objects
    yaml = Yaml()
    with pytest.raises(YamlError) as e:
        res = yaml.dump(data)
        print(res)
    assert "failed to dump yaml" in str(e.value)
