# yardimci araclar modulu
# oguz umut senel

import time


def hamle_sayaci():
    """her cagrilinca 1 artan sayac fonksiyonu dondurur"""
    sayac = 0

    def artir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return artir


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """baglanti sayisina gore azalan esitse alfabetik siralar"""
    baglantilar = galaksi["baglantilar"]

    sonuc = sorted(baglantilar.keys(),
                   key=lambda g: (-len(baglantilar[g]), g))
    return sonuc


# bonus sure olcer
def sure_olc(fonksiyon):
    """fonksiyonun calisma suresini olcen sarmalayici dondurur"""
    def sarmalayici(*args, **kwargs):
        bas = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bit = time.time()
        print(f"{fonksiyon.__name__} {bit - bas:.6f} saniye surdu")
        return sonuc
    return sarmalayici


if __name__ == "__main__":
    # sayac denemesi
    s = hamle_sayaci()
    print(s())
    print(s())
    print(s())

    from uzay_oyunu.oyun import galaksi_yukle
    g = galaksi_yukle()
    print(en_bagli_gezegenler(g))

    # bonus kismi
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    print(en_bagli_gezegenler(g))
