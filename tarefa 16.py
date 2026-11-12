#Tema B: Calculadora de Mesada e Economia 
# #16.  O Jogo Novo:  Pergunte o valor da mesada guardada e o preço de um jogo que o aluno quer. Se o valor for suficiente, calcule e mostre o troco. Senão, diga exatamente quanto dinheiro falta.
mesada = float(input("digite o valor da mesada guardada:"))
preco_jogo = float(input("digite o preço do jogo que voce quer:"))
if mesada >= preco_jogo:
    troco = mesada - preco_jogo
    print(f"voce pode comprar o jogo e seu troco e de {troco}")
else:
    falta = preco_jogo - mesada
    print(f"voce nao pode comprar o jogo, falta {falta} reais")
