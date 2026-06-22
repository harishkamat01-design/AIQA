import requests

from utils.config_loader import ConfigLoader
from utils.logger import create_logger


logger = create_logger(__name__)
config = ConfigLoader()


def test_get_booking_list():
    url = config.get_base_url() + config.get_endpoint('booking_list')
    headers = {'Accept': config.get_header('content_type')}

    response = requests.get(url, headers=headers)
    logger.info('Booking list response code: %s', response.status_code)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
