# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
from bs4 import BeautifulSoup

nome_serie_inicial = raw_input("Entre com o nome da serie: ")
temporada = raw_input("Entre com o número da temporada: ")

nome_serie = nome_serie_inicial.lower().replace(" ", "-")
endereco = "https://episodecalendar.com/pt/show/"+nome_serie+"/season/"+temporada
print ("O endereço requisitado é: \n"+endereco)


def capturando_nome_series():

    page = urllib2.urlopen(endereco)
    html_soup = BeautifulSoup(page, "html.parser")
    all_text = html_soup.find_all("div", class_ = "epic-list-episode")

    if not all_text:
        print ("Série não existe ou a página não foi encontrada!")
        exit() 

    for episodes in all_text:
        episode_name = episodes.find_all("strong")
        numero_grande = episode_name[0].text.strip()
        nome = episode_name[1]
        numero = numero_grande.split("x")
        numero_episodio = numero[1]
        if int(numero[1]) < 10:
            with open("Nomes_series.txt", "a") as arquivo:
                nome_final = "Episódio 0"+numero_episodio+" - "+nome.text.strip()
                arquivo.write((nome_final.encode("utf-8").strip()))
                arquivo.write("\n")
                arquivo.close()
            print ("O item \"Episódio 0"+numero_episodio+" - "+nome.text.strip()+"\" foi adicionado com sucesso.")
        else:
            with open("Nomes_series.txt", "a") as arquivo:
                nome_final = "Episódio "+numero_episodio+" - "+nome.text.strip()
                arquivo.write((nome_final.encode("utf-8").strip()))
                arquivo.write("\n")
                arquivo.close()
            print ("O item \"Episódio "+numero_episodio+" - "+nome.text.strip()+"\" foi adicionado com sucesso.")

capturando_nome_series()