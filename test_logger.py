"""test_logger.py holds logging handler and config for the API test"""
import logging
from test_config import TEST_LOG

test_logger = logging.getLogger('API_TESTER')
handler = logging.FileHandler(TEST_LOG)
formatter = logging.Formatter('%(asctime)s %(name)-10s %(levelname)-6s %(message)s')
handler.setFormatter(formatter)
test_logger.addHandler(handler)
test_logger.setLevel(logging.DEBUG)