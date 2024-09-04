# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
import datetime

pessoas = []

while True:
    nome = str(input('Nome: '))
    ano_nascimento = int(input('Ano de nascimento: '))
    ano_atual = datetime.datetime.now().year
    carteira_trabalho = int(input('Carteira de trabalho (0 não tem): '))
    
    if carteira_trabalho == 0:
        dados = {'nome': nome, 'ano de nascimento': ano_nascimento, 'carteira de trabalho': carteira_trabalho, 'aposentadoria': 'Não aplicável', 'salario': 'Não aplicável'}  # Passo 2: Cria o dicionário
        pessoas.append(dados) # Passo 3: Adiciona o dicionário à lista
        print(f'{nome} tem {ano_atual - ano_nascimento} anos e não tem carteira de trabalho.')
        print("-" * len(f'{nome} tem {ano_atual - ano_nascimento} anos e não tem carteira de trabalho.'))
        opcao = str(input('Deseja continuar? [S/N]: '))
        if opcao in 'Naonao':
            break
        else:
            continue
    
    if carteira_trabalho != 0:
        ano_contratacao = int(input('Ano de contratação: '))
        salario = float(input('Salário: R$'))
        aposentadoria = ano_contratacao + 35
        print(f'{nome} tem {ano_atual - ano_nascimento} anos e vai se aposentar com {aposentadoria - ano_nascimento} anos. E hoje recebe R${salario:.2f} de salário.')
        dados = {'nome': nome, 'ano de nascimento': ano_nascimento, 'carteira de trabalho': carteira_trabalho, 'ano de contratacao': ano_contratacao, 'salario': salario, 'aposentadoria': aposentadoria}  # Passo 2: Cria o dicionário com todos os dados
        pessoas.append(dados)
        opcao = str(input('Deseja continuar? [S/N]: '))
        if opcao in 'Naonao':
            break
        else:
            continue

for pessoa in pessoas:
    print(pessoa)
    print("-" * len(str(pessoa)))