# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep
from termcolor import colored
from pydoc import help

def ajuda(comando):
    print(colored(f'Acessando o manual do comando \'{comando}\'...', 'blue'))
    sleep(2)
    help(comando)
    
while True:
    print(colored('-=' * 20, 'yellow'))
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    ajuda(comando)