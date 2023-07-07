from unittest import TestCase
from unittest.mock import Mock

from csp.constraints.unique import IsUnique


class TestIsUnique(TestCase):
    def test__true(self) -> None:
        constraint = IsUnique(
            variables=[Mock(value=3), Mock(value=5), Mock(value=6), Mock(value=4)],
        )

        actual = bool(constraint)

        self.assertTrue(actual)

    def test__false(self) -> None:
        constraint = IsUnique(
            variables=[Mock(value=3), Mock(value=5), Mock(value=3), Mock(value=4)],
        )

        actual = bool(constraint)

        self.assertFalse(actual)

    def test__variable_none(self) -> None:
        constraint = IsUnique(
            variables=[Mock(value=3), Mock(value=5), Mock(value=None), Mock(value=4)],
        )

        actual = bool(constraint)

        self.assertTrue(actual)
