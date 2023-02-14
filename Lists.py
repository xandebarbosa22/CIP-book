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


# 3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o
# jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
# que você gostaria de convidar para jantar. Em seguida, utilize sua lista para
# exibir uma mensagem para cada pessoa, convidando-a para jantar.


dinner = ["Ray", "Quitéria", "Valdir", "Vini"]
for person in dinner:
    print("\nWould you like to dinner with me, " + person + "?")


# 3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
# convidados não poderá comparecer ao jantar, portanto será necessário enviar
# um novo conjunto de convites. Você deverá pensar em outra pessoa para
# convidar.

#   • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
#   no final de seu programa, especificando o nome do convidado que não
#   poderá comparecer.
#   • Modifique sua lista, substituindo o nome do convidado que não poderá
#   comparecer pelo nome da nova pessoa que você está convidando.
#   • Exiba um segundo conjunto de mensagens com o convite, uma para cada
#   pessoa que continua presente em sua lista.


dinner = ["Ray", "Quitéria", "Valdir", "Vini", "Lívia"]
for person in dinner:
    print("\nWould you like to dinner with me, " + person + "?")

print("\nUnfortunately, " + dinner[-1] +
      " will not be able to attend the dinner.")

dinner[-1] = "Apolo"
for people in dinner:
    print("\nWould you like to dinner with me, " + people + "?")


# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
# portanto agora tem mais espaço disponível. Pense em mais três convidados
# para o jantar.

#   • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
#   uma instrução print no final de seu programa informando às pessoas que
#   você encontrou uma mesa de jantar maior.

#   • Utilize insert() para adicionar um novo convidado no início de sua lista.
#   • Utilize insert() para adicionar um novo convidado no meio de sua lista.
#   • Utilize append() para adicionar um novo convidado no final de sua lista.

#   • Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
#   que está em sua lista.


dinner = ["Ray", "Quitéria", "Valdir", "Vini", "Lívia"]
for person in dinner:
    print("\nWould you like to dinner with me, " + person + "?")

print("\nUnfortunately, " + dinner[-1] +
      " will not be able to attend the dinner.")

dinner[-1] = "Apolo"
for person in dinner:
    print("\nWould you like to dinner with me, " + person + "?")

print("\nWe found a bigger dinning table!")

dinner.insert(0, "Milly")
dinner.insert(3, "Malu")
dinner.append("Luke")

for person in dinner:
    print("\nWould you like to dinner with me, " + person + "?")


# 3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
# mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
# dois convidados.

#   • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
#   mostre uma mensagem informando que você pode convidar apenas duas
#   pessoas para o jantar.

#   • Utilize pop() para remover os convidados de sua lista, um de cada vez, até
#   que apenas dois nomes permaneçam em sua lista. Sempre que remover um
#   nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
#   saiba que você sente muito por não poder convidá-la para o jantar.

#   • Apresente uma mensagem para cada uma das duas pessoas que continuam
#   na lista, permitindo que elas saibam que ainda estão convidadas.

#   • Utilize del para remover os dois últimos nomes de sua lista, de modo que você
#   tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
#   uma lista vazia no final de seu programa.


dinner = ["Ray", "Quitéria", "Valdir", "Vini", "Lívia"]
for person in dinner:
    print("Would you like to dinner with me, " + person + "?")

print("\nUnfortunately, " + dinner[-1] +
      " will not be able to attend the dinner.")

dinner[-1] = "Apolo"
for person in dinner:
    print("Would you like to dinner with me, " + person + "?")

print("\nWe found a bigger dinning table!")

dinner.insert(0, "Milly")
dinner.insert(3, "Malu")
dinner.append("Luke")

for person in dinner:
    print("Would you like to dinner with me, " + person + "?")

print("\nDue to an internal issue, we can only invite 2 people for dinner.")

dinner_popped_people = []
dinner_popped_people.append(dinner.pop(1))
dinner_popped_people.append(dinner.pop(1))
dinner_popped_people.append(dinner.pop(2))
dinner_popped_people.append(dinner.pop(2))
dinner_popped_people.append(dinner.pop(2))
dinner_popped_people.append(dinner.pop(2))

for people in dinner_popped_people:
    print("I'm sorry for the inconvenience, " +
          people + "... This was totally unforeseen!")

del dinner[0]
del dinner[0]

print(dinner)
