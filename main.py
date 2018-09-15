#!/usr/bin/python
#coding: utf-8

import random  #importando o módulo para randomizar as letras

#definindo a variável como lista para consoantes
consoantes = [
  'b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm',
  'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z'
  ]
 
#definindo a variável como lista para consoantes
vogais = ['a', 'e', 'i', 'o', 'u', 'y', 'w']

# Introduz o usuário ao programa com saudação e explicações
print('-' * 100)
print('Bem vindo ao gerador de nomes aleatórios para seu personagem de RPG!\n'.center(100))
print('A mecânica é simples.\n'.center(100))
print('Você escolhe um número de consoantes e vogais e o programa cria o nome aleatoriamente para você.\n'.center(100))
print('Caso não seja de seu agrado basta rodar novamente para criar um novo nome.\n'.center(100))
print('Enjoy it!!!\n'.center(100))
print('-' * 100)
print('\n')

#Criando função para receber o número de letras desejado para o nome
def get_name():
  nome = [] #Criando lista vazia para receber as vogais e consoantes
  num_consoantes = int(input('Digite o número de consoantes para o nome desejado: ')) 
  num_vogais = int(input('Digite o número de vogais para o nome desejado: '))
  for num in range(num_consoantes): # este for escolhe uma consoante aleatória de acordo com o número que o usuário escolheu e adiciona na lista
    nome.append(random.choice(consoantes))
  for num in range(num_vogais): # este for escolhe uma vogal aleatória de acordo com o número que o usuário escolheu e adiciona na lista
    nome.append(random.choice(vogais))
  random.shuffle(nome) # embaralhar aleatoriamente a lista
  return print('\nO nome do seu personagem será: ', ''.join(nome).capitalize()) # converte lista em string unindo todos os elementos e deixando a primeira letra maiúscula

print(get_name()) #imprimindo o resultado na tela

print('-' * 50)



while True:
  choice = input('Deseja criar um novo nome? (S) para Sim - (N) para Não: ') #pergunta ao usuário se ele deseja criar outro nome
  lista_choice = ['S', 's', 'N', 'n']

  while choice not in lista_choice:
    choice = input('Escolha (S) para Sim ou (N) para Não: ')
  else:
    if (choice == 'S') or (choice == 's'):
      print(get_name())
      print('-' * 50)
    else:
      print('-' * 50)
      print('\nObrigado por usar o gerador de nomes aleatórios para RPG!\n')
      print('Espero que tenha sido de grande ajuda!\n')
      print('Até a próxima!\n')
      print('-' * 50)
      break
