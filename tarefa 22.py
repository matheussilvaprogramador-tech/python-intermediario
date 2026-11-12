#22.  O Bug do Chapéu:  Melhore o exercício anterior. Adicione um  else  poderoso no final para o caso 
# de o usuário digitar "5" ou qualquer letra errada, fazendo o chapéu responder: "Hmm, escolha inválida. 
# O Chapéu está confuso!".
preferencia = int(input(
    "voce prefere: 1- livros, 2- esportes, 3- natureza, 4- pegadinhas?:"
)) 
if preferencia == 1:
    print("voce foi sorteado para a casa corvinal")
elif preferencia == 2:
    print("voce foi sorteado para a casa grifinoria")
elif preferencia == 3:
    print("voce foi sorteado para a casa lufa-lufa")
elif preferencia == 4:
    print("voce foi sorteado para a casa sonserina")
else:
    print("humm, escolha invalida. o chapeu esta confuso!")
