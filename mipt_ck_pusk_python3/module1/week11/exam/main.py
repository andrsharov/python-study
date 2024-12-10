def caps(s: str) -> str:
    if type(s) != str:
        raise TypeError('На входе ожидалась строка')
    return s.upper()