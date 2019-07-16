import scrape
import markov

scrape.runScraper('http://www.mldb.org/artist-420-david-bowie.html', 'out.txt')
print("Done scraping. Generating Markov...")
print("********************************************")
markov.runMarkov(6, 500, 'out.txt')
