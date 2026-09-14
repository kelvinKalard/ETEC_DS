valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra < 200:
    desconto = valor_compra * 0.05
elif valor_compra < 300:
    desconto = valor_compra * 0.10
else:
    desconto = valor_compra * 0.15

valor_final = valor_compra - desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")