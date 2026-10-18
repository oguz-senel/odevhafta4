# uzay oyunu
# oguz umut senel

import json
import os
from uzay_oyunu.araclar import hamle_sayaci


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """esyalar varsa sende metnini yoksa bos string dondurur"""
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if len(esyalar) > 0:
        return "Sende: " + ", ".join(esyalar)
    return ""


def hedef_menusu(hedefler: list[str]) -> str:
    """numarali hedef listesi dondurur"""
    metin = "Nereye gitmek istersin?"
    for i in range(len(hedefler)):
        metin += "\n[" + str(i + 1) + "] " + hedefler[i]
    return metin


def galaksi_kur(gezegenler: list[str], baglantilar: dict,
                baslangic: str, **kwargs) -> dict:
    """galaksi sozlugu olusturur baslangic yoksa hata verir"""
    if baslangic not in gezegenler:
        raise ValueError(f"{baslangic} listede yok")

    # yakit yoksa 50 al
    yakit = kwargs.get("yakit", 50)

    galaksi = {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }
    return galaksi


def galaksi_yukle() -> dict:
    """json dosyasindan galaksiyi okur"""
    yol = os.path.join(os.path.dirname(__file__), "galaksi.json")
    with open(yol, "r", encoding="utf-8") as f:
        veri = json.load(f)
    return galaksi_kur(**veri)


def travel():
    """ana oyun dongusu"""
    from uzay_oyunu.akis import yakit_gostergesi
    galaksi = galaksi_yukle()
    sayac = hamle_sayaci()
    gosterge = yakit_gostergesi(galaksi["yakit"], 5)

    credits = False
    engines = False
    copilot = False
    hamle = 0

    print("=== UZAY MACERASI ===")
    print("Konum:", galaksi["konum"])
    print("Yakıt:", galaksi["yakit"])
    print()

    while galaksi["yakit"] > 0:
        envanter = envanter_metni(credits, engines, copilot)
        if envanter:
            print(envanter)

        konum = galaksi["konum"]
        hedefler = galaksi["baglantilar"].get(konum, [])

        if len(hedefler) == 0:
            print("Buradan gidecek yer yok!")
            break

        print(hedef_menusu(hedefler))

        try:
            secim = input("Seçimin (q=çık): ")
            if secim.lower() == "q":
                break

            idx = int(secim) - 1
            if idx >= 0 and idx < len(hedefler):
                yeni_yer = hedefler[idx]
                galaksi["konum"] = yeni_yer
                try:
                    galaksi["yakit"] = next(gosterge)
                except StopIteration:
                    print("Yakıtın bitti, uzayda sürükleniyorsun…")
                    break
                hamle = sayac()

                print()
                print(yeni_yer, "gezegenine vardın!")
                print("Kalan yakıt:", galaksi["yakit"])

                if yeni_yer == "centauri" and not credits:
                    credits = True
                    print("Bol kredi buldun!")
                elif yeni_yer == "orion" and not copilot:
                    copilot = True
                    print("Yetenekli bir pilot katıldı!")
                elif yeni_yer == "sirius" and not engines:
                    engines = True
                    print("Güçlü motorlar taktın!")
                elif yeni_yer == "kara_delik":
                    print("Kara deliğe ulaştın! Kazandın!")
                    print(f"Oyunu {hamle} hamlede bitirdin!")
                    return

                print()
            else:
                print("Yanlış numara!\n")
        except ValueError:
            print("Sayı gir!\n")

    if galaksi["yakit"] <= 0:
        print("Yakıt bitti!")
    print(f"Oyunu {hamle} hamlede bitirdin!")


if __name__ == "__main__":
    travel()
