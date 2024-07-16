# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações: 
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*notas, situacao=False):
    relatorio_notas = {
        'quantidade': len(notas),
        'maior': max(notas),
        'menor': min(notas),
        'media': sum(notas) / len(notas)
    }
    
    if situacao:
        if relatorio_notas['media'] >= 7:
            relatorio_notas['situacao'] = 'Aprovado'
        elif relatorio_notas['media'] >= 5:
            relatorio_notas['situacao'] = 'Recuperação'
        else:
            relatorio_notas['situacao'] = 'Reprovado'
    
    return relatorio_notas

# Exemplo de uso da função
notas_alunos = []
for aluno in range(1, 5):
    nota = float(input(f'{aluno}° Nota do aluno: '))
    notas_alunos.append(nota)

deseja_situacao = input('Deseja ver a situação? [S/N] => ').strip().upper() == 'S'
relatorio = notas(*notas_alunos, situacao=deseja_situacao)

print(f'''\nRelatório de notas:
      Quantidade de notas: {relatorio['quantidade']}
      Maior nota: {relatorio['maior']}
      Menor nota: {relatorio['menor']}
      Média da turma: {relatorio['media']}
      Situação: {relatorio['situacao'] if 'situacao' in relatorio else 'Não informada'}''')
