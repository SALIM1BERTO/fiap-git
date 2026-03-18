import os
os.system("cls")

print("Vamos calcular porcentagem!")

# escolha = int(input("Digite:\n"
#                 "1 para saber a porcentagem\n"
#                 "2 para saber um desconto\n"
#                 "3 para saber um acrecimo\n"
#                 ">"))
#
# if escolha not in (1, 2, 3):
#     print("Opção invalida")
#     exit()

print(f"""
1 - saber porcentagem
2 - saber um desconto
3 - saber um acrecimo
""")

escolha = int(input("Escolha uma opção: "))

por = float(input("Digite a porcentagem: "))
valor = float(input("\nDigite o valor: "))

porc = por / 100 * valor

match escolha:
    case 1:
        print(f"\n{por}% de {valor} é {porc}")

    case 2:
        print(f"O valor de {valor} com deseconto de {por}% fica: {valor - porc}")

    case 3:
        print(f"O valor de {valor} com acrecimo de {por}% fica: {valor + porc}")
