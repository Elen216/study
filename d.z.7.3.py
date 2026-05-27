def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) >= 2:
        first_idx = text.find(symbol)
        second_idx = text.find(symbol, first_idx + 1)
        return second_idx
    return None
