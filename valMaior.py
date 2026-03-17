email = input("Digite seu e-mail: ")
nota = float(input("Digite sua nota: "))

if nota > 8.5:
    print(f"Enviando convite para o e-mail: {email}")

else:
    print("Nota insuficiente")