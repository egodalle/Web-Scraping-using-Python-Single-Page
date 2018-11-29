# Web-Scraping-using-Python-Single-Page
This python script will scrape the author,date and body of all the articles of the first page of a news website.
The steps in scraping are listed below:

1. First, It  will take the url and then convert it to BeautifulSoup object
2. It will then scrape all the title's link of the first page and save it to a list
3. It will then loop thru all the items(links) on the list and then retrieve the title,date,author and body of the article under the 'p' tag. It also removes text advertisements which are children of the 'p' tag, thus I used the decompose python method
4. Lastly, It will save the scraped data to a text file
