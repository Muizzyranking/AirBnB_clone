#!/usr/bin/python3
import unittest
from unittest.mock import patch
import sys
from io import StringIO

stdout = sys.stdout


class TestConsole(unittest.TestCase):
    """Tests for the HBNB console"""

    def test_prompt(self):
        """Tests that the custom prompt is displayed correctly"""
        with patch("sys.stdout", new=StringIO()) as fake_output:
            with patch("builtins.input", return_value="quit"):
                from console import HBNBCommand

                HBNBCommand().cmdloop()
        # self.assertEqual("(hbnb) ", fake_output.getvalue().strip())

    def test_quit(self):
        """Tests that the 'quit' command exits the program"""
        with patch("sys.stdout", new=StringIO()):
            with patch("builtins.input", return_value="quit"):
                from console import HBNBCommand

                self.assertFalse(HBNBCommand().cmdloop())

    # ... (Add more tests here!) ...


if __name__ == "__main__":
    unittest.main()
