import pytest
import diff

class TestReadingFiles:
    def test_compares_nothing(self):
        diff_object = diff.DiffStrings('', '')
        assert diff_object.result == ''

    def test_compares_nothing_to_something(self):
        diff_object = diff.DiffStrings('', 'something')
        assert diff_object.result == '> something'
        diff_object = diff.DiffStrings('something', '')
        assert diff_object.result == '< something'
