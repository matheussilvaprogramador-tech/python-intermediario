#Tema C: O Chapéu Seletor e Testes de Personalidade 
# #21.  O Chapéu Seletor Clássico:  Faça a pergunta: "Você prefere: 1-Livros, 2-Esportes, 3-Natureza, 4-Pegadinhas". Use  if/elif/else  para sortear o aluno em uma das 4 casas da escola de magia (ex: Corvinal, Grifinória, Lufa-Lufa, Sonserina). 

preferencia = int(input(
    "Você prefere: 1-Livros, 2-Esportes, 3-Natureza ou 4-Pegadinhas? "
))

if preferencia == 1:
    print("Você foi sorteado para a casa Corvinal!")
elif preferencia == 2:
    print("Você foi sorteado para a casa Grifinória!")
elif preferencia == 3:
    print("Você foi sorteado para a casa Lufa-Lufa!")
elif preferencia == 4:
    print("Você foi sorteado para a casa Sonserina!")
else:
    print("Opção inválida. Digite um número de 1 a 4.")
