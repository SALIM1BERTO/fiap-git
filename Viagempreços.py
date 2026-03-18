print("Bem vindo ao Viagemdeavião.com\n\n")
#categoria 
viagem = input("Selecione sua catergia de voo: \n" \
"1 - Economica\n" \
"2 - Executiva\n" \
"3 - Primeira Classe\n\n" \
"> ")

viaj = int(input("\nInsira a quantidade de viajantes: "))

valor = float(input("Insira o valor da sua viagem: "))

if int(viagem) == 1:
    if viaj == 2:
        print(f"\n\nvalor bruto: R${valor:.2f}")

        print(f"Seu desconto foi de: R${valor -(valor * 0.97):.2f}")        
        valor = valor * 0.97

        print(f"valor com desconto de 3%: R${valor:.2f}\n")
        print(f"O valor por pessoa fica: R${valor / viaj:.2f}\n\n")
        

    elif viaj == 3:
        print(f"\n\nvalor bruto: R${valor:.2f}")

        print(f"Seu desconto foi de: R${valor -(valor * 0.96):.2f}")        
        valor = valor * 0.96

        print(f"valor com desconto de 4%: R${valor:.2f}\n")
        print(f"O valor por pessoa fica: R${valor / viaj:.2f}\n\n")
        

    elif viaj >= 4:
        print(f"\n\nvalor bruto: R${valor:.2f}")

        print(f"Seu desconto foi de: R${valor -(valor * 0.95):.2f}")        
        valor = valor * 0.95

        print(f"valor com desconto de 5%: R${valor:.2f}\n")
        print(f"O valor por pessoa fica: R${valor / viaj:.2f}\n\n")

elif int(viagem) == 2:
    if viaj == 2:
        print(f"\n\nvalor bruto: R${valor:.2f}")

        print(f"Seu desconto foi de: R${valor -(valor * 0.95):.2f}")        
        valor = valor * 0.95

        print(f"valor com desconto de 5%: R${valor:.2f}\n")
        print(f"O valor por pessoa fica: R${valor / viaj:.2f}\n\n")
        

    elif viaj == 3:
        print(f"\n\nvalor bruto: R${valor:.2f}")

        print(f"Seu desconto foi de: R${valor -(valor * 0.93):.2f}")        
        valor = valor * 0.93

        print(f"valor com desconto de 7%: R${valor:.2f}\n")
        print(f"O valor por pessoa fica: R${valor / viaj:.2f}\n\n")
        

    elif viaj >= 4:
        print(f"\n\nvalor bruto: R${valor:.2f}")

        print(f"Seu desconto foi de: R${valor -(valor * 0.92):.2f}")        
        valor = valor * 0.92

        print(f"valor com desconto de 8%: R${valor:.2f}\n")
        print(f"O valor por pessoa fica: R${valor / viaj:.2f}\n\n")

elif int(viagem) == 3:
    if viaj == 2:
        print(f"\n\nvalor bruto: R${valor:.2f}\n")
        
        print(f"Seu desconto foi de: R${valor -(valor * 0.90):.2f}\n")        
        valor = valor * 0.90

        print(f"valor com desconto de 10%: R${valor:.2f}\n")
        print(f"O valor por pessoa fica: R${valor / viaj:.2f}\n\n")
        

    elif viaj == 3:
        print(f"\n\nvalor bruto: R${valor:.2f}")

        print(f"Seu desconto foi de: R${valor -(valor * 0.85):.2f}")      
        valor = valor * 0.85

        print(f"valor com desconto de 15%: R${valor:.2f}\n")
        print(f"O valor por pessoa fica: R${valor / viaj:.2f}\n\n")
        

    elif viaj >= 4:
        print(f"\n\nvalor bruto: R${valor:.2f}")

        print(f"Seu desconto foi de: R${valor -(valor * 0.80):.2f}")        
        valor = valor * 0.80

        print(f"valor com desconto de 20%: R${valor:.2f}\n")
        print(f"O valor por pessoa fica: R${valor / viaj:.2f}\n\n")        