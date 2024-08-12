perguntas = [
    "Telefonou para a Vítma?",
    "Esteve no local do Crime?",
    "Mora perto da Vítma?",
    "Já trabalhou com a Vítma?",
    "Tem algum motivo para fazer o crime?"
]

respostas_positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta + " (responda sim ou não):").strip().lower()
    if resposta == 'sim':
        respostas_positivas +=1
if respostas_positivas == 2:
    classificacao = "Suspeito"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assasino"
    
else:
    classificacao = "inocente"
print(f"Classificação: {classificacao}")  