import pytest
from diff import DiffFiles

class TestReadingFiles:
    def test_compares_nothing(self):
        diff = DiffFiles('', '')
        assert diff.result == ''
