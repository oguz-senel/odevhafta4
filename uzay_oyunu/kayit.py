# gorev kayit modulu
# oguz umut senel


def gorev_kaydi(baslik: str, *adimlar: str,
                oncelik: str = "normal", **ekler) -> str:
    """gorev metni olusturur oncelik sadece adla verilir"""
    sonuc = "[" + oncelik.upper() + "] " + baslik

    for i in range(len(adimlar)):
        sonuc += "\n " + str(i + 1) + ". " + adimlar[i]

    for k in ekler:
        sonuc += "\n " + k + ": " + str(ekler[k])

    return sonuc


if __name__ == "__main__":
    # normal argumanlarla cagri
    print(gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan", "Pilot bul", "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe"
    ))

    print()

    # yildizla acarak cagri
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekstralar = {"sorumlu": "Ayşe"}

    print(gorev_kaydi(
        "Kara deliğe atla",
        *adim_listesi,
        oncelik="yüksek",
        **ekstralar
    ))
