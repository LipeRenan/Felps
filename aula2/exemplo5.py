#leia o valor de um produto, caso o valor seja menor do que 100 mostre a seguinte mensagem
#"você recebeu 5% de desconto", caso contrário 
#"você recebeu 10% de desconto"

produto = float(input("informne o valor do prouduto:"))

if produto<=0:
    print("valor inválida!!!")
else:
    if produto<100:
        print("você recebeu 5% de desconto")
    else:
        print("você recebeu 10% de desconto")

    