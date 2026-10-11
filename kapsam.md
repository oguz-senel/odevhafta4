# Kapsam ornekleri gorev 4b
Oguz Umut Senel

## Ornek 1 yerel degisken

```python
x = 10
def fonk():
    x = 20
    print(x)
fonk()
print(x)
```

Tahminim: 20 sonra 10 yazar
Gercek sonuc: 20 ve 10
Nedeni: fonksiyonun icindeki x = 20 yerel degisken oldugu icin disaridaki x degismez fonk bitince disaridaki x yine 10 olarak kalir

## Ornek 2 ic ice fonksiyon

```python
def dis():
    y = 5
    def ic():
        print(y)
    ic()
dis()
```

Tahminim: 5 yazar
Gercek sonuc: 5
Nedeni: ic fonksiyonu kendi icinde y bulamayinca bir distaki dis fonksiyonunun y degerini alir buna enclosing scope deniyor derste gormustuk LEGB kuralindaki E harfi

## Ornek 3 UnboundLocalError

```python
z = 10
def fonk():
    print(z)
    z = 20
fonk()
```

Tahminim: once 10 yazar sonra z 20 olur gibi dusunmustum
Gercek sonuc: UnboundLocalError hatasi verdi
Nedeni: python fonksiyonda asagida z = 20 atamasini gordugu an z yi yerel degisken olarak belirliyor ama print(z) satirinda henuz z ye deger atanmadigi icin hata veriyor yani fonksiyonda asagida bile olsa atama varsa python o degiskeni direkt yerel sayiyor
bunu cozmek icin normalde global yazilabilirdi ama bu odevde global yasak oldugu icin kullanmiyoruz gorev 5teki closure yapisinda da nonlocal kullaniyoruz
