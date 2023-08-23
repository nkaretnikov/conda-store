import yaml


class YamlError(Exception):
    pass


class Yaml:
    def load(self, stream):
        try:
            return yaml.safe_load(stream)
        except Exception as e:
            raise YamlError("failed to load yaml") from e

    def dump(self, data):
        try:
            return yaml.safe_dump(data)
        except Exception as e:
            raise YamlError("failed to dump yaml") from e
