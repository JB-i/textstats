def char_frequencies(text: str) -> dict[str, int]:
    """Count of each character, ignoring whitespace and case."""
    frequencies = {}

    for char in text.lower():
        if not char.isspace():
            frequencies[char] = frequencies.get(char, 0) + 1

    return frequencies