from unittest import TestCase
from unittest.mock import Mock

from csp.constraints.jolka import IsJolkaRule


class TestIsJolkaRule(TestCase):
    def test__true(self) -> None:
        constraint = IsJolkaRule(
            h_variable=Mock(value="BOAT"),
            h_index=2,
            v_variable=Mock(value="CAT"),
            v_index=1,
        )

        actual = bool(constraint)

        self.assertTrue(actual)

    def test__false(self) -> None:
        constraint = IsJolkaRule(
            h_variable=Mock(value="BOAT"),
            h_index=0,
            v_variable=Mock(value="CAT"),
            v_index=1,
        )

        actual = bool(constraint)

        self.assertFalse(actual)

    def test__variable_none(self) -> None:
        constraint = IsJolkaRule(
            h_variable=Mock(value=None),
            h_index=2,
            v_variable=Mock(value="CAT"),
            v_index=1,
        )

        actual = bool(constraint)

        self.assertTrue(actual)
