# Web Scraping with Python

Bu Python kodu, requests_html modülü kullanılarak bir web sitesinden veri çekmek için yapılmıştır.

## Kullanılan Modül

- requests_html: Web sayfalarını çekmek ve işlemek için kullanılır.

## Nasıl Kullanılır

1. `requests_html` modülünü yükleyin:
 
```bash
   pip install requests-html
```

2. Kodu çalıştırın:

```bash   
python web_scraping.py
```

3. Kod, NTV haber sitesinden anlık başlıkları çekecek ve okunabilir hale getirmek için temizleyecektir.

## Temizleme Fonksiyonu

clean_text fonksiyonu, metni temizlemek için kullanılır. Özellikle '\n' (newline) ve '\xa0' (NO-BREAK SPACE) karakterlerini temizler.

## Hata Durumları

Herhangi bir hata durumunda, ilgili hata mesajı ekrana yazdırılır.

mertyetkiner
