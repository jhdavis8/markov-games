'''
lyric_generator.py: simple wrapper script to call the scraper and markov generator
                    in sequence

Josh Davis July 2019
'''

import scrape
import markov

scrape.runScraper('http://www.mldb.org/artist-438-bob-dylan.html', 'out.txt')
print("Done scraping. Generating Markov...")
print("********************************************")
markov.runMarkov(6, 500, 'out.txt')
