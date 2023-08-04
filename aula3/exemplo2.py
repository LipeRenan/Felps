#Operadores lógicos
n1 = 500
n2 = 1000
n3 = 1250
#Operador lógico E>(and)
print("Verificação do n1:",n1>n2 and n1>n3)
print("Verificação do n2:",n2>n1 and n2>n3)
print("Verificação do n3:",n3>n1 and n3>n2)
#Operador lógico OU>(or)
print("Verificação do n1:",n1>n2 or n1>n3)
print("Verificação do n2:",n2>n1 or n2>n3)
print("Verificação do n3:",n3>n1 or n3>n2)
#operador lógico NÃO>(not)
print("Verificação do n1:",not(n1>n2 or n1>n3))
print("Verificação do n2:",not(n2>n1 or n2>n3))
print("Verificação do n3:",not(n3>n1 or n3>n2))


