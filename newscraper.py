# import HTMLSession class from requests_html module
from requests_html import HTMLSession

# Function for text clearing
def clean_text(text):
    return text.replace('\n', ' ').replace('\xa0', ' ')

# Create an object of class HTMLSession
session = HTMLSession()

# URL of the website to be scraped
url = 'https://www.ntv.com.tr/' 

# Request web page
try:
    r = session.get(url)

    # Pull rendered content with JavaScript by spooling
    r.html.render(sleep=1,)

    # Find all elements with a given class on a web page    
    articles = r.html.find('div.ntv-main-slider-item')

    # Create a list to hold the information of the news
    newslist = []
    
    # Loop for each element
    for item in articles:
        try:
            # Pull news title and link from each element
            newsitem = item.find("a", first=True)

            # Clear the news headline using the clear function
            title = clean_text(newsitem.attrs['title'])

            # Collect news title and link in a dictionary
            newsarticle = {
                'title': title,
                'link' : newsitem.absolute_links
            }

            # Add news to the list
            newslist.append(newsarticle)
        
        except KeyError as e:
            # Print to screen if KeyError error is received
            print(f"KeyError: {e}")
            
    # Print the information of each news item on the screen
    for news in newslist:
        print(news)
        print()

# In case of any error, print the error to the screen
except Exception as e:
    print(f"An error occurred: {e}")
