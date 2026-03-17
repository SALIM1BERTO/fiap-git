print("Vamos calcular!")

while True:

    oper = int(input("Escolha sua operação: \n"
                     "1 - Soma\n"
                     "2 - Subtração\n"
                     "3 - Multiplicação\n"
                     "4 - Divisão\n"
                     "> "))

    if oper not in (1, 2, 3, 4):
        print("Valor digitado invalido")

        exit()

    v1 = int(input("\nDigite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))

    if oper == 1:
        print(f"\nResultado: {v1} + {v2} = {v1 + v2}")

    elif oper == 2:
        print(f"\nResultado: {v1} - {v2} = {v1 - v2}")

    elif oper == 3:
        print(f"\nResultado: {v1} X {v2} = {v1 * v2}")

    elif oper == 4:
        print(f"\nResultado: {v1} -:- {v2} = {v1 / v2}")

    esco = input("\nQuer fazer outra conta? (s/n): ").lower()

    if esco == 'n':
        break

    print("\n" * 20)