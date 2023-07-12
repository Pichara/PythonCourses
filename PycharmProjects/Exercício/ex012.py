p =float(input('qual é o preço do produto? R$'))
l=float(input('qual é o desconto do produto? %'))
x=(p*l)
d=(x/100)
r=(p-d)
print('O produto que vale R${} valerá na liquidação R${}'.format(p,r))


