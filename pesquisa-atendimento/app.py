excelente = 0
ruim = 0

for i in range(50):
    print("Entrevistado número:", i + 1)

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opinião sobre o atendimento: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

    print()

print("Resultado da pesquisa")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)