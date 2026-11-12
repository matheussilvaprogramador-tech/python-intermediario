#14.  O Clube dos Rebeldes (Validação Inversa):  O clube secreto aceita todo mundo, exceto  quem se chamar "Voldemort". Pergunte o nome e use o operador de diferença ( != ) para barrar o vilão e liberar os outros. 
nome = input(" digite seu nome:")
if nome != "voldemort":
    print(f"Bem vindo ao clube secreto, {nome}!")
else:
    print("Acesso negado, voce e do mal")
