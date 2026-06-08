from utilities.logger import get_logger

log = get_logger()

def test_logger():

    log.info("Framework Started")

    assert True