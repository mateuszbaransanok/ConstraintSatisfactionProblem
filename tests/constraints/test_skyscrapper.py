from unittest import TestCase
from unittest.mock import Mock

from csp.constraints.skyscrapper import IsSkyscrapperRule


class TestIsSkyscrapperRule(TestCase):
    def test__true(self) -> None:
        constraint = IsSkyscrapperRule(
            variables=[Mock(value=3), Mock(value=1), Mock(value=2), Mock(value=4)],
            number=2,
        )

        actual = bool(constraint)

        self.assertTrue(actual)

    def test__false(self) -> None:
        constraint = IsSkyscrapperRule(
            variables=[Mock(value=2), Mock(value=1), Mock(value=3), Mock(value=4)],
            number=2,
        )

        actual = bool(constraint)

        self.assertFalse(actual)

    def test__variable_none(self) -> None:
        constraint = IsSkyscrapperRule(
            variables=[Mock(value=None), Mock(value=1), Mock(value=2), Mock(value=3)],
            number=1,
        )

        actual = bool(constraint)

        self.assertTrue(actual)
