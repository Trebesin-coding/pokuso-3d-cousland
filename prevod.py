def na_binarni(cislo: int) -> str:
    """Převede nezáporné celé číslo na binární zápis bez prefixu."""
    if cislo < 0:
        raise ValueError("Očekávám nezáporné číslo.")

    if cislo == 0:
        return "0"

    cislice = []
    while cislo > 0:
        cislice.append(str(cislo % 2))
        cislo //= 2

    return "".join(reversed(cislice))
