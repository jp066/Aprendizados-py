class Curso:
    def __init__(self, nome, descricao, instrutor, alunos=[]): # alunos é uma lista vazia por padrão
        self.nome = nome
        self.descricao = descricao
        self.instrutor = instrutor # Instrutor é uma classe, e instrutor é um objeto dessa classe
        self.alunos = alunos
        
    def __str__(self):
        alunos_nomes = ', '.join([aluno.nome for aluno in self.alunos])
        return f'''
    Curso: {self.nome}
    Descrição: {self.descricao}
    Instrutor: {self.instrutor.nome}
    alunos: {alunos_nomes}
    '''

    def adicionar_aluno(self, *aluno):
        self.alunos.extend(aluno)
        
    def remover_aluno(self, aluno):
        self.alunos.remove(aluno)
        
    def exibir_infos(self): # so foi passado self porque os atributos são da propria classe
        print(f'Nome: {self.nome}') # mesmo eu tendo o nome do aluno e instrutor, eu posso acessar o nome do curso pois o que foi passado de parametro foi o self (que é o objeto da classe)
        print(f'Descrição: {self.descricao}')
        print(f'Instrutor: {self.instrutor.nome}') # instrutor é um objeto da classe Instrutor, e eu quero acessar o nome desse objeto
        print('Alunos:')
        for aluno in self.alunos:
            print(f'Nome: {aluno.nome}, Idade: {aluno.idade}')
        
        
class Instrutor:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        
    def exibir_infos(self): # so foi passado self porque os atributos são da propria classe
        print(f'Nome: {self.nome}')
        print(f'Especialidade: {self.especialidade}')
        
        
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
    def exibir_infos(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        
        

Instrutor = Instrutor('Lucas', 'Programação')
aluno1 = Aluno('João', 20)
aluno2 = Aluno('Maria', 25)
aluno3 = Aluno('Pedro', 30)
aluno4 = Aluno('Fernando', 30)
aluno5 = Aluno('Jacinto', 27)
aluno6 = Aluno('Joaquim', 30)
aluno7 = Aluno('Jose', 19)
aluno8 = Aluno('Hevely', 24)
curso = Curso('Python', 'Curso de Python', Instrutor)


curso.adicionar_aluno(aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8)
curso.exibir_infos()