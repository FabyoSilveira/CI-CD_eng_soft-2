from Calculator import Calculator
import re

calc = Calculator()

print('Operações suportadas - Soma | Subtração | Multiplicação | Divisão')

numberInput = input('Escreva dois números inteiros que deseja operar separados por virgula:\n')
operationInput = input('Escreva o símbolo matemático para realizar sua operação:\n')

logicOperationArray = re.split(',', numberInput)

if operationInput == '+':
  print('O resultado da sua operação é: ', calc.sum(int(logicOperationArray[0]), int(logicOperationArray[1])))
elif operationInput == '-':
  print('O resultado da sua operação é: ', calc.sub(int(logicOperationArray[0]), int(logicOperationArray[1])))
elif operationInput == '*':
  print('O resultado da sua operação é: ', calc.mult(int(logicOperationArray[0]), int(logicOperationArray[1])))
elif operationInput == '/':
  print('O resultado da sua operação é: ', calc.div(int(logicOperationArray[0]), int(logicOperationArray[1])))
else:
  print('Operação não suportada!')