import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "assignments/4-261109/10.py"


class MultiplicationTableTest(unittest.TestCase):
    def run_table(self, n):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], input=f"{n}\n",
            capture_output=True, text=True, timeout=5,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def test_sample(self):
        self.assertEqual(self.run_table(3), "1*1=1\n1*2=2 2*2=4\n1*3=3 2*3=6 3*3=9\n")

    def test_all_valid_inputs(self):
        for n in range(1, 10):
            with self.subTest(n=n):
                output = self.run_table(n)
                self.assertTrue(output.endswith("\n"))
                rows = output.splitlines()
                self.assertEqual(len(rows), n)
                for i, row in enumerate(rows, 1):
                    terms = row.split(" ")
                    self.assertEqual(len(terms), i)
                    for j, term in enumerate(terms, 1):
                        self.assertEqual(term, f"{j}*{i}={j*i}")


if __name__ == "__main__":
    unittest.main()
