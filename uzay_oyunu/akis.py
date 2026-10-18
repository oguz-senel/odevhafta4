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


def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """her next cagrisinda yakiti tuketim kadar azaltip kalani verir sifirda durur"""
    kalan = yakit
    while kalan > 0:
        kalan = kalan - tuketim
        if kalan < 0:
            kalan = 0
        yield kalan


def satirlari_oku(yol: str) -> Generator[str, None, None]:
    """dosyadaki bos ve diyezle baslayan yorum satirlarini atlar"""
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if len(temiz) == 0:
                continue
            if temiz.startswith("#"):
                continue
            yield temiz


def ayristir(satirlar) -> Generator[tuple[str, str, int], None, None]:
    """satirlari kaynak hedef ve yakit olarak ayirir demet dondurur"""
    for s in satirlar:
        parcalar = s.split("->")
        kaynak = parcalar[0].strip()
        sag = parcalar[1].strip()
        sag_kisim = sag.split()
        hedef = sag_kisim[0]
        yakit = int(sag_kisim[1])
        yield (kaynak, hedef, yakit)


def uzun_yolculuklar(kayitlar, esik: int) -> Generator[tuple[str, str, int], None, None]:
    """yakiti verilen esikten buyuk olanlari secer"""
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit


def rota_sayaci(baglantilar: dict):
    """onbellekli rota sayisi bulucu fonksiyon"""
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """verilen gezegenden baslayip adim kadar giden farkli rotalarin sayisi"""
        if adim == 0:
            return 1
        toplam = 0
        komsular = baglantilar.get(gezegen, [])
        for k in komsular:
            toplam = toplam + rota_sayisi(k, adim - 1)
        return toplam

    return rota_sayisi



