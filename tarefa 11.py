#11.  O Guardiao Simples:  Crie um programa que pergunte "Qual a palavra magica?". Se a resposta for "Abre-te Sesamo", imprima "A caverna se abriu!". Senao, imprima "A caverna continua fechada.".
palavra = input("Digite a palavra mágica: ").lower()

if palavra == "abre te sesamo":
    print("A caverna se abriu!")
else:
    print("A caverna continua fechada.")

