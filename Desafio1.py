
print("---------------------------------")
nome = (input("Digite o seu nome: "))
nivel = float(input("Quanto XP vc tem? "))
print("---------------------------------")


if nivel <= 1000:
    print(("O Herói de nome ") + nome + (" está no nível de Ferro "))

elif nivel >=1001 and nivel <= 2000:
    print(("O Herói de nome ")+ nome + (" está no nível de Bronze "))

elif nivel >= 2001 and nivel <= 5000:
    print(("O Herói de nome ")+ nome +(" está no nível de Prata "))

elif nivel >= 5001 and nivel <= 7000:
    print(("O Herói de nome ")+ nome +(" está no nível de Ouro "))

elif nivel >= 7001 and nivel <= 8000:
    print(("O Herói de nome ")+ nome +(" está no nível de Platina "))

elif nivel >= 8001 and nivel <= 9000:
    print(("O Herói de nome ")+ nome +(" está no nível de Ascendente "))

elif nivel >= 9001 and nivel <= 10000:
    print(("O Herói de nome ")+ nome +(" está no nível de Imortal "))

else:
    print(("O Herói de nome ")+ nome +(" está no nível de Radiante "))
