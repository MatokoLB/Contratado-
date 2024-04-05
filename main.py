#usando dicionario
#  Desenvolver um projeto (usando dicionários) que vai gravar 
# a quantidade de currículos para aquela vaga () e quantas 
# pessoas têm as palavras-chave necessárias no currículo(candidatos).

#  Nosso código deve ficar pedindo para qual vaga a pessoa se inscreveu e o resumo de 
# cada participante em loop (só deve parar quando inserir o número 0 na pergunta da 
# vaga).

#  ⇨ O texto do resumo/minibio vai ser informado pelo usuário (como desafio extra você 
# pode tentar ler esse texto de arquivos txt em uma pasta e eliminar essa etapa de pedir 
# os textos em loop) e então vamos checar se temos as palavras-chave necessárias e 
# marcar como um candidato válido para a vaga

 
vagas ={"vaga1":{"palavraChave":"python"}}
candidatos ={"candidato1":{"miniBio":"ola eu sei python"},"candidato2":{"miniBio":"ola eu sei js e python"}}
num = 0



# while True:
#     num += 1
#     vaga = "vaga" 
#     palavrachave = input("digite a palavra chave da vaga: ").lower()
#     vagas.update({vaga + str(num):{"palavra-chave":palavrachave}})


#     x = input("deseja sair S/N? ").lower()
#     if x == "s":
#         break
#     print(vagas)


# while True:
#     num += 1
#     candidato = "candidato" 
#     minibio = input("digite a minibio: ").lower()
#     candidatos.update({candidato + str(num): {"minibio": minibio}})


#     x = input("deseja sair S/N? ").lower()
#     if x == "s":
#         break
#     print(candidatos)


def aplicarVagaCandidato():
    x = input("digite a vaga: ")
    vaga = "vaga" + x

    palavraChave = vagas[vaga]["palavraChave"]
    
    quantidaCurriculo = 0
    aplicarmVaga = []
    for candidato in candidatos:
        curriculo = candidatos[candidato]["miniBio"]

        print(candidato) 
        for x in palavraChave:

            if x in curriculo:
                print(candidato,curriculo,"ok")
                aplicarmVaga.append(candidato)
                quantidaCurriculo
                break
            else:
                print(candidato,curriculo,"off")
                break


    print(len(candidatos))      
                

aplicarVagaCandidato()

