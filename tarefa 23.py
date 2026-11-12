#23.  Seletor de Classes RPG:  Faça duas perguntas. 1: "Prefere atacar de longe (1) ou de perto (2)?". Dentro do primeiro  if  (longe), pergunte "Magia (A) ou Arco (B)?" para definir Mago ou Arqueiro. Dentro do  else  (perto), pergunte "Espada (A) ou Adagas (B)?" para definir Guerreiro ou Assassino. (Lógica de If aninhado).
distancia = input("Prefere atacar de longe (1) ou de perto (2)? ")

if distancia == "1":
    arma = input("Magia (A) ou Arco (B)? ")

    if arma == "A":
        print("Mago")
    else:
        print("Arqueiro")

else:
    arma = input("Espada (A) ou Adagas (B)? ")

    if arma == "A":
        print("Guerreiro")
    else:
        print("Assassino")
