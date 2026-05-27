def correct_sentence(text: str) -> str:
    if not text:
        return ""
    corrected = text[0].upper() + text[1:]
    if not corrected.endswith('.'):
        corrected += '.'  
    return corrected
