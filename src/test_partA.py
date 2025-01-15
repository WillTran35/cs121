import unittest
from PartA import tokenize, computeWordFrequencies, print_frequencies
from unittest.mock import patch
import io


class TestTokenize(unittest.TestCase):

    def test_tokenize(self):
        # Test text file contents
        test_text = "Hello world! This is a test file. Apple apple Apple."

        # Simulating file reading (mocking the file reading part)
        with open('testfile.txt', 'w') as file:
            file.write(test_text)

        # Call the tokenize function
        tokens = tokenize('testfile.txt')

        # Check if tokens are correct
        self.assertEqual(tokens, ['hello', 'world', 'this', 'is', 'a', 'test', 'file', 'apple', 'apple', 'apple'])

    def test_non_english_characters(self):
        # Test file with non-English characters
        test_text = "Héllo wørld! Tést fïle."

        with open('testfile.txt', 'w') as file:
            file.write(test_text)

        # Call the tokenize function
        tokens = tokenize('testfile.txt')

        # Check that non-English characters are skipped and no errors occur
        self.assertEqual(tokens, ["h", "llo", "w", "rld", "t", "st", "f", "le"])

    def test_whitespace(self):
        # Test file with spaces, newlines, and tabs
        test_text = "   Hello    world!  \nThis\tis a test file.   "

        with open('testfile.txt', 'w') as file:
            file.write(test_text)

        # Call the tokenize function
        tokens = tokenize('testfile.txt')

        # Check if the tokens list doesn't include spaces, newlines, or tabs
        self.assertEqual(tokens, ['hello', 'world', 'this', 'is', 'a', 'test', 'file'])

    def test_blank_file(self):
        # Test an empty file
        with open('testfile.txt', 'w') as file:
            file.write('')

        # Call the tokenize function
        tokens = tokenize('testfile.txt')

        # Check if the file is empty, the tokens list should also be empty
        self.assertEqual(tokens, [])

    def test_special_characters(self):
        # Test file with special characters and punctuation
        test_text = "Can’t, Ma-ma tree"

        with open('testfile.txt', 'w') as file:
            file.write(test_text)

        # Call the tokenize function
        tokens = tokenize('testfile.txt')

        # Check if the tokens are correctly extracted and special characters are handled
        self.assertEqual(tokens, ['can', 't', 'ma', 'ma', 'tree'])

    def test_combined_text_and_numbers(self):
        # Test file with alphanumeric combinations
        test_text = "Washington & hi all-the seâtences"

        with open('testfile.txt', 'w') as file:
            file.write(test_text)

        # Call the tokenize function
        tokens = tokenize('testfile.txt')

        # Check if the tokens are correctly handled
        self.assertEqual(tokens, ['washington', 'hi', 'all', 'the', 'se', 'tences'])

    def test_numbers_and_hyphens(self):
        # Test file with numbers and hyphens in tokens
        test_text = "Sad12-sad"

        with open('testfile.txt', 'w') as file:
            file.write(test_text)

        # Call the tokenize function
        tokens = tokenize('testfile.txt')

        # Check if the tokens list handles numbers and hyphens correctly
        self.assertEqual(tokens, ['sad12', 'sad'])

    def test_case_variation(self):
        # Test case with different cases of the same word
        test_text = "Apple, apple, APPle"

        with open('testfile.txt', 'w') as file:
            file.write(test_text)

        # Call the tokenize function
        tokens = tokenize('testfile.txt')

        # Check if case variations are normalized
        self.assertEqual(tokens, ['apple', 'apple', 'apple'])


class TestComputeWordFrequencies(unittest.TestCase):
    def test_computeWordFrequencies(self):
        tokens = ['hello', 'world', 'hello', 'apple', 'apple', 'apple']
        frequencies = computeWordFrequencies(tokens)

        # Expected frequency count
        expected = {'hello': 2, 'world': 1, 'apple': 3}

        self.assertEqual(frequencies, expected)

    def test_empty_list(self):
        # Test with an empty list
        tokens = []
        frequencies = computeWordFrequencies(tokens)

        # Expected empty frequency count
        expected = {}

        self.assertEqual(frequencies, expected)

    def test_single_word(self):
        # Test with only one word in the list
        tokens = ['apple']
        frequencies = computeWordFrequencies(tokens)

        # Expected frequency count for single word
        expected = {'apple': 1}

        self.assertEqual(frequencies, expected)

    def test_multiple_occurrences(self):
        # Test with multiple occurrences of the same word
        tokens = ['apple', 'apple', 'apple']
        frequencies = computeWordFrequencies(tokens)

        # Expected frequency count for repeated word
        expected = {'apple': 3}

        self.assertEqual(frequencies, expected)

    def test_mixed_case_words(self):
        # Test file with non-English characters
        test_text = "Apple, apple, APPLE"

        with open('testfile.txt', 'w') as file:
            file.write(test_text)

        # Call the tokenize function
        tokens = tokenize('testfile.txt')

        # Check that non-English characters are skipped and no errors occur
        self.assertEqual(tokens, ["apple", "apple", "apple"])

        frequencies = computeWordFrequencies(tokens)

        # Expected frequency count, case insensitive
        expected = {'apple': 3}

        self.assertEqual(frequencies, expected)

    def test_multiple_unique_words(self):
        # Test with multiple unique words
        tokens = ['apple', 'banana', 'cherry', 'apple']
        frequencies = computeWordFrequencies(tokens)

        # Expected frequency count
        expected = {'apple': 2, 'banana': 1, 'cherry': 1}

        self.assertEqual(frequencies, expected)

    def test_non_alphanumeric_tokens(self):
        # Test with alphanumeric tokens (including numbers)
        tokens = ['apple1', 'banana2', 'apple1']
        frequencies = computeWordFrequencies(tokens)

        # Expected frequency count
        expected = {'apple1': 2, 'banana2': 1}

        self.assertEqual(frequencies, expected)


class TestPrintFrequencies(unittest.TestCase):
    def test_print_frequencies(self):
        frequencies = {'hello': 2, 'apple': 3, 'world': 1}

        # Mock print to capture output
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_frequencies(frequencies)
            output = fake_out.getvalue().strip()

        # Expected output format
        expected_output = "apple - 3\nhello - 2\nworld - 1"

        self.assertEqual(output, expected_output)

    def test_empty_frequencies(self):
        # Test with empty frequency dictionary
        frequencies = {}

        # Mock print to capture output
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_frequencies(frequencies)
            output = fake_out.getvalue().strip()

        # Expected output is nothing (empty)
        expected_output = ""

        self.assertEqual(output, expected_output)

    def test_single_word_frequency(self):
        # Test with a single word frequency
        frequencies = {'apple': 3}

        # Mock print to capture output
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_frequencies(frequencies)
            output = fake_out.getvalue().strip()

        # Expected output for single word frequency
        expected_output = "apple - 3"

        self.assertEqual(output, expected_output)

    def test_multiple_words_ordered(self):
        # Test with multiple words sorted by frequency (desc) and then alphabetically
        frequencies = {'apple': 3, 'banana': 2, 'cherry': 1}

        # Mock print to capture output
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_frequencies(frequencies)
            output = fake_out.getvalue().strip()

        # Expected output sorted by frequency, then alphabetically
        expected_output = "apple - 3\nbanana - 2\ncherry - 1"

        self.assertEqual(output, expected_output)

    def test_multiple_words_with_same_frequency(self):
        # Test with multiple words having the same frequency
        frequencies = {'apple': 2, 'banana': 2, 'cherry': 2}

        # Mock print to capture output
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_frequencies(frequencies)
            output = fake_out.getvalue().strip()

        # Expected output sorted alphabetically because frequencies are the same
        expected_output = "apple - 2\nbanana - 2\ncherry - 2"

        self.assertEqual(output, expected_output)

    def test_large_number_of_tokens(self):
        # Test with a large number of tokens
        frequencies = {f'word{i}': i for i in range(1, 11)}  # words 'word1' to 'word10'

        # Mock print to capture output
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_frequencies(frequencies)
            output = fake_out.getvalue().strip()

        # Expected output sorted by frequency, then alphabetically
        expected_output = "\n".join([f'word{i} - {i}' for i in range(10, 0, -1)])  # words from 'word10' to 'word1'

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
