#25.  O Guru dos Animais:  Pergunte a idade do aluno  e se ele prefere gatos ou cachorros. 
# Crie 4 respostas possíveis combinando os dados (Ex: "Jovem e prefere gatos", "Adulto e prefere cachorros", etc). 
idade = int(input("Digite sua idade: "))
animal = input("Você prefere gatos ou cachorros?: ")

if idade < 18:
    if animal == "gatos":
        print("Jovem e prefere gatos")
    elif animal == "cachorros":
        print("Jovem e prefere cachorros")
    else:
        print("Digite uma opção válida")

else:
    if animal == "gatos":
        print("Adulto e prefere gatos")
    elif animal == "cachorros":
        print("Adulto e prefere cachorros")
    else:
        print("Digite uma opção válida")



