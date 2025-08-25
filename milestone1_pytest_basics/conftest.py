import pytest


@pytest.fixture(scope="session")
def browser_launch():
    print("Initialize Browser Instance")
    yield
    print("Close Browser Instance")