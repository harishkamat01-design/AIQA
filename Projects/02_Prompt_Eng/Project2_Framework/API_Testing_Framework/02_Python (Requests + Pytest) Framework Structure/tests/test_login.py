import requests

from utils.config_loader import ConfigLoader
from utils.data_loader import DataLoader
from utils.logger import create_logger
from utils.schema_validator import SchemaValidator


logger = create_logger(__name__)
config = ConfigLoader()
data = DataLoader()


def test_verify_login_returns_token():
    payload = data.get_payload('login')
    url = config.get_base_url() + config.get_endpoint('auth')
    headers = {'Content-Type': config.get_header('content_type')}

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    logger.info('Login response payload: %s', response_json)

    assert response.status_code == 200
    assert 'token' in response_json
    SchemaValidator.validate(response_json, 'schemas/login_schema.json')
