print(f"{' TABUADA ':=^40}\n")
n1 = int(input("Digite um número para ver a tabuada: "))
print(f"\n{' TABUADA DO ' + str(n1) :^40}\n")
for i in range(1, 11):
    print(f"{n1} x {i} = {n1 * i}")