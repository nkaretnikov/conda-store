from ruamel.yaml import YAML
from io import StringIO


class YamlError(Exception):
    pass


class Yaml:
    def __init__(self, typ="rt"):
        # 'rt' keeps comments and empty lines
        self.typ = typ

    def load(self, stream):
        try:
            yaml = YAML(typ=self.typ)
            return yaml.load(stream)
        except Exception as e:
            raise YamlError("failed to load yaml") from e

    def dump(self, data):
        # Note: writing to a user-provided stream would be more efficient, but
        # callers expect a value as the result.
        # https://yaml.readthedocs.io/en/latest/example.html#output-of-dump-as-a-string
        stream = StringIO()
        try:
            yaml = YAML()
            yaml.dump(data, stream=stream)
            return stream.getvalue()
        except Exception as e:
            raise YamlError("failed to dump yaml") from e
