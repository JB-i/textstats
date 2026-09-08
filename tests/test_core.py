import pytest

from textstats import char_frequencies, longest_word, word_count


def test_longest_word_rejects_empty():
    with pytest.raises(ValueError):
        longest_word("")


@pytest.mark.parametrize("text,expected", [
    ("", 0),
    ("one", 1),
    ("the end.", 2),
])
def test_word_count(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize("text,expected", [
    ("", {}),
    ("Hello", {"h": 1, "e": 1, "l": 2, "o": 1}),
    ("A a\tB\nb", {"a": 2, "b": 2}),
])
def test_char_frequencies(text, expected):
    assert char_frequencies(text) == expected