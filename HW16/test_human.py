import pytest

def test_01(human):
    """Test checks age of human"""
    assert human.age == 23


def test_02(human):
    """Test checks grow effect"""
    human.grow()
    assert human.age == 24


def test_03(human):
    """Test checks alive status"""
    assert human._Human__is_alive() is True


def test_04(human, monkeypatch):
    """Test checks age limit"""
    monkeypatch.setattr(
        human, '_Human__age', 101
    )
    human.grow()
    assert human._Human__status == "dead"


def test_05(human, monkeypatch):
    """Test checks dead status"""
    monkeypatch.setattr(Human, "_human__age", 100)
    human.grow()
    with pytest.raises(Exception):
        human._Human__is_alive()


def test_06(human):
    """Test checks alive status"""
    assert human._Human__is_alive() is True


def test_07(human):
    """Test checks correct gender"""
    assert human.gender == "male"


def test_08(human):
    """Test checks changing gender"""
    human.change_gender('female')
    assert human.gender == 'female'



def test_09(human):
    """
    This test check changing gender to incorrect gender
    """
    with pytest.raises(Exception):
        human.change_gender(" ")


def test_10(human):
    """
    This test check not correct gender
    """
    with pytest.raises(Exception):
        human._Human__validate_gender("empty")


