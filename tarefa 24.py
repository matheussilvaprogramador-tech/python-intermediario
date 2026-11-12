#24.  O Termômetro de Humor:  Pergunte ao usuário uma cor (Azul, Amarelo, Vermelho). 
# O sistema deve responder como ele está se sentindo usando  elif  (Ex: Azul = Calmo, Vermelho = Zangado). 
cor = input("escolha uma cor entre azul, amarelo, vermelho:")
if cor == "azul":
    print("Calmo")
elif cor == "amarelo":
    print("triste")
elif cor == "vermelho":
    print("zangado")
else:
    print("digite uma opçao valida ")
