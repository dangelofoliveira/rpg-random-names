#!/usr/bin/python
#coding: utf-8

import random  #importando o módulo para randomizar as letras
import os #importando o módulo os para limpar o console

#definindo a variável como lista para consoantes
consoantes = [
  'b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm',
  'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z'
  ]
 
#definindo a variável como lista para vogais
vogais = ['a', 'e', 'i', 'o', 'u', 'w', 'y']


# Introduz o usuário ao programa com saudação e explicações
print('-' * 100)
print('Bem vindo ao gerador de nomes aleatórios para seu personagem de RPG!\n'.center(100))
print('A mecânica é simples.\n'.center(100))
print('Você escolhe um número de consoantes e vogais e o programa cria o nome aleatoriamente para você.\n'.center(100))
print('Enjoy it!!!\n'.center(100))
print('-' * 100)

#Criando função para receber o número de letras desejado para o nome
def get_name():
  nome = [] #Criando lista vazia para receber as vogais e consoantes
  
  while True:
      try:
          num_consoantes = int(input('\nDigite o número de consoantes para o nome desejado: '))
      except ValueError:
          print('\nVocê só pode digitar números inteiros para este campo.')
      else:
          break
  while True:
      try:
          num_vogais = int(input('\nDigite o número de vogais para o nome desejado: '))
      except ValueError:
          print('\nVocê só pode digitar números inteiros para este campo.')
      else:
          break
  
  
  #limpar o console
  os.system("clear")
  
  # este for escolhe, aleatoriamente, uma quantidade de elementos da lista consoantes de acordo com o número que o usuário escolheu e adiciona na lista nome
  for num in range(num_consoantes):
      nome.append(random.choice(consoantes))
  # este for escolhe, aleatoriamente, uma quantidade de elementos da lista vogais de acordo com o número que o usuário escolheu e adiciona na lista nome
  for num in range(num_vogais):
    nome.append(random.choice(vogais))
  # embaralhar aleatoriamente a lista
  random.shuffle(nome)
  # converte lista em string unindo todos os elementos e deixando a primeira letra maiúscula
  return print('\nO nome do seu personagem será: ',''.join(nome).capitalize())

#Chama a função
get_name()

print('-' * 50)




#Criar um laço perguntar ao usuário se ele quer escolher um novo nome
while True:
  choice = input('\nDeseja criar um novo nome? (S) para Sim - (N) para Não: ')
  
  #limpar o console
  os.system('clear')
  
  #Cria uma lista com strings para Sim ou Não
  lista_choice = ['S', 's', 'N', 'n']

  #Este while valida a escolha do usuário para apenas os elementos de lista_choice
  while choice not in lista_choice:
    choice = input('\nEscolha (S) para Sim ou (N) para Não: ')
    os.system('clear') #limpar o console
  else:
    if (choice == 'S') or (choice == 's'):
      get_name()
      print('-' * 100)
    else:
      print('-' * 100)
      print('\nObrigado por usar o gerador de nomes aleatórios para RPG!\n')
      print('Espero que tenha sido de grande ajuda!\n')
      print('Até a próxima!\n')
      print('-' * 100)
      break
