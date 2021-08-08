import yaml


class Utils:
    @classmethod
    def get_data(self, filepath):
        with open(filepath) as f:
            return yaml.safe_load(f)
