import pytest
from textstats import word_count


@pytest.mark.parametrize("text,expected", [
    ("", 0),
    ("one", 1),
    ("the end.", 2),
    ("  espaces   en   trop ", 3)
])

def test_word_count(text, expected):
    """Test le comptage de mots."""
    assert word_count(text) == expected
