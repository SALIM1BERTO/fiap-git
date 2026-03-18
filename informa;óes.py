nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))
comida = input("Qual sua comida favorita: ")

print("Juntando tudo fica\n")

print(f"{"Seu nome é:":<30}{nome:>15}")
print(f"{'Sua idade é:':<30}{idade:>15}")
print(f"{'Sua comida favorita é:':<30}{comida:>15}")