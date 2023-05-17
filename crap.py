#!./venv/bin/python

from bs4 import BeautifulSoup
import requests
import csv

# Nastavení vstupního a výstupního souboru
input='input2.csv'
output='output2.md'

# Scrapování textu - specifické rpo web Rádce
def textscrap(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    with open(output, 'a', encoding='utf-8') as file:
        file.write(url + '\n')
        title = soup.find(class_='title__name')
        # print(title.get_text())
        file.write('#' + title.get_text())
        odrazky = soup.find_all(class_='froalaListBaseItem')
        for p in odrazky:
            # print(p.get_text())
            file.write('- ' + p.get_text()+ '\n')
        file.write("**Proč je to důležité**")
        paragraphs = soup.find_all(class_='box__text')
        for p in paragraphs:
            # print(p.get_text())
            file.write(p.get_text())
        
        file.write('\n' + '---' + '\n')
    print("Zapsáno do souboru...")


# Načteme CSV s adresami
with open(input, 'r') as ifile:
    # Create a CSV reader object
    reader = csv.reader(ifile)

    # Projdeme všechny řádky
    for row in reader:
        # A ev. i hodnoty - tady máme vždy jen jednu hodnotu
        for value in row:
            try:
                print(value)
                textscrap(value)
            except: 
                pass    