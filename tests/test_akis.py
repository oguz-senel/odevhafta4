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


# gorev 3 testleri
def test_boru_hatti_toplam_yakit():
    # dokumandaki ornek 88 toplam yakit
    from uzay_oyunu.akis import satirlari_oku, ayristir
    toplam = sum(y for _, _, y in ayristir(satirlari_oku("veri/seyir.txt")))
    assert toplam == 88


def test_boru_hatti_uzun_yolculuklar():
    # 10dan buyuk olanlar
    from uzay_oyunu.akis import satirlari_oku, ayristir, uzun_yolculuklar
    kayitlar = ayristir(satirlari_oku("veri/seyir.txt"))
    sonuc = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert sonuc == ['sirius', 'centauri', 'orion', 'kara_delik']


def test_boru_hatti_tembellik():
    # fonksiyonlarin liste degil generator dondurdugune bakalim
    import types
    from uzay_oyunu.akis import satirlari_oku, ayristir, uzun_yolculuklar
    g1 = satirlari_oku("veri/seyir.txt")
    assert isinstance(g1, types.GeneratorType)
    g2 = ayristir(g1)
    assert isinstance(g2, types.GeneratorType)
    g3 = uzun_yolculuklar(g2, 10)
    assert isinstance(g3, types.GeneratorType)


# gorev 4 testleri
def test_rota_sayaci_ornek_ciktilar():
    # pdf teki 10 baglantili ornek harita
    from uzay_oyunu.akis import rota_sayaci
    harita = {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "kara_delik": ["sirius"]
    }
    say = rota_sayaci(harita)
    assert say("dünya", 3) == 9
    assert say("dünya", 10) == 2185
    assert say("dünya", 40) == 16832258606399


def test_rota_sayaci_onbellek_kontrol():
    # galaksi json ile onbellek hits kontrolu
    import json
    from uzay_oyunu.akis import rota_sayaci
    with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as f:
        veri = json.load(f)
    say = rota_sayaci(veri["baglantilar"])
    assert say("dünya", 0) == 1
    deger = say("dünya", 3)
    assert deger > 0
    bilgi = say.cache_info()
    assert bilgi.hits > 0


# gorev 5 testleri
@pytest.fixture
def ornek_galaksi():
    return {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya", "orion"],
            "sirius": ["dünya", "orion", "kara_delik"],
            "orion": ["centauri", "sirius"],
            "kara_delik": ["sirius"]
        }
    }


def test_buyuk_harfli_gezegenler(ornek_galaksi):
    # soru 1 buyuk harf listesi
    from uzay_oyunu.istatistik import buyuk_harfli_gezegenler_map, buyuk_harfli_gezegenler_comp
    beklenen = ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]
    assert buyuk_harfli_gezegenler_map(ornek_galaksi) == beklenen
    assert buyuk_harfli_gezegenler_comp(ornek_galaksi) == beklenen


def test_cok_baglantili_gezegenler(ornek_galaksi):
    # soru 2 en az iki baglanti
    from uzay_oyunu.istatistik import cok_baglantili_gezegenler_filter, cok_baglantili_gezegenler_comp
    beklenen = ["dünya", "centauri", "sirius", "orion"]
    assert cok_baglantili_gezegenler_filter(ornek_galaksi, 2) == beklenen
    assert cok_baglantili_gezegenler_comp(ornek_galaksi, 2) == beklenen


def test_toplam_baglanti_sayisi(ornek_galaksi):
    # soru 3 toplam baglanti sayisi 10
    from uzay_oyunu.istatistik import toplam_baglanti_sayisi_reduce, toplam_baglanti_sayisi_sum
    assert toplam_baglanti_sayisi_reduce(ornek_galaksi) == 10
    assert toplam_baglanti_sayisi_sum(ornek_galaksi) == 10


def test_hizli_yolculuk_partial():
    # partial ile hiz 3 sabitlenmeli
    from uzay_oyunu.istatistik import yolculuk, hizli_yolculuk
    assert hizli_yolculuk.func == yolculuk
    assert hizli_yolculuk.keywords == {"hiz": 3.0}
    assert hizli_yolculuk(30) == 10.0
    assert hizli_yolculuk(15) == 5.0




