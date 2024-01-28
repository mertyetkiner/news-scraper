from requests_html import HTMLSession # import HTMLSession class from requests_html module

def clean_text(text): # Function for text clearing
    return text.replace('\n', ' ').replace('\xa0', ' ')

session = HTMLSession() # Create an object of class HTMLSession
url = 'https://www.ntv.com.tr/' # URL of the website to be scraped

try:
    r = session.get(url) # Request web page
    r.html.render(sleep=1,) # Pull rendered content with JavaScript by spooling
    articles = r.html.find('div.ntv-main-slider-item') # Find all elements with a given class on a web page

    newslist = [] # Create a list to hold the information of the news

    for item in articles:  # Loop for each element
        try:
            newsitem = item.find("a", first=True) # Pull news title and link from each element
            title = clean_text(newsitem.attrs['title'])  # Clear the news headline using the clear function
            newsarticle = {  # Collect news title and link in a dictionary
                'title': title,
                'link' : newsitem.absolute_links
            }
            newslist.append(newsarticle) # Add news to the list
        except KeyError as e: # Print to screen if KeyError error is received
            print(f"KeyError: {e}")

    for news in newslist: # Print the information of each news item on the screen
        print(news)
        print()

except Exception as e: # In case of any error, print the error to the screen
    print(f"An error occurred: {e}")
