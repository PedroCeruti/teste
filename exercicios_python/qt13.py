m2 = float(input("Digite o tamanho da área a ser pintada: "))

l = m2/3
la = l/18
if(l >= 18):
  v = la * 80
l = int(l)
print(f"Vão ser necessarias {la} latas")
print(f"Valor total: R${v:.2f}")