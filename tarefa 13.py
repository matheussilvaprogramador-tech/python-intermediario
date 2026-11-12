#13.  Segurança Dupla (If Aninhado):  Crie um sistema bancário. Primeiro, ele pede a senha de letras. Se acertar, ele pede o PIN de 4 números. Só imprima "Acesso ao Cofre Liberado" se ele acertar as duas coisas (uma dentro da outra). 
senha = input("digite a senha de letras:")
if senha == "senha123":
    pin = input("digite o pin de 4 numeros:")
    if pin == "1234":
        print("Acesso ao Cofre Liberado")
else:
    print("Acesso negado")
