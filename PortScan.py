import socket
from os import system
from time import sleep


def main():
    system('clear' or 'cls')
    
    print("---------- PortScan ----------")

    host =  input("Informa o endereço IP ou um endereço DNS: ")
    escolha = input(("Deseja utilizar o intervalo de portas padrão (1 - 1024) - S/N?: ")).upper()


    if escolha == 'S':
        print("\n-> Escaneando o intervalo de portas padrão...\n")
        PortScanPadrao(host)

    elif escolha == 'N':
        inicioRange = int(input("\nInforme o INÍCIO do intervalo de portas: "))
        fimRange = int(input("Informe o FINAL do intervalo de portas: "))

        if inicioRange > 0 and fimRange <= 65535:
            print("\n-> Escaneando o intervalo de portas informado ...\n")
            PortScanModificado(host, inicioRange, fimRange)

        else:
            print("\nIntervalo de portas INVÁLIDO, reiniciando o programa ...")
            sleep(2)
            main()

    else:
        print("Formato de resposta incorreto, responda apenas com 'S' ou 'N', reiniciando o programa...")
        sleep(2)
        system('clear') or None
        main()


def PortScanPadrao(enderecoHost):
    
    servicosIdentificados = {}

    for porta in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        verificaPorta = sock.connect_ex((enderecoHost, porta))

        if verificaPorta == 0:
            try:
                servico = socket.getservbyport(porta)
                servicosIdentificados[porta] = servico

            except:
                servicosIdentificados[porta] = 'NOT FOUND'

    for x in servicosIdentificados:
        print("PORTA: {} --- STATUS: OPEN --- SERVICE: {}".format(x, servicosIdentificados[x]))


def PortScanModificado(enderecoHost, inicioRange, fimRange):
        
    servicosIdentificados = {}

    for porta in range(inicioRange, fimRange + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        verificaPorta = sock.connect_ex((enderecoHost, porta))

        if verificaPorta == 0:
            try:
                servico = socket.getservbyport(porta)
                servicosIdentificados[porta] = servico

            except:
                servicosIdentificados[porta] = 'NOT FOUND'

    for x in servicosIdentificados:
        print("PORTA: {} --- STATUS: OPEN --- SERVICE: {}".format(x, servicosIdentificados[x]))


main()
