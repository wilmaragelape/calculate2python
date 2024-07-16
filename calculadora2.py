#************************** Calculadora em Python ******************************

print('Selecione o número da operação desejada: \n  1 - Soma \n  2 - Subtração \n  3 - Multiplicação \n  4 - Divisão \n')
selecione = int(input("Digite sua opção (1/2/3/4): "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if selecione == 1:
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
    
elif selecione == 2:
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif selecione == 3:
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
    
elif selecione == 4:
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado}")

else:
    print("Opção inválida. Por favor, selecione 1, 2, 3 ou 4.")