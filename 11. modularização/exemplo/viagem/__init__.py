# __init__.py

# Importando funções principais para facilitar o acesso
from .passaporte import verificar_passaporte, obter_visto
from .destino import planejar_viagem, comprar_passagem

# Definindo __all__
__all__ = ['verificar_passaporte', 'obter_visto', 'planejar_viagem', 'comprar_passagem']

# Código de inicialização (opcional)
print("Inicializando o pacote 'viagem'")
