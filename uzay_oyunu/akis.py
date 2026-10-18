# oguz umut senel
# 20253004027
# akis modulu - uretecler ve fonksiyonlar

from collections.abc import Generator
import itertools


def fibonacci() -> Generator[int, None, None]:
    """sonsuz fibonacci sayisi ureten fonksiyon"""
    a = 0
    b = 1
    while True:
        yield a
        gecici = a + b
        a = b
        b = gecici
