#15.  A Senha Sensível (Caps Lock):  Peça a senha secreta. Adicione um  elif  para testar se o usuário digitou a senha certa, mas toda em MAIÚSCULAS, e imprima um aviso: "Quase! Mas você gritou a senha (Caps Lock). Tente minúsculas." 
senha = input("digite a senha secreta:")
if senha == "senha123":
    print("Acesso permitido")
elif senha == "senha123".upper():
    print("Quase! mas voce gritou a senha (caps lock). tente minusculas.")
    