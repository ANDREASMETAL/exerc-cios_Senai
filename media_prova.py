print('Ola, seja bem vindo.')
provas= int(input('Por favor imforme a quantia de provas que o aluno realizou: '))
contador=1
soma=0

while contador <= provas:
    print('|',30*'-','|')
    nota = float(input(f'Digite a nota da prova {contador}: '))
    soma = soma+ nota
    contador = contador+1
    
media= soma/ provas
print('|',30*'-','|')
print(f'A media do aluno é {media:.2f}')