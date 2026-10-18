# uzay oyunu hafta 4 odevi

ogrenci: Oguz Umut Senel
ogrenci no: 20253004027
ders: ileri python programlama
github: https://github.com/oguz-senel/odevhafta4

bu hafta projeye uretecler boru hatti ve onbellek ekledik


## gorev 4 onbellek olcumleri

adim=20 icin 10 baglantili ornek haritada olcum yaptim sonuclar soyle cikti:

- onbelleksiz sure: 1.602125 saniye
- onbellekli sure: 0.000080 saniye
- cache_info ciktisi: CacheInfo(hits=47, misses=51, maxsize=None, currsize=51)

onbellek kullaninca ayni yerleri tekrar tekrar hesaplamadigi icin inanilmaz hizlandi normalde surekli dallanip ayni seyleri hesapliyordu onbellek sayesinde tek seferde cozdu baya fark etti yani


## gorev 5 okunaklilik hakkinda dusuncem

bence kesinlikle liste uretecleri cok daha okunakli map ve filter kullaninca hem lambda yazmak zorunda kaliyoruz hem de sonra list() ile sarmak gerekiyor kod cok karisiyor reduce zaten ayri dert sum() fonksiyonu cok daha temiz ve anlasilir o yuzden python da liste ureteci bence cok daha guzel


## bonus mesgul bekleme ve time sleep farki

zamanlayici fonksiyonunda while True icinde surekli time.perf_counter() ile saati kontrol ettigimiz icin buna mesgul bekleme (busy waiting) deniyor islemci hic durmadan surekli calisiyor ve bos yere yuzde 100 cpu harcayip bilgisayari yoruyor

time.sleep ile farki ise su:
time.sleep dedigimiz zaman isletim sistemi programi uyutuyor islemci o sirada baska programlarla ilgilenebiliyor hic cpu harcamiyor sure bitince tekrar uyandiriyor mesgul beklemede ise islemciyi hic birakmiyoruz surekli kontrol edip yoruyoruz


## testleri calistirma

uv run pytest
