# encoding: utf-8
import os


def rename_file():

    texto = str()

    if os.path.isfile("Nomes_filmes.txt"):
        arq = open("Nomes_filmes.txt")
        texto = arq.readlines()
        arq.close()
    else:
        print ("O arquivo Nomes_series.txt não existe na pasta atual!")

    if os.path.isdir("Filmes"):
        os.chdir("Filmes")
    else:
        os.mkdir("Filmes")
        os.chdir("Filmes")

    for linha in texto:
        nome_filme = linha.translate(None, "\n")

        if os.path.isdir(nome_filme):
            print("A pasta \""+nome_filme+"\" já foi criada!")

            #Retorna o nome reduzido
            os.chdir(nome_filme)
            nome_arquivo = nome_filme.split("(")[0]
            nome_reduzido = nome_arquivo[0:(len(nome_arquivo))-1]

            #Lista os diretorios
            file_list = os.listdir(".")
            if len(file_list) == 0:
                print("Esta pasta está vazia!")

            elif len(file_list) > 0:

                print("Esta pasta contém arquivos!")

                resposta = raw_input("O filme atual é dual áudio? (s, n ou qualquer outra tecla para não renomear): ")

                if resposta == "s":

                    for file_name in file_list:
                        formato_arquivo = file_name.split(".")[(len(file_name.split("."))-1)]
                        if formato_arquivo == "mkv":
                            os.rename(file_name, nome_reduzido+" (Inglês e Português).mkv")
                        elif formato_arquivo == "srt":
                            os.rename(file_name, nome_reduzido+" (Inglês e Português).srt")

                elif resposta == "n":
                    for file_name in file_list:
                        formato_arquivo = file_name.split(".")[(len(file_name.split("."))-1)]
                        if formato_arquivo == "mkv":
                            os.rename(file_name, nome_reduzido+".mkv")
                        elif formato_arquivo == "srt":
                            os.rename(file_name, nome_reduzido+".srt")
            
            os.chdir("..")

        else:
            os.mkdir(nome_filme)
            print("Pasta \""+nome_filme+"\" criada!")

rename_file()
