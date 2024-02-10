#Faca um programa que leia o nome de uma pessoa e exiba uma mensagem de boas-vindas.

nome = input('Qual é o seu nome? ')
print('Olá, ' + nome + '! Prazer em te conhecer!')

nome = input('Qual é o seu nome? ')
print('Olá, {}, seja bem-vinda(a)!'.format(nome))