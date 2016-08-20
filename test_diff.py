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

    def test_totally_different(self):
        diff_object = diff.DiffStrings('foo', 'bar')
        assert diff_object.result == '< foo\n> bar'

    def test_compare_prefix_to_full_string(self):
        diff_object = diff.DiffStrings('some', 'something')
        assert diff_object.result == '> thing'
        diff_object = diff.DiffStrings('something', 'some')
        assert diff_object.result == '< thing'

    def test_compare_suffix_to_full_string(self):
        diff_object = diff.DiffStrings('thing', 'something')
        assert diff_object.result == '> thing'
        diff_object = diff.DiffStrings('something', 'thing')
        assert diff_object.result == '< thing'

    #def test_suffix_difference(self):
    #    diff_object = diff.DiffStrings('this', 'that')
    #    assert diff_object.result == '< is\n> at'

    #def test_prefix_difference(self):
    #    diff_object = diff.DiffStrings('what', 'that')
    #    assert diff_object.result == '< w\n> t'

