import pytest


def test_add_float() -> None:
    assert 0.1 + 0.2 == pytest.approx(0.3)
