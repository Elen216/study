def first_word(text: str) -> str:
    cleaned_text = text.replace('.', ' ')
    trimmed_text = cleaned_text.strip()
    words = trimmed_text.split()
    if words:
        return words[0].rstrip(',')
    return ""
