# Web Scraping with Python

This Python script is made to pull data from a website using the requests_html module.

## Module Used

- requests_html: Used to retrieve and process web pages.

## How to Use

1. Install the `requests_html` module:
 
```bash
   pip install requests-html
```

2. Run the script:

```bash   
python web_scraping.py
```

3. The code will pull instant headlines from NTV news site and clean them to make them readable.

## Cleanup Function

The clean_text function is used to clear text. In particular, it cleans '\n' (newline) and '\xa0' (NO-BREAK SPACE) characters.

## Error Conditions

In case of any error, the relevant error message is printed to the screen.

mertyetkiner
