import serial
import time

esp = serial.Serial('/dev/ttyUSB0', 115200)

def ler_serial ():
    linha = esp.readline().decode().strip().split()
    leitura_temp = linha[0]
    leitura_umid = linha [1]

    return leitura_temp, leitura_umid

