"""Tests with the unittest module.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 19_unittest.md.

From this_course you can also run:

    python tag4/19_unittest.py
"""

import io
import unittest


def mean(values):
    """Return the arithmetic mean of a non-empty series."""
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def within_tolerance(reading, reference, tolerance):
    """Return True when reading stays within tolerance of reference."""
    if tolerance < 0:
        raise ValueError("tolerance must not be negative")
    return abs(reading - reference) <= tolerance


class MeanTests(unittest.TestCase):
    """Checks for the mean function."""

    def test_two_values(self):
        """A series of 20 and 22 has the mean 21."""
        self.assertEqual(mean([20.0, 22.0]), 21.0)

    def test_one_value(self):
        """A single value is its own mean."""
        self.assertEqual(mean([20.0]), 20.0)

    def test_empty_series(self):
        """An empty series is rejected."""
        with self.assertRaises(ValueError):
            mean([])


class ToleranceTests(unittest.TestCase):
    """Checks for the tolerance comparison."""

    def test_inside(self):
        """A deviation of 0.4 is inside a tolerance of 0.5."""
        self.assertTrue(within_tolerance(20.4, 20.0, 0.5))

    def test_on_the_boundary(self):
        """A deviation equal to the tolerance is still inside."""
        self.assertTrue(within_tolerance(20.5, 20.0, 0.5))

    def test_outside(self):
        """A deviation of 1.0 is outside a tolerance of 0.5."""
        self.assertFalse(within_tolerance(21.0, 20.0, 0.5))

    def test_negative_tolerance(self):
        """A negative tolerance is rejected."""
        with self.assertRaises(ValueError):
            within_tolerance(20.0, 20.0, -0.1)


class FailureSample(unittest.TestCase):
    """One deliberate mismatch, used only to show a failure report."""

    def test_mismatch(self):
        """Fail on purpose so the report format is visible."""
        self.assertEqual(1, 2)


def main():
    """Show one failure report, then run the real test cases."""
    stream = io.StringIO()
    sample = unittest.defaultTestLoader.loadTestsFromTestCase(FailureSample)
    unittest.TextTestRunner(stream=stream, verbosity=2).run(sample)
    print("Example of a failing test:")
    print(stream.getvalue())

    suite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    suite.addTests(loader.loadTestsFromTestCase(MeanTests))
    suite.addTests(loader.loadTestsFromTestCase(ToleranceTests))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
