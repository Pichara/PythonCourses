from random import shuffle
a=input('Primeiro Aluno:')
b=input('Segundo Aluno:')
c=input('Terceiro Aluno:')
d=input('Quarto Aluno:')
lista=[a,b,c,d]
shuffle(lista)
print('A ordem dos alunos é')
print(lista)