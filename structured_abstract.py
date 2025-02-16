import urllib.request as urllib2
import pickle
from collections import defaultdict

target_url = 'https://lhncbc.nlm.nih.gov/ii/areas/structured-abstracts/downloads/Structured-Abstracts-Labels-102615.txt'
normalized_sections = defaultdict(list)
with open('structured_headings.txt', 'w') as file:
    for line in urllib2.urlopen(target_url):
        clean_line = line.decode("utf-8").split('|')
        normalized_sections[clean_line[1].lower()].append(clean_line[0].lower())

with open('/Users/joemenke/Desktop/illinois/research_projects/structured_abstract_sections.pkl', 'wb') as file:
    pickle.dump(normalized_sections, file)
    
print(normalized_sections)
print(list(normalized_sections.keys()))