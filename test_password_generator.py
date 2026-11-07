import contextlib
import io
from pathlib import Path
import runpy
import string
import unittest


class PasswordGeneratorTests(unittest.TestCase):
    def setUp(self):
        script = Path(__file__).with_name("Password Generator.py")
        with contextlib.redirect_stdout(io.StringIO()):
            self.result = runpy.run_path(str(script))

    def test_password_length(self):
        self.assertEqual(len(self.result["password"]), 12)

    def test_allowed_characters(self):
        allowed = string.ascii_letters + string.digits + string.punctuation
        self.assertTrue(
            all(character in allowed for character in self.result["password"])
        )


if __name__ == "__main__":
    unittest.main()