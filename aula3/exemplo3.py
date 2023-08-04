#Aplicar operadores lógicos com if
#Leia a qtd de faltas de um aluno e sua média final

faltas = int(input("Informe a quatidade de faltas:"))
media = float(input("Informe a media final:"))
#Condições de reprovação:
#qtd de faltas maior do que 8 ou media menor do que 7
#analizar condição do aluno somente se o valor das faltas for
#maior ou igual a zero
if faltas <0:
    print("valor inválid0!!!")
    if faltas>8 and media<7:
        print("Aluno reprovado")
        if faltas>8:
            print("aluno reprovadopor faltas")
        if media<7:
            print("aluno reprovado por média")
else:
    print("aprovado")


