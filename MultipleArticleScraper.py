from urllib.request import Request
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def converToSoup(mainURL):
	''' 
        This function will parse the url to BeautifulSoup(BS)
        '''
	try:
		urlRequest = Request(mainURL,headers={'User-Agent':'Mozilla/6.0'})
		urlOpen = urlopen(urlRequest)
		urlRead = urlOpen.read()
		urlClose = urlOpen.close()
		urlBSoup = BeautifulSoup(urlRead,"html.parser")
		return urlBSoup
	except HTTPError:
		print ("The server returned an HTTP error")
	except URLError:
		print ("The server could not be found")
		
def getAllLinks(urlBSoup):
	newsSoup = urlBSoup.findAll("div",{"id":"ch-ls-head"})

	newsList = []
	for news in newsSoup:
		newsLink = news.a['href']
		newsList.append(newsLink)
	return newsList

def getWholeArticle(titleSoup):
        Title = titleSoup.find("h1",{"class":"entry-title"}).text
        checkAuthorisNull = titleSoup.find("div",{"id":"art_author"})

        if checkAuthorisNull == None:
                Author = ""
        else:
                Author = checkAuthorisNull.text.replace("\n","")
		
        Date = titleSoup.find("div",{"id":"art_plat"}).text

        soupBody = titleSoup.findAll("div",{"id":"article_content"})
        articleBody = soupBody[0].div

        for unwantedText in articleBody.findAll("div"):
                unwantedText.decompose()

        Body = articleBody.get_text()

        NewsInfo = [Title,Date,Author,Body]
        return NewsInfo
	
def saveData(link,wholeArticle):
	''' 
        This function will save the scraped data to a text file	
        '''
	file = wholeArticle[0].replace(" ","_")
	file1 = file.replace("?","_")
	filename = file1 + ".txt"
	f = open(filename,"w")
	f.write(wholeArticle[0] + "\n")
	f.write(wholeArticle[1] + "\n")
	f.write(wholeArticle[2] + "\n")
	f.write(link + "\n")
	f.write(wholeArticle[3])
	f.close()
	return True
	
def main():
	# Main link
	mainURL="https://opinion.inquirer.net/tag/rodrigo-duterte"
	
	# Main link to Bsoup
	mainBSoup = converToSoup(mainURL)
	
	# Get all sub link 
	allLinks = getAllLinks(mainBSoup)
	print (allLinks)
	
	# Sub link
	for link in allLinks:
		titleSoup = converToSoup(link)
		wholeArticle = getWholeArticle(titleSoup)
	
	# This function will save the scraped data to a text file
		saveData(link,wholeArticle)
	
main()
