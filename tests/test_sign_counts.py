import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "assignments/4-261109/8.py"


class SignCountsTest(unittest.TestCase):
    def test_counts_until_first_zero(self):
        cases = [
            ("1 -2 3 -4 5 0\n", "3 2\n"),
            ("0\n", "0 0\n"),
            ("1 2 3 0\n", "3 0\n"),
            ("-1 -2 -3 0\n", "0 3\n"),
            ("  1\t-2   3  0  \n", "2 1\n"),
            ("1 -2 0 3 -4\n", "1 1\n"),
            ("99999999999999999999 -99999999999999999999 0\n", "1 1\n"),
        ]
        for data, expected in cases:
            with self.subTest(data=data):
                result = subprocess.run(
                    [sys.executable, str(SCRIPT)], input=data,
                    capture_output=True, text=True, timeout=5,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, "")
                self.assertEqual(result.stdout, expected)


if __name__ == "__main__":
    unittest.main()
