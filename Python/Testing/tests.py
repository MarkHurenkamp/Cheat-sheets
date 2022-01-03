import unittest
from unittest import mock

import functions_to_test


class FunctionsToTest(unittest.TestCase):
    def test_addition(self):
        """Easiest example: add 1.2 and 2.5 and verify the result being 3.7"""
        self.assertEqual(functions_to_test.addition(1.2, 2.5), 3.7)

    def test_divide(self):
        """Divide 5 by 2 to get 2.5 and assert a zero division error is raised
        when dividing by zero."""
        self.assertEqual(functions_to_test.divide(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            functions_to_test.divide(5, 0)

    def test_divide_with_try_except(self):
        """Same as test_divide by caught the exception with a try/except block"""
        self.assertEqual(functions_to_test.divide_with_try_except(5, 2), 2.5)
        self.assertEqual(
            functions_to_test.divide_with_try_except(5, 0), "Can't divide by zero"
        )


class FileOperationsToTest(unittest.TestCase):
    def test_read_text_file_contents(self):
        """Assert the correct contents when reading a text file"""
        contents = "Test line 1\nTest line 2\nTest line 3"
        self.assertEqual(
            functions_to_test.read_text_file_contents(
                filename=r"Test files/samplefile.txt"
            ),
            contents,
        )

    def test_read_mocked_text_file_contents(self):
        """Assert the correct contents of a mocked text file.
        Mocking files is generally preferred over opening them for unit testing
        as it is much faster and it doesn't rely on the (test) files being available.
        """
        mocked_contents = "Mocked test line 1\nMocked test line 2"
        with mock.patch("builtins.open", mock.mock_open(read_data=mocked_contents)):
            self.assertEqual(
                functions_to_test.read_text_file_contents(filename=r"a mocked file"),
                mocked_contents,
            )

    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="some data")
    def test_read_mocked_text_file_contents2(self, m):
        """Assert the correct contents of a mocked text file.
        Mocking files is generally preferred over opening them for unit testing
        as it is much faster and it doesn't rely on the (test) files being available.
        """
        self.assertEqual(
                functions_to_test.read_text_file_contents(filename=r"a mocked file"),
                "some data",
            )

    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_write_mocked_text_file_content(self, mocked_open):
        """Assert the correct data is written to a mocked text file"""
        mocked_text_to_write = "Some text to write"
        handle = mocked_open()
        functions_to_test.write_data_to_text_file(filename=r"a mocked file", input=mocked_text_to_write)
        mocked_open.assert_called_with("a mocked file", 'w')
        handle.write.assert_called_with(mocked_text_to_write)
            

    def test_read_excel_file(self):
        """Assert the correct contents when reading an Excel file"""
        self.assertEqual(
            functions_to_test.read_excel_file_contents(
                filename=r"Test files/sample_excel_file.xlsx", sheetname="Sheet1", cell="B2"
            ),
            "Cell contents B2",
        )

if __name__ == "__main__":
    unittest.main()
