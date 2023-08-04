#Estruturas de decisão(condicional
#Leia a idade do aluno(a) e defina sua categoria de acordo com as seguintes informações:
# Categorias - idade
# Sem categoria - menor do que 3
# Infantil - 3 até 10
# Juvenil - 11 até 17
# Adulto - 18 até 39
# Senior - 40 até 130
# Acima de 130 - Idade inválida

idade = int(input("Informe sua Idade:"))

if idade<3:
    print("Idade inválida!!!")
elif idade<=10:
    print("Categoria Infantil")
elif idade<=17:
    print("Categoria Juvenil")
elif idade<=39:
    print("Categoria Adulto")
elif idade<=130:
    print("Categoria Senior")
elif idade>=130:
    print("Idade inválida!!!")







