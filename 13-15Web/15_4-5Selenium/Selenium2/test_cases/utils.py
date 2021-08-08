import yaml


class Utils:
    @classmethod
    def get_data(self, filestream):
        with open(filestream) as d:
            return yaml.safe_load(d)
