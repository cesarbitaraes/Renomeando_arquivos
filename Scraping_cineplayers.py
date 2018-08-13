# encoding: utf-8
import urllib2
from bs4 import BeautifulSoup


def busca_filme():
    initial_movie = raw_input("Qual filme deseja buscar? ")
    movie = initial_movie.lower().replace(" ", "+")
    endereco = "http://www.cineplayers.com/busca?b="+movie+"&x=0&y=0"
    page = urllib2.urlopen(endereco)
    html_soup = BeautifulSoup(page, "html.parser")
    resultados = html_soup.find_all("tr", attrs={"id": "linha_filme"})

    for filmes in resultados:
        info_filmes = filmes.find_all("a")

    finded_results = len(info_filmes)
    print ("Esses foram os "+str(finded_results)+" resultados encontrados: ")

    n=1
    for links in info_filmes:
        print str(n)+" - "+links.text
        n=n+1

    movie_choose = raw_input("Digite o número do filme escolhido: ")
    if int(movie_choose) > finded_results:
        print("Número solicitado não pertence à lista!\nEncerrado...")
        exit()
    print ("Esse é o link: ")
    url_big = info_filmes[int(movie_choose)-1]
    url_medium = str(url_big)
    url_final = url_medium.split("\"")[1] 
    link_filme = "http://www.cineplayers.com"+url_final
    print link_filme
    return link_filme


def captura_dados_filme(link_filme):
    page = urllib2.urlopen(link_filme)
    html_soup = BeautifulSoup(page, "html.parser")

    resultados = html_soup.find_all("div", attrs={"id":"r-princ"})
    nome_ptbr = resultados[0].find_all("h1")
    nome_en = resultados[0].find_all("span", attrs={"class":"txt_italico"})
    nome_ptbr_final = nome_ptbr[0].text.replace(","," -")
    nome_en_final = nome_en[0].text

    partes = nome_en_final.split(",")

    if len(partes) == 2:
        nome_inicial = partes[0]
        ano = partes[1]
        nome_inicial_final = nome_inicial[1:(len(nome_inicial))]
        ano_final = ano[1:(len(ano)-1)]

        nome_filme_final = nome_ptbr_final+" ("+nome_inicial_final+") - "+ano_final
        with open("Nomes_filmes.txt", "a") as arquivo:
                arquivo.write(nome_filme_final.replace(":"," -").encode("utf-8").strip())
                arquivo.write("\n")
                arquivo.close()
        print "Fime: \""+nome_filme_final.replace(":", " -")+"\" adicionado ao arquivo."
    else:
        nome_inicial = partes[0]
        nome_meio = partes[1]
        ano = partes[2]
        nome_inicial_final = nome_inicial[1:(len(nome_inicial))]
        nome_meio_final = nome_meio[1:len(nome_meio)]
        ano_final = ano[1:(len(ano)-1)]
        if nome_meio_final == "The" or nome_meio_final == "O" or nome_meio_final == "Una":
            nome_filme_final = nome_ptbr_final+" ("+nome_meio_final+" "+nome_inicial_final+") - "+ano_final
        else:
            nome_filme_final = nome_ptbr_final+" ("+nome_inicial_final+" - "+nome_meio_final+") - "+ano_final
        with open("Nomes_filmes.txt", "a") as arquivo:
                arquivo.write(nome_filme_final.replace(":"," -").encode("utf-8").strip())
                arquivo.write("\n")
                arquivo.close()
        print "Fime: \""+nome_filme_final.replace(":", " -")+"\" adicionado ao arquivo."


resposta = "s"
while resposta == "s":
    link_filme = busca_filme()
    captura_dados_filme(link_filme)
    resposta = raw_input("Deseja continuar procurando filmes (s ou n)? ")