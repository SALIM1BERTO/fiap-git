rm = input("Por favor, digite seu RM: ")
idade = int(input("Por favor, digite sua idade: "))

if idade >= 18:
    print(f"\n\nSua participação foi autorizada, aluno de RM {rm}"
          f"\nMais instruçoes serão enviadas ao seu e-mail cadastrado na FIAP!")
else:
    print(f"\n\nVocê não tem autorização para participar por causa de sua idade")

    aut = input("\nVocê possui autorização dos responsaveis para participar? (s/n)\n>").lower()

    if aut not in ('s', 'n'):
        print("Erro, valor incerido invalido, tente novamente\n")
        exit()

    if aut == 's':
        print(f"\nSua participação foi autorizada, aluno RM {rm}"
              f"\nMais instruçoes serão enviadas ao seu e-mail cadastrado na FIAP!")

    else:
        print("Você não possui autorização")
