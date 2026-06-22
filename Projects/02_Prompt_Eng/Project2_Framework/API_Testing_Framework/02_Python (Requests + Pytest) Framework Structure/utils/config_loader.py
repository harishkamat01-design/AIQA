import yaml


class ConfigLoader:
    def __init__(self, path='config/config.yaml'):
        with open(path, 'r', encoding='utf-8') as stream:
            self.config = yaml.safe_load(stream)

    def get_base_url(self):
        return self.config['base_url']

    def get_endpoint(self, name):
        return self.config['endpoints'][name]

    def get_header(self, name):
        return self.config['headers'][name]
