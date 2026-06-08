from utilities.config_reader import ConfigReader

def test_read_config():

    print(ConfigReader.get_base_url())
    print(ConfigReader.get_browser())

    assert ConfigReader.get_browser() == "chrome"