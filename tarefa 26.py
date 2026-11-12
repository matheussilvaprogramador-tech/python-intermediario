#Tema D: Cenários Complexos e Desafios do Chefão Misturando Conceitos 
# 26.  O Radar de Velocidade:  Pergunte a velocidade do carro (número). Se for menor ou igual a 80, "Siga em paz".
#  Se for entre 81 e 100, "Multa leve de 50 moedas". Se for maior que 100, "Multa gravíssima de 200 moedas e carro apreendido!". 
velocidade = int(input("Digite a velocidade do carro?:"))
if velocidade <= 80:
    print("Siga em paz")
elif velocidade <=100:
    print("muita leve de 50 moedas")
else:
    print("multa gravissima de 200 moedas")

