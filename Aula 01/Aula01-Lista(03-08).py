import os, sys
from time import sleep


def ex1():
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    print(f'A soma entre {x} e {y} é: {x+y}')
    print(f'A diferença entre {x} e {y} é: {x-y}')
    print(f'A multiplicação entre {x} e {y} é: {x*y}')
    print(f'A divisão entre {x} e {y} é: {x/y}')

def ex2():
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    print(f'Olá, {nome}! Você tem {idade} anos!')
    pass

def ex3():
    x = float(input('Digite um número Real: '))

    if x > 0:
        print(f'{x} é um número Positivo!')
    elif x < 0:
        print(f'{x} é um número Negativo!')  
    else:
        print(f'{x} é um número Neutro!')

def ex4():
    nota = float(input('Informe a nota do aluno: '))
    if nota >= 7:
        print('Aluno aprovado!')
    else:
        print('Aluno reprovado!')

def ex5():
    n = int(input('Informe um número inteiro: '))
    for i in range(1,11):
        print(f'{n} x {i:<2} = {n*i}')

def ex6():
    n = int(input('Digite um número inteiro positivo: '))
    soma = 0
    for i in range(1,n+1):
        soma += i
    print(f'A soma dos números entre 1 e {n} é: {soma}')

def ex7():
    numeros = []
    for i in range(1,11):
        numeros.append(int(input(f'Digite um {i}º número: ')))

    print(f'A soma entre os números {numeros} é:  {sum(numeros)}')
    print(f'A média entre os números {numeros} é: {sum(numeros)/len(numeros)}')

def ex8():
    x = 1
    soma = 0
    c = 1
    while x != 0:
        x = int(input(f'Digite o {c}º número a ser somado [0 para encerrar]: '))
        c += 1
        if x == 0:
            print(f'A soma de todos os valores digitados é: {soma}')
            continue
        else:
            soma += x

def ex9():
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    print(f'O maior número entre {x} e {y} é: {maior(x,y)}')

def ex10():
    x = []
    for i in range(1,6):
        x.append(int(input(f'Digite o {i}º número: ')))
    print(f'O menor número em {x} é: {menor(*x)}')
    print(f'O maior número em {x} é: {maior(*x)}')

def menor(*x):
    return min(x)

def maior(*x):
    return max(x)


def inicial():
    finalizar = False

    while not finalizar:
        os.system('cls')
        menu = ['Leia dois números e exiba a soma, subtração, multiplicação e divisão.',
            'Leia o nome e a idade de uma pessoa e exiba uma mensagem com essas informações.',
            'Leia um número e informe se ele é positivo, negativo ou zero.',
            'Leia a nota de um aluno e informe se ele foi aprovado (nota ≥ 7) ou reprovado.',
            'Leia um número inteiro e mostre sua tabuada de 1 a 10.',
            'Leia um número N e calcule a soma dos números de 1 até N.',
            'Leia 10 números e informe a soma e a média.',
            'Leia vários números até que o usuário digite 0. Ao final, informe a soma dos valores digitados.',
            'Crie uma função que receba dois números e retorne o maior deles.',
            'Desafio: Faça um programa que leia 5 números e informe o maior e o menor valor.',
            'Sair'
            ]
        
        print('='*100)
        print('Algorítimos - Aula 01 (03/08/26)'.center(100))
        print('Lista de Exercícios – Revisão Inicial de Algoritmos em Python'.center(100))
        print('='*100)
        for k,v in enumerate(menu, start=1) :
            print(f'[{k:02}] - {v}')
        print('='*100)
        op = int(input('Digite uma opção: '))

        match op:
            case 1:
                os.system('cls')
                ex1()
            case 2:
                os.system('cls')
                ex2()
            case 3:
                os.system('cls')
                ex3()
            case 4:
                os.system('cls')
                ex4()
            case 5:
                os.system('cls')
                ex5()
            case 6:
                os.system('cls')
                ex6()
            case 7:
                os.system('cls')
                ex7()
            case 8:
                os.system('cls')
                ex8()
            case 9:
                os.system('cls')
                ex9()
            case 10:
                os.system('cls')
                ex10()
            case 11:
                print('Programa encerrado...')
                sys.exit()
            case _:
                print('Opção Inválida.')
                sleep(1)
                continue

        print('='*100)
        escolha = input('Tecle [Enter] para voltar ao menu ou digite "sair" para encerrar.').lower()
        if escolha == 'sair':
            finalizar = True
            print('Programa encerrado...')
        else:
            continue

inicial()