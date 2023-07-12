from random import choice
a=input('Primeiro Aluno:')
b=input('Segundo Aluno:')
c=input('Terceiro Aluno:')
d=input('Quarto Aluno:')
lista=(a,b,c,d)
x=choice(lista)
print('Quem apagará o quadro será {}'.format(x))