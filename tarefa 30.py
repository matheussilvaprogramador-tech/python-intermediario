#30.  O DESAFIO FINAL - A Taverna do Dragão:  Crie um super-sistema que une todos os temas! - Passo 1: Pede a  Senha Secreta  
# para entrar na Taverna. (Se errar, o programa acaba ali mesmo). - Passo 2: Se entrar, verifica a  Idade  
# (Se menor de  13, ganha suco de uva; se maior, ganha Poção Mágica). - Passo 3: O Taverneiro faz uma pergunta de 
#  Personalidade  para escolher qual item te vender. - Passo 4: Usa a  Calculadora de Mesada  para ver se você tem ouro
#  suficiente para comprar o item sorteado no Passo 3. 
senha = input("Digite a senha secreta para entrar na Taverna: ")

if senha == "dragao":

    print("Bem-vindo a Taverna do Dragão")

    idade = int(input("Digite sua idade: "))

    if idade < 13:
        print("Você ganhou um suco de uva!")
    else:
        print("Você ganhou uma Poção Mágica!")

    personalidade = input("Você é corajoso ou inteligente? ")

    if personalidade == "corajoso":
        print("Você escolheu uma Espada de Ouro!")
        preco = 50
    else:
        print("Você escolheu um Livro Mágico!")
        preco = 30

    mesada = float(input("Quanto ouro você tem? "))

    if mesada >= preco:
        print("Você tem ouro suficiente para comprar seu item!")
        print(f"Seu troco será de {mesada - preco} moedas.")
    else:
        print("Você não tem ouro suficiente!")
        print(f"Faltam {preco - mesada} moedas.")

else:
    print("Senha incorreta! A entrada da Taverna foi bloqueada.")
    