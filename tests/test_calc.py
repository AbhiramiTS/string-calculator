from calc import calc
import unittest

class CalcTests(unittest.TestCase):
    def test_empty_string(self):
        """it should return 0 if the string is empty"""
        assert calc.add('') == 0

    def test_add_two_numbers(self):
        """it should add 2 numbers in a comma separated string"""
        assert calc.add('1, 2') == 3

    def test_add_n_numbers(self):
        """Allow the Add method to handle an unknown amount of numbers"""
        assert calc.add('1, 2, 3') == 6

    def test_new_lines(self):
        """Allow the Add method to handle new lines between numbers (instead of commas)"""
        assert calc.add('1\n2,3') == 6

    def test_different_delimiters(self):
        """it should be able handle different delimiters"""
        assert calc.add('//;\n1;2') == 3

    def test_bigger_than_1000(self):
        """Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2"""
        assert calc.add('//;\n1000,1;2') == 3

    def test_delimiters_n_length(self):
        """Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6"""
        assert calc.add('//[***]\n1***2***3') == 6

    def test_multiple_delimiters(self):
        """handle multiple delimiters with length longer than one char"""
        assert calc.add('//[*][%]\n1*2%3') == 6