import pytest
import diff

class TestSingleLines:
    def test_compares_nothing(self):
        diff_object = diff.DiffStrings('', '')
        assert diff_object.result == ''

    def test_compares_nothing_to_something(self):
        diff_object = diff.DiffStrings('', 'something')
        assert diff_object.result == '> something'
        diff_object = diff.DiffStrings('something', '')
        assert diff_object.result == '< something'

    def test_simple_compare(self):
        diff_object = diff.DiffStrings('foo', 'bar')
        assert diff_object.result == '< foo\n> bar'
