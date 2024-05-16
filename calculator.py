# Biblioteca

import math

def somar():
    try:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))
        return numero1 + numero2
    except ValueError:
        print("\n")
        print("Digite um número válido")

def subtracao():
    try:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))
        return numero1 - numero2
    except ValueError:
        print("\n")
        print("Digite um número válido")

def multiplicacao():
    try:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))
        return numero1 * numero2
    except ValueError:
        print("\n")
        print("Digite um número válido")

def divisao():
    try:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))

        if numero2 == 0:
            print("A divisão não pode ser por 0")
        return numero1 / numero2
    except ValueError:
        print("\n")
        print("Digite um número válido")

def potencia():
    try:
        numero1 = float(input("Digite o número: "))
        numero2 = float(input("Digite a potência: "))
        return numero1 ** numero2
    except ValueError:
        print("\n")
        print("Digite um número válido")

def seno():
    try:
        ang = int (input("Digite o ângulo: "))
        rad = math.radians(ang)
        return round(math.sin(rad), 3)
    except ValueError:
        print("\n")
        print("Digite um número válido")

def cosseno():
    try:
        ang = int (input("Digite o ângulo: "))
        rad = math.radians(ang)
        return round(math.con(rad), 3)
    except ValueError:
        print("\n")
        print("Digite um número válido")

def raiz():
    try:
        numero = float(input("Digite um número: "))
        if numero < 0:
            print("Erro: Raiz quadrada de número negativo não é permitida.")
            return
        return round(math.sqrt(numero), 3)
    except ValueError:
        print("\n")
        print("Digite um número válido")

def percentual():
    try:
        parte = float(input("Digite a parte: "))
        total = float(input("Digite o total: "))
        if total == 0:
            return "Erro: Divisão por zero não é permitida."
        return (parte / total) * 100
    except ValueError:
        print("\n")
        print("Digite um número válido")

def fatorial():
    try:
        num = int(input("Digite um número inteiro: "))
        if num < 0:
            return "Erro: Fatorial de número negativo não é permitido."
        return math.factorial(num)
    except ValueError:
        print("\n")
        print("Digite um número válido")

def mostrar_resultado(resultado):
    if resultado != None:
        print("\n")
        print("==========================")
        print("O resultado é: ", resultado)
        print("==========================")
    

# Tela

while True:

    print("\n")
    print("====================================================")
    print("***CALCULADORA***")
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
    print("====================================================")
    operacao = input("\nDigite o número da operação desejada: ")
    

# Operadores

    if operacao.isnumeric():
        operacao = int(operacao)

        if operacao == 1:
            resultado = somar()
            mostrar_resultado(resultado)

        elif operacao == 2:
            resultado = subtracao()
            mostrar_resultado(resultado)

        elif operacao == 3:
            resultado = multiplicacao()
            mostrar_resultado(resultado)

        elif operacao == 4:
             resultado = divisao()
             mostrar_resultado(resultado)
        
        elif operacao == 5:
            resultado = potencia()
            mostrar_resultado(resultado)

        elif operacao == 6:
            resultado = seno()
            mostrar_resultado(resultado)

        elif operacao == 7:
            resultado = cosseno()
            mostrar_resultado(resultado)

        elif operacao == 8:
            resultado = raiz()
            mostrar_resultado(resultado)

        elif operacao == 9:
            resultado = percentual() 
            mostrar_resultado(resultado)

        elif operacao == 10:
            resultado = fatorial()
            mostrar_resultado(resultado)

        elif operacao == 11:
            print("Encerrando a calculadora...")
            break

        else:
            print("Insira um número válido")
    else:
	    print("\n Ação não suportada")