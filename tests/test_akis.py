# test_akis.py
# oguz umut senel
# 20253004027

import itertools
import pytest
from uzay_oyunu.akis import fibonacci


# gorev 1 testleri
def test_fibonacci_next():
    # next ile ilk 3 elemani alma
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)


def test_fibonacci_islice():
    # islice ile ilk 12 degeri alma
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(itertools.islice(fibonacci(), 12)) == beklenen


def test_fibonacci_takewhile():
    # takewhile ile 100den kucuk sayilar
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    sonuc = list(itertools.takewhile(lambda x: x < 100, fibonacci()))
    assert sonuc == beklenen


def test_fibonacci_tek_kullanimlik():
    # uretec tukenince ayni yerden devam eder yani tek kullanimliktir
    g = fibonacci()
    ilk = list(itertools.islice(g, 5))
    ikinci = list(itertools.islice(g, 5))
    assert ilk == [0, 1, 1, 2, 3]
    assert ikinci == [5, 8, 13, 21, 34]
    assert ilk != ikinci
