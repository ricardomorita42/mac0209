#   Este script converte o tempo exibido para que na primeira linha seja 0
# e que nas demais tenhamos a soma das diferença deste sobre o instante
# anterior. Assim, na linha final teremos as somas das diferenças entre
# os instantes = tempo total

import datetime
import io
import os

# Encontra todos os .csv da pasta e põe numa lista
processing_queue = []
with os.scandir("./") as entries:
    for entry in entries:
        if ".csv" in entry.name:
            processing_queue.append(entry.name)

arq_entrada = processing_queue.pop()
arq_saida = "resultados/proc_" + arq_entrada

# Processando cada .csv:
while processing_queue:
    # inic variaveis
    datas = []
    instantes = []
    ax = []
    ay = []
    az = []

    entrada = open(arq_entrada, "r")

    #1a vez descarta titulo e a 2nda inputa dado
    linha = entrada.readline()
    linha = entrada.readline()

    #populando as listas com o arquivo lido
    while linha:
        temp_linha = linha.split(",")

        str_data = temp_linha[0]
        #print(str_data)
        datas.append(datetime.datetime.strptime(str_data, "%Y-%m-%d %H:%M:%S.%f"))

        ax.append(float(temp_linha[1]))
        ay.append(float(temp_linha[2]))
        az.append(float(temp_linha[3]))

        linha = entrada.readline()

    #agora lidando com o output
    saida = open(arq_saida,"w+")

    #escrevendo cabecalho e 1a linha
    saida.write("time,ax,ay,az\n")

    linha_atual = []
    linha_atual.append(0)
    linha_atual.append(ax[0])
    linha_atual.append(ay[0])
    linha_atual.append(az[0])
    instantes.append(0)

    saida.write(",".join(str(x) for x in linha_atual))
    saida.write("\n")

    #escrevendo o resto do arquivo
    i = 1
    while i < len(datas):
        linha_atual = []
        diff = datas[i] - datas[i-1]
        t_atual = diff.total_seconds() + instantes[i-1]
        instantes.append(t_atual)

        linha_atual.append(round(float(t_atual),5))
        linha_atual.append(ax[i])
        linha_atual.append(ay[i])
        linha_atual.append(az[i])

        saida.write(",".join(str(x) for x in linha_atual))
        saida.write("\n")
        i = i+1

    #fechando io e preparando o proximo arquivo
    entrada.close()
    saida.close()
    arq_entrada = processing_queue.pop()
    arq_saida = "resultados/proc_" + arq_entrada
