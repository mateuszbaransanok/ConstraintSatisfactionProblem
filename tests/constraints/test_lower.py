from unittest import TestCase
from unittest.mock import Mock

from csp.constraints.lower import IsLower


class TestIsLower(TestCase):
    def test__true(self) -> None:
        constraint = IsLower(
            lower=Mock(value=3),
            greater=Mock(value=4),
        )

        actual = bool(constraint)

        self.assertTrue(actual)

    def test__false(self) -> None:
        constraint = IsLower(
            lower=Mock(value=4),
            greater=Mock(value=3),
        )

        actual = bool(constraint)

        self.assertFalse(actual)

    def test__variable_none(self) -> None:
        constraint = IsLower(
            lower=Mock(value=None),
            greater=Mock(value=4),
        )

        actual = bool(constraint)

        self.assertTrue(actual)
