#19.  Caixa Eletrônico da Mesada:  O pai deu a mesada, mas perguntou: "Você tirou nota A em matemática?". Se a resposta for "sim", a mesada recebe um bônus de 20 moedas. Se for "não", recebe apenas o valor normal. Imprima o total final. 
mesada = float(input("digite o valor da mesada:"))
nota = input("voce tirou nota A em matematica? (sim/nao):")
if nota.lower() == "sim":
    mesada += 20
    print(f"voce recebeu um bonuus de 20 moedas, sua mesada final e de {mesada} moedas")
else:
    print(f" voce nao recebeu bonus, sua mesada final e de {mesada} moedas")
    