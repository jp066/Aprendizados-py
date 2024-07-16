# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo()]
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from funcoes import aumentar_moeda, diminuir_moeda, dobrar_moeda, metade_moeda, moeda

def resumo(valor, aumento, reducao):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobrar_moeda(valor, True)}')
    print(f'Metade do preço: \t{metade_moeda(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar_moeda(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir_moeda(valor, reducao, True)}')
    print('-' * 30)
    print()