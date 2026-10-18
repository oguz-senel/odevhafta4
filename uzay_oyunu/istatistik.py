# oguz umut senel - 20253004027
# istatistik modulu - map filter reduce ve partial

from functools import reduce, partial

# hocanin okunaklilik sorusuna yorumum:
# bence kesinlikle liste uretecleri cok daha okunakli cunku map ve filter yazarken araya lambda giriyor bide en disa list() yazmak lazim parantezler cok karisiyor
# reduce da ayni sekilde reduce(lambda t, k: t + len(k), ...) yazmaktansa sum() fonksiyonu kullanmak bin kat daha temiz ve anlasilir o yuzden python tarzi liste ureteci ve sum daha iyi bence


# soru 1 gezegen adlarinin buyuk harfli listesi
def buyuk_harfli_gezegenler_map(galaksi: dict) -> list[str]:
    """map ile gezegenleri buyuk harfe cevirir"""
    return list(map(lambda g: g.upper(), galaksi["gezegenler"]))


def buyuk_harfli_gezegenler_comp(galaksi: dict) -> list[str]:
    """liste ureteci ile gezegenleri buyuk harfe cevirir"""
    return [g.upper() for g in galaksi["gezegenler"]]


def buyuk_harfli_gezegenler(galaksi: dict) -> list[str]:
    """buyuk harf listesi dondurur"""
    return buyuk_harfli_gezegenler_comp(galaksi)


# soru 2 en az iki baglantisi olan gezegenler
def cok_baglantili_gezegenler_filter(galaksi: dict, esik: int = 2) -> list[str]:
    """filter ile en az esik kadar baglantisi olanlari secer"""
    bag = galaksi["baglantilar"]
    # lambda ile komsularina bakiyoruz
    return list(filter(lambda g: len(bag.get(g, [])) >= esik, galaksi["gezegenler"]))


def cok_baglantili_gezegenler_comp(galaksi: dict, esik: int = 2) -> list[str]:
    """liste ureteci ile en az esik kadar baglantisi olanlari secer"""
    bag = galaksi["baglantilar"]
    return [g for g in galaksi["gezegenler"] if len(bag.get(g, [])) >= esik]


def cok_baglantili_gezegenler(galaksi: dict, esik: int = 2) -> list[str]:
    """en az iki baglantisi olan gezegenleri dondurur"""
    return cok_baglantili_gezegenler_comp(galaksi, esik)


# soru 3 toplam baglanti sayisi
def toplam_baglanti_sayisi_reduce(galaksi: dict) -> int:
    """reduce ile tum baglanti sayilarini toplar"""
    bag = galaksi["baglantilar"]
    return reduce(lambda toplam, komsular: toplam + len(komsular), bag.values(), 0)


def toplam_baglanti_sayisi_sum(galaksi: dict) -> int:
    """sum ile tum baglanti sayilarini toplar"""
    bag = galaksi["baglantilar"]
    return sum(len(komsular) for komsular in bag.values())


def toplam_baglanti_sayisi(galaksi: dict) -> int:
    """toplam baglanti sayisini dondurur"""
    return toplam_baglanti_sayisi_sum(galaksi)


# yolculuk ve partial ile hizli yolculuk
def yolculuk(mesafe: float, hiz: float = 1.0) -> float:
    """mesafeyi hiza bolerek yolculuk suresini bulur"""
    return mesafe / hiz


# partial ile hizi 3 yaptik
hizli_yolculuk = partial(yolculuk, hiz=3.0)
