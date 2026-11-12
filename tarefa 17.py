#17.  A Feira de Poções Múltiplos Produtos:  Mostre um menu com 3 poções e preços diferentes. Peça para o usuário digitar 1, 2 ou 3. Use  if/elif/else  para calcular o valor da compra baseado na escolha.
print("bem vindo a feira de poçoes")
print("1 - poçao de cura - R$ 10")
print("2 - poçao de força - R$ 15")
print("3 - porçao de invisibilidade - R$ 20")
escolha = int(input("digite o numero da poçao que deseja comprar:"))
if escolha == 1:
    print("voce comprou a poçao de cura por R$ 10")
elif escolha == 2:
    print("voce comprou a porçao de força por R$ 15")
elif escolha == 3:
    print("voce comprou a porçao de invisibilidade por R$ 20")
else:
    print("opçao invalida, por favor digite 1, 2, ou 3 ")
    