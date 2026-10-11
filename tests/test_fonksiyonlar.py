# testler

from uzay_oyunu.oyun import envanter_metni, hedef_menusu


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
