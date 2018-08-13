# encoding: utf-8

import urllib2
from bs4 import BeautifulSoup

def capturando_nome_filmes():

    numero = raw_input("Entre com o número do filme (aperte n para encerrar): ")
    while numero != "n":
        site = "http://www.adorocinema.com/filmes/filme-"+numero+"/"
        page = urllib2.urlopen(site)

        html_soup = BeautifulSoup(page, "html.parser")

        hidden_infos = html_soup.find("div", attrs={"class": "more-hidden"})
        ano = hidden_infos.find("span", attrs={"class": "that"})
        name_ptbr = html_soup.find(class_ = "titlebar-title titlebar-title-lg")
        name_english = html_soup.find("h2", attrs={"class": "that"})


        if name_english is not None:
            name_english_reduzido = name_english.text.strip()
        if name_ptbr is not None:
            name_ptbr_reduzido = name_ptbr.text.strip()
        if ano is not None:
            year = ano.text.strip()

        if name_english is not None:
            nome_final = name_ptbr_reduzido+" ("+name_english_reduzido+") - "+year
            with open("Nomes_filmes.txt", "a") as arquivo:
                arquivo.write((nome_final.replace(":", " -")).encode("utf-8").strip())
                arquivo.write("\n")
                arquivo.close()
            print "Fime: \""+nome_final.replace(":", " -")+"\" adicionado ao arquivo."
        else:
            nome_final = name_ptbr_reduzido+" ("+name_ptbr_reduzido+") - "+year
            with open("Nomes_filmes.txt", "a") as arquivo:
                arquivo.write((nome_final.replace(":", " -")).encode("utf-8").strip())
                arquivo.write("\n")
                arquivo.close()
            print "Fime: \""+nome_final.replace(":", " -")+"\" adicionado ao arquivo."

        numero = raw_input("Entre com o número do filme (aperte n para encerrar): ")

capturando_nome_filmes()