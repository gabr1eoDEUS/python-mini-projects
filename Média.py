#Importando bibliotecas
from colorama import Fore, Back, Style
from time import sleep
import os


#Laço de repetição
while True:
    #Limpando a tela
    def limpa_tela():
        os.system('cls')
    

    #Cabeçalho
    print(Fore.MAGENTA+'=' * 27+Style.RESET_ALL )
    print('Calculadora de Média Anual.')
    print('-----Feito por Gabriel-----')
    print(Fore.MAGENTA+'=' * 27+Style.RESET_ALL+'\n')
    #Pegando as informações do user e usando o try(Em casos de digitação inválida)
    try:
        n1 = float(input('Primeiro bimestre: '))
        n2 = float(input('Segundo bimestre:  '))
        n3 = float(input('Terceiro bimestre: '))
        n4 = float(input('Quarto bimestre:   '))
    except ValueError:
        print('Entrada inválida. Por favor, digite um número válido.\n')
        sleep(3)
        limpa_tela()
        continue
    print('\n')
    #Calculando a média
    media = (n1+n2+n3+n4) / 4
    #Tempo para calcular a média
    print('Analisando média anual\nAguarde...\n')
    sleep(3)

    #Fazendo a lógica
    if media >= 6:
        print('Sua média é {:.1f}.'.format(media)+Fore.GREEN+' APROVADO!\n'+Style.RESET_ALL)
    else:
        print('Sua média é {:.1f}.'.format(media)+Fore.RED+' REPROVADO!\n'+Style.RESET_ALL)
    
    #Repetição do programa
    while True:
        opc = str(input('Deseja calcular outra média? [S / N]: ')).upper()
        if opc == 'S':
            limpa_tela()
            break
        elif opc == 'N':
            limpa_tela()
            break
        else:
            print('Opção inválida. tente novamente...')
            sleep(2)
            limpa_tela()
    #Saindo do loop acima
    if opc == 'N':
        break