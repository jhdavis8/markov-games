'''
scrape.py: takes in a MLDB artist page link and output name and dumps 
           the lyrics of every song by that artist into a text file.
           Note there is a delay between every request to prevent
           being flagged as a spammer

Josh Davis July 2019
Credit to this article for the general approach:
https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460?gi=64b1fe1d8a19
'''

import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup

def createLyricsFile(links, filename):
    output = open(filename,"w")
    #for i in links:
    for i in links:
        time.sleep(0.5)
        song_url = 'http://www.mldb.org/' + i['href']
        print(song_url)
        song_response = requests.get(song_url)
        song_soup = BeautifulSoup(song_response.text, "html.parser")
        try:
            lyrics = song_soup.findAll("p","songtext")[0].get_text()
        except IndexError as e:
            print(e)
            continue
        output.write(lyrics)
        
        
def runScraper(url, filename):
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.findAll(href=re.compile("song-"))
    print("Parsed " + str(len(links)) + " links.")
    createLyricsFile(links, filename)

if __name__ == "__main__":
    runScraper(sys.argv[1], sys.argv[2])
