ef popular_words(text: str, words: list) -> dict:
    text_lower = text.lower()
    words_in_text = text_lower.split()
    result = {}
    for word in words:
        result[word] = words_in_text.count(word)
    return result
