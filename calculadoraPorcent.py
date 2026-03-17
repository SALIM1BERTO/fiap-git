print("Vamos calcular porcentagem!")

escolha = int(input("Digite:\n"
                "1 para saber a porcentagem\n"
                "2 para saber um desconto\n"
                "3 para saber um acrecimo\n"
                ">"))

if escolha not in (1, 2, 3):
    print("Opção invalida")
    exit()

por = float(input("Digite a porcentagem: "))
valor = float(input("\nDigite o valor: "))

porc = por / 100 * valor

if escolha == 1:
    print(f"\nA porcentagem de {valor} é {porc}")

elif escolha == 2:
    print(f"O valor de {valor} com deseconto de {por}% fica: {valor - porc}")

elif escolha == 3:
    print(f"O valor de {valor} com acrecimo de {por}% fica: {valor + porc}")
