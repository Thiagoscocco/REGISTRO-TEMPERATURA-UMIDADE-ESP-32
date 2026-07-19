
from tkinter import *
import recepcao_dados
import time
import os

def tempo_real ():
    print ('antes')
    leitura_temp, leitura_umid = recepcao_dados.ler_serial ()
    time.sleep (0.2)
    leitura_ok = (f'OK')
    check_leitura["text"] = "OK"
    janela.after(200, lambda: check_leitura.config(text="Lendo"))
    check_leitura["text"] = leitura_ok
    print ('depois')

    visor_temp = f'''{leitura_temp}°C'''
    visor_umid = f'''{leitura_umid}%'''

    visor_temperatura["text"] = visor_temp
    visor_umidade ["text"] = visor_umid

    fonte_negrito=("Arial", 15, "bold")
    cor_cinza= "black"

    visor_temperatura["font"] = fonte_negrito
    visor_umidade["font"]= fonte_negrito

    visor_temperatura["fg"]= cor_cinza
    visor_umidade["fg"]= cor_cinza

    mensagem_aviso = (f'Leitura em Andamento...')    
    texto_aviso ["text"]=  mensagem_aviso
    
    janela.after(1000, tempo_real)

janela = Tk ()
janela.title ("Temperatura e Umidade")
janela.geometry('330x320')
janela.resizable(False, False)

janela.rowconfigure (0, weight=1)
janela.rowconfigure (1, weight=1)
janela.rowconfigure (2, weight=1)
janela.rowconfigure (3, weight=3)
janela.rowconfigure (4, weight=1)
janela.rowconfigure (5, weight=1)

janela.columnconfigure (0, weight=1)
janela.columnconfigure (1, weight=1)

## FRAME DOS BOTÕES (5)
frame_botoes = Frame (janela, borderwidth=1, relief="raised")
frame_botoes.grid (column= 0, row= 5, padx= 10, pady= 10, ipadx= 50, columnspan=2)

frame_botoes.columnconfigure(0, weight=0)
frame_botoes.columnconfigure(1, weight=0)

## FRAME DO VISOR
frame_visor = Frame (janela, width= 290, height= 90, borderwidth=1, relief="raised")
frame_visor.grid (column= 0, row= 2, padx= 10, pady= 10, ipadx= 50, ipady=20,  columnspan=2)
frame_visor.grid_propagate(False)

frame_visor.rowconfigure (0, weight=1)
frame_visor.rowconfigure (1, weight=1)

frame_visor.columnconfigure(0, weight=1)

## TEXTO DO TÍTULO (0) 
texto_inicial = Label (janela, text= "Temperatura e Umidade DHT 11")
texto_inicial.grid (column= 0, row= 0, padx= 10, pady= 15, sticky= "n", columnspan=2)

## TEXTO DE AVISO (1)
texto_aviso= Label (janela, text="")
texto_aviso.grid (column= 0, row= 1, padx= 1, pady= 1, columnspan=2)

## VISOR DE TEMPERATURA (FRAME O)
visor_temperatura = Label (frame_visor, text= "Aguardando Leitura de Temperatura",fg= "gray", font= ("Arial", 11, "italic"))
visor_temperatura.grid(column= 0, row= 0, padx= 10, pady=5, columnspan=2)

## VISOR DE UMIDADE (FRAME 1)
visor_umidade = Label (frame_visor, text= "Aguardando Leitura de Umidade", fg= "gray", font= ("Arial", 11, "italic"))
visor_umidade.grid(column= 0, row= 1, padx= 10, pady=5, columnspan=2)

## CHECK DE LEITURA (FRAME 2)
check_leitura = Label (frame_visor, text= "", fg= "red", font= ("Arial", 8, "italic"))
check_leitura.grid(column= 0, row= 2, padx= 5, pady=5, columnspan=2, sticky="se")

##TEXTO DE ORIENTAÇÃO (4)
texto_orientacao = Label(janela, text= "Clique em Registrar para Iniciar o Registro")
texto_orientacao.grid (column= 0, row= 4, padx= 10, pady= 3, columnspan=2)

##BOTÃO DE REGISTRAR TEMPERATURA E UMIDADE
botao_registrar = Button(frame_botoes, text = "Registrar", command= None, width=15)
botao_registrar.grid (column= 0, row= 0, padx= 2, pady= 10, sticky="s")

## BOTÃO DE REINICIAR LEITURAS 
botao_reiniciar = Button (frame_botoes, text= "Tempo Real", command= tempo_real, width=15)
botao_reiniciar.grid (column=1, row = 0, padx=2, pady = 10, sticky="s")



















janela.mainloop()