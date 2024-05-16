# Biblioteca

import math

# Métodos

def realizar_operaoes_simples(operacao):
    numero1 = float(input("Digite o primeiro número: "))

    if operacao == 5:
        numero2 = float(input("Digite a potência: "))
    else:
        numero2 = float(input("Digite o segundo número: "))

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

    apresenta_resultado(resultado)

def realizar_operaoes_seno_cosseno(operacao): 
    ang = int(input("Digite o ângulo: "))
    rad = math.radians(ang)

    if operacao == 6:
         resultado = round(math.sin(rad), 3)
    else:
        resultado = round(math.cos(rad), 3)

    apresenta_resultado(resultado)

def raiz_quadrada():
    num = float(input("Digite um número: "))
    if num < 0:
        return "Erro: Raiz quadrada de número negativo não é permitida."
    resultado = round(math.sqrt(num), 3)

    apresenta_resultado(resultado)

def percentual(): 
    parte = float(input("Digite a parte: "))
    total = float(input("Digite o total: "))
    if total == 0:
        return "Erro: Divisão por zero não é permitida."
    resultado =  (parte / total) * 100

    apresenta_resultado(resultado)

def fatorial():
    num = int(input("Digite um número inteiro: "))
    if num < 0:
        return "Erro: Fatorial de número negativo não é permitido."
    resultado = math.factorial(num)

    apresenta_resultado(resultado)
    

def apresenta_resultado(resultado):
    print("\n O resultado é: ", resultado)

    # Menu Inicial

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
            raiz_quadrada()
        elif operacao == 9:
            percentual()
        elif operacao == 10:
            fatorial()
        elif operacao == 11:
            print("Encerrando a calculadora...")
            break
        else:
            print("Operação não suportada")
    else:
        print('Por favor, insira um número válido')