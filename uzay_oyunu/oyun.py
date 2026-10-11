# uzay oyunu
# oguz umut senel


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


def travel():
    """ana oyun dongusu"""
    konum = "dünya"
    yakit = 100
    credits = False
    engines = False
    copilot = False

    print("=== UZAY MACERASI ===")
    print("Konum:", konum)
    print("Yakıt:", yakit)
    print()

    while yakit > 0:
        envanter = envanter_metni(credits, engines, copilot)
        if envanter:
            print(envanter)

        if konum == "dünya":
            destinations = ["centauri", "sirius"]
        elif konum == "centauri":
            destinations = ["dünya", "sirius", "orion"]
        elif konum == "sirius":
            destinations = ["dünya", "centauri", "orion", "kara_delik"]
        elif konum == "orion":
            destinations = ["centauri", "sirius"]
        elif konum == "kara_delik":
            destinations = ["sirius"]
        else:
            destinations = []

        if len(destinations) == 0:
            print("Buradan gidecek yer yok!")
            break

        print(hedef_menusu(destinations))

        try:
            secim = input("Seçimin (q=çık): ")
            if secim.lower() == "q":
                break

            idx = int(secim) - 1
            if idx >= 0 and idx < len(destinations):
                yeni_yer = destinations[idx]
                konum = yeni_yer
                yakit -= 10

                print()
                print(yeni_yer, "gezegenine vardın!")
                print("Kalan yakıt:", yakit)

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
                    return

                print()
            else:
                print("Yanlış numara!\n")
        except ValueError:
            print("Sayı gir!\n")

    if yakit <= 0:
        print("Yakıt bitti!")


if __name__ == "__main__":
    travel()
