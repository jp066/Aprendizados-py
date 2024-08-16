class Cachorro:
	def __init__(self, nome, cor, acordado=True):
		self.nome = nome
		self.cor = cor
		self.acordado = acordado
	
	def latir(self):
		print("auau")
		
	
	def dormir(self):
		self.acordado = False
		print('Zzzzzz')
# Instanciando a classe. explicando o que é instanciar:
# Instanciar é criar um objeto a partir de uma classe.
# O objeto é uma instância da classe.
# A classe é o molde, o objeto é o produto final.
# O objeto é um dado.
# A classe é um modelo.
		

cao_1 = Cachorro('rabito', 'branco', False)
cao_2 = Cachorro('aladim', 'branco e preto')
# Atributos são as características do objeto.
# Métodos são as ações do objeto.

cao_1.latir()

cao_2.dormir()

print(cao_1.acordado)
print(cao_2.acordado)