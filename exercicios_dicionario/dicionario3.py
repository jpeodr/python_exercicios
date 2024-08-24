alunos = {
    "joao": [7.5, 7, 8],
    "vitoria": [8, 9, 10],
    "corina": [8.2, 9.2, 9.3],
    "juliana": [7.8, 9, 8],
    "roberto": [6, 7.8, 7],
    "andre": [10, 9.2, 8.6]
}

def media_cada_aluno(nome_aluno):
    notas_aluno = alunos[nome_aluno]
    media = sum(notas_aluno) / len(notas_aluno)
    return media
    
#corrigir

def situacao_aluno(nome_aluno):
    media = media_cada_aluno(nome_aluno)
    print(media)
    if media >= 7:
        print("Aprovado")
    elif media >= 5 and media < 7:
        print("Recuperação")
    else:
        print("Reprovado")

for i in alunos.keys():
    situacao_aluno(i)

def media_geral(dicionario_notas):
    soma_notas = 0
    quantidade_notas = 0
    for lista_nota in dicionario_notas.values():
        soma = sum(lista_nota)
        soma_notas = soma_notas + soma
        quantidade = len(lista_nota)
        quantidade_notas = quantidade_notas + quantidade
    media = soma_notas / quantidade_notas
    print(f"Média geral da turma: {media_geral:.2f}")

media_geral(alunos)