import requests
import urllib.parse
import time
from bs4 import BeautifulSoup

def pega_ruas(cidade):
    file_ruas = open("./txt/ruas.txt", 'w')

    # limpa o parametro
    cidade = cidade.strip()
    cidade = cidade.lower()

    cidade = cidade.replace(' ', '-')

    url = "https://www.rastreamentocorreios.net/qual_cep/sp/{cidade}".format(cidade=cidade)
    response = requests.get(url)

    print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.table
    streets_table = table.findAll('a')

    for element in streets_table:
        street = element.get_text()
        file_ruas.write(street + '\n')
    
    file_ruas.close()