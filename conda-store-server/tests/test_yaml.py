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
    # no comments or extra whitespace
    env_str_expected = """\
channels:
- conda-forge
dependencies:
- python
- pip:
  - nothing
- ipykernel
- pytest
- requests
description: ''
name: test-env
prefix: null
variables: null
"""
    yaml = Yaml()
    env_yaml = yaml.load(env_str)
    env_str_actual = yaml.dump(env_yaml)
    assert env_str_actual == env_str_expected

def test_yaml_load_error():
    s = """\
:
"""
    yaml = Yaml()
    with pytest.raises(YamlError) as e:
        yaml.load(s)
    assert "failed to load yaml" in str(e.value)

def test_yaml_dump_error():
    class Foo:
        pass
    data = Foo()  # cannot handle arbitrary objects
    yaml = Yaml()
    with pytest.raises(YamlError) as e:
        res = yaml.dump(data)
        print(res)
    assert "failed to dump yaml" in str(e.value)
