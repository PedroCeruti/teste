#Vide "Atividades.txt"
nota = float(input("Digite uma nota: "))
while(nota < 0) or (nota > 10):
  nota = float(input("Digite uma nota: "))
else:
  print("Ok")