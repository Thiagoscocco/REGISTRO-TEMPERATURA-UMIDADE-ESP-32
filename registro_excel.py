import os
import time
import csv
import random
from datetime import datetime
#from input_dados import temperatura_esp, umidade_esp

def simular_dados (): 
    temp_esp = random.randint (12, 25)
    umid_esp = random.randint (78, 92)
    linha_dados = f' {temp_esp},{umid_esp}'
    return linha_dados

def converter_dados ():
    dado_bruto = simular_dados ().split (",")

    temperatura = dado_bruto [0]
    umidade = dado_bruto [1]
    return temperatura, umidade

def converter_data_hora ():
    agora = datetime.now ()

    data = agora.strftime ("%d/%m/%y")
    hora = agora.strftime ("%H:%M:%S")
    return data, hora

def criar_csv ():
        
    with open ("teste.csv", "w", newline="") as arquivo:
        infos_linha = csv.writer (arquivo)
        infos_linha.writerow (["Data","Hora","Temperatura (°C)","Umidade (%)"]) 

def escrever_csv ():
    contagem = 0
    while True:
        temperatura, umidade = converter_dados ()
        data, hora = converter_data_hora ()
        contagem += 1
        if contagem <= 10:
            time.sleep (2)
            print ("Rodando Leituras...")
            with open ("teste.csv", "a", newline= "") as arquivo:
                adicao = csv.writer (arquivo)
                adicao.writerow ([data,hora,temperatura,umidade])
        else:
            break

criar_csv ()
escrever_csv ()