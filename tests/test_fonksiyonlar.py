# testler

import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu, galaksi_kur
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler


# envanter testleri

def test_envanter_hepsi_var():
    assert envanter_metni(True, True, True) == "Sende: bol kredi, güçlü motorlar, yetenekli bir pilot"

def test_envanter_kredi_pilot():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"

def test_envanter_hic_yok():
    assert envanter_metni(False, False, False) == ""

def test_envanter_sadece_motor():
    assert envanter_metni(False, True, False) == "Sende: güçlü motorlar"


# hedef menusu testleri

def test_menu_iki_hedef():
    sonuc = hedef_menusu(["centauri", "sirius"])
    assert sonuc == "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"

def test_menu_bos():
    assert hedef_menusu([]) == "Nereye gitmek istersin?"

def test_menu_numaralama():
    sonuc = hedef_menusu(["a", "b", "c"])
    assert "[1] a" in sonuc
    assert "[3] c" in sonuc


# galaksi testleri

def test_galaksi_konum_yakit():
    g = galaksi_kur(["dünya", "mars"], {"dünya": ["mars"], "mars": []}, "dünya", yakit=100)
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100

def test_galaksi_yakit_varsayilan():
    g = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g["yakit"] == 50

def test_galaksi_hata():
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {}, "plüton")


# sayac testleri

def test_sayac_artis():
    s = hamle_sayaci()
    assert s() == 1
    assert s() == 2
    assert s() == 3

def test_sayac_bagimsiz():
    s1 = hamle_sayaci()
    s2 = hamle_sayaci()
    s1()
    s1()
    assert s2() == 1


# en bagli gezegenler testi

def test_en_bagli_siralama():
    g = galaksi_kur(
        ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya", "sirius", "orion"],
            "sirius": ["dünya", "centauri", "orion", "kara_delik"],
            "orion": ["centauri", "sirius"],
            "kara_delik": ["sirius"],
        },
        "dünya", yakit=100
    )
    assert en_bagli_gezegenler(g) == ["sirius", "centauri", "dünya", "orion", "kara_delik"]
