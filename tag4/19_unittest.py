# `unittest`
#
# Tag 4, Einheit 19
# Skript: `tag4/19_unittest.py`
#
# Ziel
#
# Du liest einen Testfall, erkennst einen fehlgeschlagenen Vergleich an der Meldung und lässt die Tests für Mittelwert und Toleranz laufen.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.
#
# Im Terminal, aus dem Ordner `python_basics-nov-2026`:
#
#     python -m unittest tag4/19_unittest.py

# Aufbau
#
# `unittest.TestCase` sammelt Prüfungen. Jede Methode, deren Name mit `test` beginnt, ist ein Test. `self.assertEqual` verlangt Gleichheit. `self.assertTrue` und `self.assertFalse` verlangen einen Wahrheitswert.
#
# `with self.assertRaises(ValueError)` verlangt, dass der eingerückte Aufruf `ValueError` auslöst. Bleibt die Ausnahme aus, schlägt der Test fehl.
#
# Die Funktionen `mean` und `within_tolerance` sind dieselben Rechnungen wie in `tag3/measurement.py`. Sie stehen hier noch einmal, damit der Test ohne Import lesbar bleibt.
#
# `FailureSample` vergleicht 1 mit 2. Dieser Test gehört nicht zur Messaufgabe. Er zeigt die Meldung: `AssertionError`, die beiden Werte und den Namen `test_mismatch`. Die Tests von `MeanTests` und `ToleranceTests` müssen bestehen.

# Was die Tests abdecken
#
# - Mittelwert von 20 und 22 ist 21.
# - Eine einzelne Messung ist ihr eigener Mittelwert.
# - Eine leere Reihe löst `ValueError` aus.
# - Die Abweichung 0,4 liegt bei Toleranz 0,5 innen.
# - Die Abweichung 0,5 liegt auf der Grenze und gilt als innen.
# - Die Abweichung 1,0 liegt außen.
# - Eine negative Toleranz löst `ValueError` aus.
#
# Das sind die drei Lagen aus Einheit 18: üblicher Fall, Rand und Grenze.

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
        self.assertEqual(mean([20.0, 22.0]), 21.0)

    def test_one_value(self):
        self.assertEqual(mean([20.0]), 20.0)

    def test_empty_series(self):
        with self.assertRaises(ValueError):
            mean([])


class ToleranceTests(unittest.TestCase):
    """Checks for the tolerance comparison."""

    def test_inside(self):
        self.assertTrue(within_tolerance(20.4, 20.0, 0.5))

    def test_on_the_boundary(self):
        self.assertTrue(within_tolerance(20.5, 20.0, 0.5))

    def test_outside(self):
        self.assertFalse(within_tolerance(21.0, 20.0, 0.5))

    def test_negative_tolerance(self):
        with self.assertRaises(ValueError):
            within_tolerance(20.0, 20.0, -0.1)


if __name__ == "__main__":
    class FailureSample(unittest.TestCase):
        """One deliberate mismatch, so the report format is visible."""

        def test_mismatch(self):
            self.assertEqual(1, 2)

    stream = io.StringIO()
    sample = unittest.defaultTestLoader.loadTestsFromTestCase(FailureSample)
    unittest.TextTestRunner(stream=stream, verbosity=2).run(sample)
    print("Example of a failing test:")
    print(stream.getvalue())

# Übung
#
# Trag in `expected` den Mittelwert von 20, 21 und 22 ein. Das ist 21. Die Lösung unten enthält die fertige Klasse. Der Lauf am Ende prüft die fertige Fassung.

# gegeben:
class ExtraTests(unittest.TestCase):
    """One more mean check."""

    def test_three_values(self):
        # lösung ab hier:
        expected =
        self.assertEqual(mean([20.0, 21.0, 22.0]), expected)

# Lösung

class ExtraTests(unittest.TestCase):
    """One more mean check."""

    def test_three_values(self):
        self.assertEqual(mean([20.0, 21.0, 22.0]), 21.0)


if __name__ == "__main__":
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(MeanTests))
    suite.addTests(loader.loadTestsFromTestCase(ToleranceTests))
    suite.addTests(loader.loadTestsFromTestCase(ExtraTests))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print("solution", "ok" if result.wasSuccessful() else "failed")

# Damit ist der Kurs durch. Die Zusammenfassung steht in `tag4/Tag4_Zusammenfassung.md`.
