import yaml

import pytest


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
    env_yaml = yaml.safe_load(env_str)
    env_str_actual = yaml.dump(env_yaml)
    assert env_str_actual == env_str_expected
