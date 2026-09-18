tipo_imovel = input("Digite o tipo do imóvel (comercial, casa ou apartamento): ")
consumo = float(input("Digite o consumo mensal de água em m³: "))

if tipo_imovel == "comercial":
    print("Consumo comercial controlado - plano corporativo.")

elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico - excelente controle de água!")

elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    print("Consumo moderado - dentro do padrão residencial.")

else:
    print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")