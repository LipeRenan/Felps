#Estrutura de repetição while(continuação)
#Leia 5 números e mostre a soma de todos os valores informados

# cont = 1
# soma = 0 #acumulador
# while cont<=5:
#     num = float(input("Informe um valor:"))
#     soma += num
#     cont +=1
# print("Valor total é:",soma)
# Calcilar a soma do valores do intervalo (fechado) das variáveis a e b (280)
# a = 10
# b = 25
# ac = 0
# while a<=b:
#     print(a,end=" ")
#     ac += a
#     a += 1
# print("\nO resultado é:", ac)

#leia dois valores e mostre a soma do intervalo entre eles
# n1 = int(input("1° valor:"))
# n2 = int(input("2° valor:"))
# n3 = 0
# if n1<n2:
#     while n1<=n2:
#         n3 += n1
#         n1 += 1
#     print("\nO resultado é:", n3)
# elif n2<n1:
#     while n2<=n1:
#         n3 += n2
#         n2 += 1
#     print("O resultado é:",n3)
# else:
#     print("Os valores são iguais!!!")

#somar 5 valores positivos informados pelo usuário
# soma = 0 
# cont = 1

# while cont<=5:
#     valor = float(input("informae um valor positivo:"))
#     if valor<0:
#         continue
#     soma += valor
#     cont +=1
# print(f"O resultado da soma é {soma}")

#somar 5 valores negativo informados pelo usuário
# neg = 0 
# cont = 1

# while cont<=5:
#     valor = float(input("informae um valor negativo:"))
#     if valor>=0:
#         print("somente número negativo!!!")
#         break
#     neg += valor
#     cont +=1
# print(f"O resultado da soma é {neg}")

#leia 3 notas e mostre a média, caso seja digitado um valor negativo ou acima de 10
#será solicitado um novo valor

# soma = 0 
# cont = 1
# while cont<=3:
#     nota = float(input("informe a notas:"))
#     if nota<0 or nota>10:
#         continue
#     soma += nota
#     cont +=1
# print(f"O resultado da soma é {soma}")
# print(f"A média é {soma/3:.2f}")
