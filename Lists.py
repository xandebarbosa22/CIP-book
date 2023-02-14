# 3.1 – Nomes: Armazene os nomes de alguns de seus amigos em uma lista
# chamada names. Exiba o nome de cada pessoa acessando cada elemento da
# lista, um de cada vez.

names = ["Ray", "Vini", "Livia", "Vivian"]
print("\nHello my friends: " + names[0] + ",",
      names[1] + ",", names[2] + ",", names[3] + "! How are you doing?")


# 3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
# simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas.
# O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve
# estar personalizada com o nome da pessoa.

names = ["Ray", "Vini", "Lívia", "Vivian"]
print("")
for name in names:
    print("Hello, " + name + "! How are you doing?")


# 3.3 – Sua própria lista: Pense em seu meio de transporte preferido, como
# motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
# lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter
# uma moto Honda”.


motorcycle = ["Honda", "Yahama", "Suzuki", "BMW", "Harley-Davidson"]
print("\nI would like to have a " + motorcycle[2] + " motorcycle.")
