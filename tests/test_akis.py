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


# gorev 2 testleri
def test_yakit_gostergesi_ornek():
    # dokumandaki ornek 100 yakit 30 tuketim
    from uzay_oyunu.akis import yakit_gostergesi
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_yakit_gostergesi_stop_iteration():
    # yakit sifir olunca bir sonraki cagri stopiteration firlatmali
    from uzay_oyunu.akis import yakit_gostergesi
    g = yakit_gostergesi(20, 10)
    assert next(g) == 10
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)


def test_yakit_gostergesi_bastansifir():
    # bastan 0 olan yakit icin bos liste uretmeli
    from uzay_oyunu.akis import yakit_gostergesi
    assert list(yakit_gostergesi(0, 10)) == []


def test_yakit_gostergesi_fazla_tuketim():
    # tuketim yakittan coksa 0 uretip durmali
    from uzay_oyunu.akis import yakit_gostergesi
    assert list(yakit_gostergesi(15, 25)) == [0]

