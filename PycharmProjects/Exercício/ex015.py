dias=int(input('quantos dias o carro ficou alugado?'))
km=float(input('quantos km você andou com o carro alugado?'))
pago=(dias*60)+(km*0.15)
print('Voçe ficou com o carro {} dias e andou {} km \nentão o total a pagar sera de \n======R${:.2f}======'.format(dias, km, pago))