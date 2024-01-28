from requests_html import HTMLSession # requests_html modülünden HTMLSession sınıfını içe aktar

def clean_text(text): # Text temizleme işlemi için fonksiyon
    return text.replace('\n', ' ').replace('\xa0', ' ')

session = HTMLSession() # HTMLSession sınıfından bir nesne oluştur
url = 'https://www.ntv.com.tr/' # Scraping işlemi yapılacak web sitesinin URL'si

try:
    r = session.get(url) # Web sayfasını talep et
    r.html.render(sleep=1,) # JavaScript ile render edilen içeriği bekleterek çek
    articles = r.html.find('div.ntv-main-slider-item')  # Web sayfasındaki belirli bir sınıfa sahip tüm elemanları bul

    newslist = [] # Haberlerin bilgilerini tutacak bir liste oluştur

    for item in articles:  # Her bir eleman için döngü oluştur
        try:
            newsitem = item.find("a", first=True) # Her bir elemandan haber başlığını ve linki çek
            title = clean_text(newsitem.attrs['title'])  # Temizleme fonksiyonunu kullanarak haber başlığını temizle
            newsarticle = {  # Haber başlığı ve bağlantısını bir sözlükte topla
                'title': title,
                'link' : newsitem.absolute_links
            }
            newslist.append(newsarticle) # Haberleri listeye ekle
        except KeyError as e: # KeyError hatası alınırsa ekrana yazdır
            print(f"KeyError: {e}")

    for news in newslist: # Her bir haberin bilgilerini ekrana yazdır
        print(news)
        print()

except Exception as e: # Herhangi bir hata durumunda ekrana hatayı yazdır
    print(f"An error occurred: {e}")