#20.  A Cantina Inflacionada:  Crie um sistema onde o usuário informa o dinheiro que tem e escolhe Lanche (R$ 15), Suco (R$ 8) ou Combo (R$ 20). O sistema deve usar o elif  para identificar a escolha, verificar se o dinheiro dá para pagar, e liberar ou negar a venda. 
dinheiro = float(input("Digite o valor de dinheiro que voce tem:"))
print("escolha o intem que deseja comprar:")
print("1 - lanche - R$ 15")
print("2 - suco - R$ 8")
print("3 - combo - R$ 20")
escolha = int(input("Digite o número do item que deseja comprar:"))

if escolha == 1:
    if dinheiro >= 15:
        print("Compra aprovada!")
    else:
        print("Dinheiro insuficiente.")
elif escolha == 2:
    if dinheiro >= 8:
        print("Compra aprovada!")
    else:
        print("Dinheiro insuficiente.")
elif escolha == 3:
    if dinheiro >= 20:
        print("Compra aprovada!")
    else:
        print("Dinheiro insuficiente.")
else:
    print("Escolha inválida.")