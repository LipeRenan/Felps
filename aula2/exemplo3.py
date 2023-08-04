#Leia a idade do usuário e informe se ele é maior ou menor de idade
#verificar números negativo antes da idade
idade = int(input("Informe sua idade:"))
if idade<0:
    print("Idade inválida!!!")
    print("Verifique o valor informado.")
else:
    if idade>=18:
         print("você é maior de idade!")
    else:
        print("Você é menor de idade!")
        

