# gorev 4 tuzak testi

# eski hatali hali boyleydi
# def yakit_ekle(miktar, depo=[]):
#     depo.append(miktar)
#     return depo
# liste her cagrilista ayni kaldigi icin degerler ust uste birikiyordu

def yakit_ekle(miktar, depo=None):
    """depoya yakit ekler none kalibi ile duzeltildi"""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_tek_ekleme():
    assert yakit_ekle(10) == [10]

def test_iki_cagri_ayri():
    # eski kodda burasi [10, 20] oluyordu
    yakit_ekle(10)
    sonuc = yakit_ekle(20)
    assert sonuc == [20]

def test_kendi_deposu():
    depo = [5]
    sonuc = yakit_ekle(10, depo)
    assert sonuc == [5, 10]
