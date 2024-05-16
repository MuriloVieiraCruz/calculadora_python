# Biblioteca

import math

def somar():
    numero1 = float (input("Digite o primeiro número: "))
    numero2 = float (input("Digite o segundo número: "))
    resultado = numero1 + numero2

def diminuir():
    numero1 = float (input("Digite o primeiro número: "))
    numero2 = float (input("Digite o segundo número: "))
    resultado = numero1 - numero2

def multiplicar():
    numero1 = float (input("Digite o primeiro número: "))
    numero2 = float (input("Digite o segundo número: "))
    resultado = numero1 * numero2
    mostrar_resultado(resultado)

def dividir():
    numero1 = float (input("Digite o primeiro número: "))
    numero2 = float (input("Digite o segundo número: "))
    resultado = numero1 / numero2
    mostrar_resultado(resultado)

def potencia():
    numero1 = input("Digite o número: ")
    numero2 = input("Digite a potência: ")
    resultado = numero1 ** numero2
    mostrar_resultado(resultado)

def seno():
    ang = int (input("Digite o ângulo: "))
    rad = math.radians(ang)
    resultado = round(math.sin(rad), 3)
    mostrar_resultado(resultado)

def cosseno():
    ang = int (input("Digite o ângulo: "))
    rad = math.radians(ang)
    resultado = round(math.con(rad), 3)
    mostrar_resultado(resultado)

def raiz():
    numero = float(input("Digite um número: "))
    if numero < 0:
        return "Erro: Raiz quadrada de número negativo não é permitida."
    resultado = round(math.sqrt(numero), 3)
    mostrar_resultado(resultado)

def percentual():
    parte = float(input("Digite a parte: "))
    total = float(input("Digite o total: "))
    if total == 0:
        return "Erro: Divisão por zero não é permitida."
    resultado =  (parte / total) * 100
    mostrar_resultado(resultado)

def fatorial():
    num = int(input("Digite um número inteiro: "))
    if num < 0:
        return "Erro: Fatorial de número negativo não é permitido."
    resultado = math.factorial(num)
    mostrar_resultado(resultado)

def mostrar_resultado(resultado):
    print("O resultado é: ", resultado)

# Tela

while True:

    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Seno")
    print("7 - Cosseno")
    print("8 - Raiz")
    print("9 - Percentual")
    print("10 - Fatorial")
    print("11- Sair")
    operacao = input("\nDigite o número da operação desejada: ")

# Operadores

    if operacao.isnumeric():

        if operacao == 1:
            somar()

        if operacao == 2:
            diminuir()

        if operacao == 3:
            multiplicar()

        if operacao == 4:
            dividir()
        
        if operacao == 5:
            potencia()

        if operacao == 6:
            seno()

        if operacao == 7:
            cosseno()

        if operacao == 8:
            raiz()

        if operacao == 9:
            percentual() 

        if operacao == 10:
            fatorial()

        if operacao == 11:
            print("Encerrando a calculadora...")
            break

    else:
	    print("Insira um número válido")