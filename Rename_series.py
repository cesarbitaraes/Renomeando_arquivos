# encoding: utf-8
import os


def rename_file():

    texto = str()

    if os.path.isfile("Nomes_series.txt"):
        arq = open("Nomes_series.txt")
        texto = arq.readlines()
        arq.close()
    else:
        print ("O arquivo Nomes_series.txt não existe na pasta atual!")

    videos = []
    legendas = []

    file_list = os.listdir(".")

    for file_name in file_list:
        formato_arquivo = file_name.split(".")[(len(file_name.split("."))-1)]
        if formato_arquivo == "mkv":
            videos.append(file_name)
        elif formato_arquivo == "srt":
            legendas.append(file_name)

    videos.sort()
    legendas.sort()

    if (len(videos) != len(texto)) or (len(legendas) != len(texto)):
        print("Existe um problema com a quantidade de arquivos!")
        exit()

    n=0
    for linha in texto:
        nome_serie = linha.translate(None, "\n")
        os.rename(videos[n], nome_serie+".mkv")
        os.rename(legendas[n], nome_serie+".srt")
        n=n+1


rename_file()
