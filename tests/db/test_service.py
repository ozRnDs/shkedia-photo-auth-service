from db.service import DBService
import pytest
from pydantic import BaseModel
from typing import Union

@pytest.fixture(scope="module")
def connection_fixture():
    credential_file_location = "/temp/postgres_credentials/postgres_credentials.json"
    yield credential_file_location

@pytest.fixture(scope="module")
def db_service_fixture(connection_fixture):
    db_fixture = DBService(credential_file_location=connection_fixture)
    yield db_fixture
    db_fixture.close()

    
def test_DBService_init(connection_fixture):

    new_db_object = DBService(credential_file_location=connection_fixture)
    



