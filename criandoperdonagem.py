nome = input("Qual o nome do seu personagem: ")
classe = input("Qual a classe do seu heroi(guerreiro, mago ou arqueiro): ")
arma = input("Qual sua arma favorita: ")
nivel = int(input("Qual o nivel do seu personagem: "))

#isolei o texto em 10 bits e as variaveis em mais 10 bits para poder alinhar
print(f"\nSeu personagem foi criado com exito!\n")
print(f"{'Nome:':<10} {nome:>10}")
print(f"{'Classe:':<10} {classe:>10}")
print(f"{'Arma:':<10} {arma:>10}")
print(f"{'Nível:':<10} {nivel:>10}")


