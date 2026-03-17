print("Vamos classificar a idade da pessoa")

idade = int(input("\nDigite a idade da pessoa: "))

if idade < 0:
    print("Você não nasceu ainda bobo")

elif idade == 0 or idade <= 12:
    print("Você é criança")

elif idade <= 17:
    print("Você é adolecente")

elif idade <= 59:
    print("Você é adulto")

elif idade <= 100:
    print("Você é idoso")

else:
    print("Provavelmente morreu")
