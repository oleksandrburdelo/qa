import pytest

from entities.person import Person
from infrastructure.people_service import PeopleService


@pytest.fixture(scope="session")
def people_service() -> PeopleService:
    yield PeopleService()


@pytest.fixture
def first_person():
    yield Person(
        name="C-3PO",
        height="167",
        mass="75",
        hair_color="n/a",
        skin_color="gold",
        eye_color="yellow",
        birth_year="112BBY",
        gender="n/a",
    )