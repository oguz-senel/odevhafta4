# uzay oyunu hafta 4 lab odevi

ogrenci: Oguz Umut Senel
ogrenci no: 20253004027
ders: ileri python programlama
github: https://github.com/oguz-senel/odevhafta4

bu hafta uzay projesine uretecler, veri boru hatti ve onbellek ekledik


## gorev 4 onbellek olcumleri

adim=20 icin 10 baglantili ornek galakside olcum yaptim:

- onbelleksiz sure: 1.602125 saniye
- onbellekli sure: 0.000080 saniye
- cache_info ciktisi: CacheInfo(hits=47, misses=51, maxsize=None, currsize=51)

onbelleksiz fonksiyonda adim=20 yapinca surekli ayni dugumleri ve dallari tekrar tekrar hesapladigi icin yaklasik 1.6 saniye surdu bilgisayari bekletti biraz ama @lru_cache ekleyince onceden hesaplanan rota sayilarini hafizada tuttugu icin 0.00008 saniyede bitti yani neredeyse aninda hesapladi asiri hizlandi


## gorev 5 okunaklilik karsilastirmasi

bence kesinlikle liste uretecleri (list comprehension) ve sum() fonksiyonu cok daha okunakli
cunku map ve filter yazarken mecburen lambda kullanmak gerekiyor sonra bir de en disa list() eklemek gerekiyor parantezler birbirine giriyor kod kalabaligi oluyor
reduce fonksiyonu da benzer sekilde iki parametreli lambda ile kafayi karistiriyor onun yerine sum() yazinca ne yaptigi tek bakista anlasiliyor o yuzden python tarzi liste uretecleri cok daha temiz


## bonus zamanlayici mesgul bekleme ve time.sleep farki

zamanlayici fonksiyonunda bir while True dongusu icinde time.perf_counter() ile hedeflenen saniyeyi surekli kontrol ediyoruz bu yonteme mesgul bekleme (busy waiting) deniyor cunku islemci bu donguden hic cikmiyor bos yere yuzde 100 calisip bilgisayari yoruyor ve elektrik harciyor

time.sleep ile temel farki su:
time.sleep(2) gibi bir komut verdigimizde isletim sistemi o sure boyunca python programini uyku moduna aliyor yani calismasini durduruyor ve islemci o sirada baska isleri yapabiliyor boylece cpu bosuna calismamis oluyor sure bitince isletim sistemi tekrar uyandiriyor ama mesgul beklemede islemciyi hic serbest birakmiyoruz surekli kontrol edip yoruyoruz


## testler

uv run pytest
