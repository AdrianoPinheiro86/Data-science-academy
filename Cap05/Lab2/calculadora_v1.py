# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")


# Função para realizar a adição
def adicao(num1, num2):
    return num1 + num2

# Função para realizar a subtração
def subtracao(num1, num2):
    return num1 - num2

# Função para realizar a multiplicação
def multiplicacao(num1, num2):
    return num1 * num2

# Função para realizar a divisão
def divisao(num1, num2):
    return num1 / num2

# Loop principal
while True:
    print("\nSelecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    escolha = input("Digite a opção desejada (1/2/3/4/5): ")

    if escolha == '5':
        print("Encerrando a calculadora...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = adicao(num1, num2)
        operacao = "+"
    elif escolha == '2':
        resultado = subtracao(num1, num2)
        operacao = "-"
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
        operacao = "*"
    elif escolha == '4':
        if num2 != 0:
            resultado = divisao(num1, num2)
            operacao = "/"
        else:
            print("Erro: divisão por zero!")
            continue
    else:
        print("Opção inválida. Tente novamente.")
        continue

    print("O resultado da operação", num1, operacao, num2, "é:", resultado)
