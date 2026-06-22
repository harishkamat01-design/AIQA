import requests

from utils.config_loader import ConfigLoader
from utils.data_loader import DataLoader
from utils.logger import create_logger


logger = create_logger(__name__)
config = ConfigLoader()
data = DataLoader()


def test_create_booking_returns_booking_id():
    payload = data.get_payload('booking')
    url = config.get_base_url() + config.get_endpoint('booking')
    headers = {
        'Content-Type': config.get_header('content_type'),
        'Accept': config.get_header('content_type')
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    logger.info('Create booking response: %s', response_json)

    assert response.status_code == 200
    assert 'bookingid' in response_json
    assert isinstance(response_json['bookingid'], int)
