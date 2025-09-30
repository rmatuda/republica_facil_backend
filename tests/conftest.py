import pytest
from fastapi.testclient import TestClient

from republica_facil.app import app


@pytest.fixture
def client():
    return TestClient(app)
