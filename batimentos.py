idade = int(input("Insira sua idade: "))
bat = int(input("Insira sua frequencia cardiaca em BPM: "))

if idade <= 2:
    if 120 <= bat <= 140:
        print("Esta na faixa adequada")

    elif bat < 120:
        print("Esta abaixo da faixa adequada")

    elif bat > 140:
        print("Esta acima da faixa adequada")

if idade >= 8 and idade <= 17:
    if bat >= 80 and bat <= 100:
        print("Esta na faixa adequada")

    elif bat < 80:
        print("Esta abaixo da faixa adequada")

    elif bat > 100:
        print("Esta acima da faixa adequada")

if idade >= 18 and idade <= 59:
    if bat >= 70 and bat <= 80:
        print("Esta na faixa adequada")

    elif bat < 70:
        print("Esta abaixo da faixa adequada")

    elif bat > 80:
        print("Esta acima da faixa adequada")

if idade >= 60:
    if bat >= 50 and bat <= 60:
        print("Esta na faixa adequada")

    elif bat < 50:
        print("Esta abaixo da faixa adequada")

    elif bat > 60:
        print("Esta acima da faixa adequada")