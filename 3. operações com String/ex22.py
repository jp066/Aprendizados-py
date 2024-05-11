nome_completo = str(input('digite seu nome: ')).strip()
separador = nome_completo.split()

print(f'seu nome em maiusculas é {nome_completo.upper()}')
print(f'seu nome em minusculas é {nome_completo.lower()}')
print(f'há {len(nome_completo) - nome_completo.count(' ')} letras no nome')
print(f'há {len(separador[0])} caracteres no primeiro nome')