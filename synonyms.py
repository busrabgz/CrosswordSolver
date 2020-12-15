import requests
from time import sleep
from bs4 import BeautifulSoup
import string
from nltk.corpus import stopwords
import nltk
from getMerriamWebster import combine_tokens 

def searchSynonyms(clue):
    tokens = combine_tokens(clue)
    words = set()
    for word in tokens:
        if(contains_multiple_words(word)):
            # Thesaurus.com
            r_th = requests.get("https://www.thesaurus.com/browse/" + word.split()[0] + "%20" + word.split()[1])

            # Merriam webster
            r_mw = requests.get("https://www.merriam-webster.com/thesaurus/" + word.split()[0] + "%20" + word.split()[1])

            # Datamuse
            r_dm = requests.get('https://api.datamuse.com/words?rel_syn={}_{}'.format(word.split()[0], word.split()[1]))

        else:
            # Thesaurus.com
            r_th = requests.get("https://www.thesaurus.com/browse/" + word)

            # Merriam webster
            r_mw = requests.get("https://www.merriam-webster.com/thesaurus/" + word)

            # Datamuse
            r_dm = requests.get('https://api.datamuse.com/words?rel_syn={}'.format(word))

       
        soup = BeautifulSoup(r_th.text, 'html.parser')    
        texts = soup.findAll(text=True)
        
            
        soup = BeautifulSoup(r_mw.content, 'html.parser')

        for i in soup.select('.thes-list.syn-list a'):
            words.add(i.string)

        for i in soup.select('.thes-list.rel-list a'):
            words.add(i.string)
            
        for i in soup.select('.thes-list.sim-list a'):
            words.add(i.string)        
        
        results = r_dm.json()
        for result in results:
            words.add(result['word'])
    return str(texts) + ' '.join(str(e) for e in words) 

def contains_multiple_words(s):
  return len(s.split()) > 1
