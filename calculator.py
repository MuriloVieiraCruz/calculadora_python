# Biblioteca

import math

# Váriaveis

def realizar_operaoes_simples(operacao):
    numero1 = input("Digite o primeiro número: ")

    if operacao == 5:
        numero2 = input("Digite a potência: ")
    else:
        numero2 = input("Digite o segundo número: ")

    if operacao == 1:
        resultado = numero1 + numero2
    elif operacao == 2:
        resultado = numero1 - numero2
    elif operacao == 3:
        resultado = numero1 * numero2
    elif operacao == 4:
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return
    elif operacao == 5:
        resultado = numero1 ** numero2

    print("O resultado é: ", resultado)

def realizar_operaoes_seno_cosseno(operacao):
    ang = int (input("Digite o ângulo: "))
    rad = math.radians(ang)

    if operacao == 6:
         resultado = math.sin(rad)
    else:
        resultado = math.cos(rad)

    print("O resultado é: ", resultado)

def raiz_quadrada(x):
    if x < 0:
        return "Erro: Raiz quadrada de número negativo não é permitida."
    return math.sqrt(x)

def percentual(parte, total):
    if total == 0:
        return "Erro: Divisão por zero não é permitida."
    return (parte / total) * 100

def fatorial(x):
    if x < 0:
        return "Erro: Fatorial de número negativo não é permitido."
    return math.factorial(x)
    

while True:
     
    print("\nEscolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Seno")
    print("7. Cosseno")
    print("8. Raiz Quadrada")
    print("9. Percentual")
    print("10. Fatorial")
    print("11. Sair")

    operacao =  input("Digite o número da operação desejada: ")

    # Operadores

    if operacao.isnumeric():
        operacao = int(operacao)

        if operacao in [1,2,3,4,5]:
            realizar_operaoes_simples(operacao)
        elif operacao in [6,7]:
             realizar_operaoes_seno_cosseno(operacao)
        elif operacao == 8:
            num = float(input("Digite um número: "))
            print("Raiz Quadrada de", num, "é", raiz_quadrada(num))
        elif operacao == 9:
            parte = float(input("Digite a parte: "))
            total = float(input("Digite o total: "))
            print("Percentual é", percentual(parte, total), "%")
        elif operacao == 10:
            num = int(input("Digite um número inteiro: "))
            print("Fatorial de", num, "é", fatorial(num))
        elif operacao == 11:
            print("Encerrando a calculadora...")
            break
        else:
            print("Operação não suportada")
    else:
        print('Por favor, insira um número válido')
    
