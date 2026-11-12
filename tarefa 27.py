#27.  O Sistema Escolar (Calculadora de Notas):  Peça as notas de duas provas. Calcule a 
# média. Se a média for  >= 7 , Aprovado. Se for  >= 5  e  < 7 , Recuperação. Se for  < 5 , Reprovado.
#  Mostre a média e o veredito. 
nota_prova1 = int(input("Digite a primeira nota?:"))
nota_prova2 = int(input("digite a segunda nota ?:"))
media = (nota_prova1 + nota_prova2)/2
if media >=7:
    print(f"Parabens voce foi aprovado sua media foi : {media}")
elif media >= 5 and 7:
    print(f"Voce ficou em recuperação sua media foi: {media}")

elif media >= 5:
    print(f"Você ficou em recuperação sua media foi: {media}")


