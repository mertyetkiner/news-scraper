# Web Scraping with Requests-HTML

This is a simple Python script that demonstrates web scraping using the `requests_html` module to extract news headlines and links from the NTV website (https://www.ntv.com.tr/).

## Prerequisites

Before running the script, make sure you have the necessary Python libraries installed. You can install them using the following:

```bash
pip install requests-html
```

## How to Use

1. Clone the repository to your local machine:

```bash
git clone https://github.com/mertyetkiner/news-scraper.git
```

2. Navigate to the project directory:

```bash
cd news-scraper
```

3. Run the script:

```bash
python newscraper.py
```

## Script Explanation

1. Import the necessary module:

```python
from requests_html import HTMLSession
```

2. Define a function for text cleaning:

```python
def clean_text(text):
    return text.replace('\n', ' ').replace('\xa0', ' ')
```

3. Create an instance of the `HTMLSession` class:

```python
session = HTMLSession()
```

4. Specify the URL of the website to be scraped:

```python
url = 'https://www.ntv.com.tr/'
```

5. Send a request to the web page:

```python
r = session.get(url)
```

6. Render the JavaScript content on the page:

```python
r.html.render(sleep=1)
```

7. Find all elements with a specific class on the web page:

```python
articles = r.html.find('div.ntv-main-slider-item')
```

8. Iterate through each element and extract news title and link:

```python
for item in articles:
    try:
        newsitem = item.find("a", first=True)
        title = clean_text(newsitem.attrs['title'])
        newsarticle = {
            'title': title,
            'link' : newsitem.absolute_links
        }
        newslist.append(newsarticle)
    except KeyError as e:
        print(f"KeyError: {e}")
```

9. Print the information of each news item:

```python
for news in newslist:
    print(news)
    print()
```

10. Handle errors:

```python
except Exception as e:
    print(f"An error occurred: {e}")
```

mertyetkiner
