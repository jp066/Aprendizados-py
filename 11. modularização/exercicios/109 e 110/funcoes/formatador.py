def moeda(valor):
    """
    -> Recebe um valor e retorna ele formatado como moeda.
    :param valor: valor a ser formatado
    :return: valor formatado como moeda
    """    
    return f'R${valor:.2f}'.replace('.', ',')