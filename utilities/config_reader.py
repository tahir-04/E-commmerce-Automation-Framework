import json

class ConfigReader:

    @staticmethod
    def read_config():

        with open("config/config.json", "r") as file:
            return json.load(file)

    @staticmethod
    def get_base_url():

        return ConfigReader.read_config()["base_url"]

    @staticmethod
    def get_browser():

        return ConfigReader.read_config()["browser"]

    @staticmethod
    def get_implicit_wait():

        return ConfigReader.read_config()["implicit_wait"]

    @staticmethod
    def get_page_load_timeout():

        return ConfigReader.read_config()["page_load_timeout"]