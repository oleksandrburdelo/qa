import pytest
from human import Human


@pytest.fixture
def human() -> Human:
    yield Human("Oleksandr", 23, "male")

