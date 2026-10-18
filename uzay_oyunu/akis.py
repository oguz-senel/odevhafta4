# oguz umut senel
# 20253004027
# akis modulu - uretecler ve boru hatti

from typing import Generator
import itertools


# gorev 1 sonsuz fibonacci
def fibonacci() -> Generator:
    """sonsuz fibonacci sayisi ureten fonksiyon"""
    a = 0
    b = 1
    while True:
        yield a
        gecici = a + b
        a = b
        b = gecici


# gorev 2 yakit gostergesi
def yakit_gostergesi(yakit: int, tuketim: int) -> Generator:
    """her next cagrisinda yakiti tuketim kadar azaltip kalani verir sifirda durur"""
    kalan = yakit
    while kalan > 0:
        kalan = kalan - tuketim
        # eksiye duserse sifir yapalim
        if kalan < 0:
            kalan = 0
        yield kalan


# gorev 3 seyir defteri boru hatti
def satirlari_oku(yol: str) -> Generator:
    """dosyadaki bos ve diyezle baslayan yorum satirlarini atlar"""
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            # eger satir bossa atla
            if len(temiz) == 0:
                continue
            # eger yorum satiriysa atla
            if temiz.startswith("#"):
                continue
            yield temiz


def ayristir(satirlar) -> Generator:
    """satirlari kaynak hedef ve yakit olarak ayirir demet dondurur"""
    for s in satirlar:
        # orn dunya -> sirius 12
        parcalar = s.split("->")
        kaynak = parcalar[0].strip()
        sag = parcalar[1].strip()
        # sirius ve 12 kismini ayiralim
        sag_kisim = sag.split()
        hedef = sag_kisim[0]
        yakit = int(sag_kisim[1])
        yield (kaynak, hedef, yakit)


def uzun_yolculuklar(kayitlar, esik: int) -> Generator:
    """yakiti verilen esikten buyuk olanlari secer"""
    for kayit in kayitlar:
        # kayit[2] yakit oluyor
        if kayit[2] > esik:
            yield kayit


# gorev 4 onbellekli rota sayaci
def rota_sayaci(baglantilar: dict):
    """onbellekli rota sayisi bulucu fonksiyon"""
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """verilen gezegenden baslayip adim kadar giden farkli rotalarin sayisi"""
        # hic adim kalmadiysa 1 rota bulunmustur
        if adim == 0:
            return 1
        toplam = 0
        komsular = baglantilar.get(gezegen, [])
        for k in komsular:
            toplam = toplam + rota_sayisi(k, adim - 1)
        return toplam

    return rota_sayisi


# bonus zamanlayici ve mesgul bekleme
def zamanlayici(aralik: float) -> Generator:
    """aralik suresi dolunca true dolmadiysa false uretir"""
    import time

    hedef = time.perf_counter() + aralik
    while True:
        simdi = time.perf_counter()
        if simdi >= hedef:
            hedef = hedef + aralik
            yield True
        else:
            yield False


def tik_tak_programi(toplam_sure: float = 10.0, yazdir: bool = True) -> list:
    """10 saniye boyunca her 2 saniyede tik 5 saniyede tak yazar"""
    import time

    tik = zamanlayici(2.0)
    tak = zamanlayici(5.0)

    olaylar = []
    baslangic = time.perf_counter()

    while (time.perf_counter() - baslangic) <= toplam_sure:
        gecen = time.perf_counter() - baslangic
        if next(tik):
            olaylar.append((round(gecen, 2), "tik"))
            if yazdir:
                print("tik")
        if next(tak):
            olaylar.append((round(gecen, 2), "tak"))
            if yazdir:
                print("tak")

    return olaylar
