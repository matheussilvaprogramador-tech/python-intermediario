#28.  A Máquina do Tempo:  Peça para o usuário digitar um ano.  if  ano for menor que 1500: "Você encontrou 
# dinossauros ou cavaleiros!".  elif  ano menor que 2000: "Você está no século passado!".  
# elif  ano igual a 2026: "Você está no presente!".  else : "Você está no futuro com os carros voadores!". 
ano = int(input("Digite um Ano?:"))
if ano <= 1500:
    print("voce encontrou dinossauros ou cavaleiros!")
elif ano <=2000:
    print("Voce esta no seculo passado!")
elif ano >= 2001 and ano <= 2026:
    print("Voce esta no presente!")
else:
    print("Voce esta no futuro com os carros voadores!")
