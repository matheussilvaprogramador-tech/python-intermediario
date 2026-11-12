#12.  A Guilda de Robótica (Verificação de Idade):  Pergunte a idade do usuário. Se for maior ou igual a 14, diga "Bem-vindo à equipe avançada!". Senão, diga "Faltam X anos para você entrar na equipe avançada!" (O computador deve calcular e mostrar quantos anos faltam).
idade = int(input("digite sua idade: "))
if idade >= 14:
    print("Bem vindo á equipe avançada!")
else:
    print(f"faltam {14 - idade} anos para voçê entrar na equipe avançada!")
