
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))

operacao = input("Digite a operacao que deseja realizar (+ , - , * , /): ")

if operacao == '+':
    print(num1 + num2)


elif operacao == '-':
    print(num1 - num2)

elif operacao == '*':
    print(num1 * num2)


elif operacao == '/':
    print(num1 / num2)

else :
    print("Operacao invalida!!!")
