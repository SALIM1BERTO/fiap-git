comp = float(input("Valor da compra: "))
cupom1 = 'NIVER10'
cupom2 = 'NIVER20'

ins_cup = input("Cupom: ")

    if ins_cup == cupom1:
        comp = comp * 0.90
        print(f"Você recebeu um desconto de 10%\n"
              f"Valor da compra: R${comp:.2f}")

    elif ins_cup == cupom2:
        comp = comp * 0.80
        print(f"Você recebeu um desconto de 20%\n"
              f"Valor da compra: R${comp:.2f}")

    else:
        print(f"Cupom invalido\n"
              f"O valor final da compra é R${comp:.2f}")