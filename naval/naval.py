import sys

# Lista com as letras
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P']

# Lista das colunas
numeros = [str(i) for i in range(1, 16)]

#tabuleiro
tabuleiro = [letra + numero for letra in letras for numero in numeros]

#-------------------------------------- LEITURA JOGADOR 01 ----------------------------------------#
#PEÇA E POSICIONAMENTO
peca_posicao = []

J1 = []

ataque = []

sobreposicao1 = []

def escreverTxt(resultado):
    # Coletando as variáveis que você deseja escrever
linha1 = "Esta é a primeira linha do arquivo."
linha2 = "Esta é a segunda linha do arquivo."

# Abrindo o arquivo em modo de escrita
nome_do_arquivo = "resultado.txt"
with open(nome_do_arquivo, "w") as arquivo:
    # Escrevendo as duas linhas no arquivo, separadas por quebra de linha
    arquivo.write(linha1 + '\n' + linha2)

    

def camposPosicao(indice, frota, alvo, jogador):

    #VERIFICANDO SE FOI INSERIDO A QUANTIDADE CORRETA DE TORPEDOS
    if(len(frota) != 22 or len(alvo) !=25):
        print(jogador, 'ERROR_NR_PARTS_VALIDATION')
        sys.exit()

    embarcacao = ''
    
    # COLETANDO ID DA PEÇA
    peca = int(indice[0])

    #CASO SEJA UM SUBMRINO
    if peca == 3:
        # REMOÇÃO DO ID DA PEÇA PARA TRATAMENTO
        indice = indice[1:]

        validaPosicionamento(indice, jogador) # SIM (CONTINUA) / NÃO (PROGRAMA AUTO FINALIZA)

        # EVITAR SOBREPOSIÇÃO DE SUBMARINOS
        if indice in sobreposicao1:
             print(jogador, 'ERROR_OVERWRITE_PIECES_VALIDATION')
             sys.exit()
        else:
            sobreposicao1.append(indice)
            embarcacao = indice
            J1.append(embarcacao)
            return

    # CASO NÃO SEJA UM SUBMARINO, CONTINUA DEMAIS VALIDAÇÕES
    # REMOÇÃO DO ID DA PEÇA PARA TRATAMENTO
    indice = indice[1:]

    # CAPTURAR DIRECÃO (ULTIMO CARACTER)
    direcao = indice[-1]

    # REMOVER DIREÇÃO DO INDICE PARA TRATAR NO TABULEIRO
    indice = indice[:-1]

    cont = 0

    indice_Inicial = 0

    indice = indice.upper()

    # ESTE INDICE EXISTE NO TABULEIRO E NÃO FOI USADO...
    if indice not in J1:
        indice_Inicial = tabuleiro.index(indice)

        # verificação de direcao para contagem e posicionamento da peça no tabuleiro
        direcao = direcao.upper()

        # PEÇA NA VERTICAL 
        if direcao == 'V':
            
            # será realizado uma contagem de intervalo para capturar os campos a serem 
            # Ocupados pela peça a partir do index fornecido pela peça

            while cont < pecaTamanho(peca):
                embarcacao += tabuleiro[indice_Inicial + (15 * cont)] + '|' # A CADA 15
                 # INDICE EXISTE NO TABULEIRO ?
                validaPosicionamento(tabuleiro[indice_Inicial + (15 * cont)], jogador) # SIM (CONTINUA) / NÃO (PROGRAMA AUTO FINALIZA)
                if tabuleiro[indice_Inicial + (15 * cont)] not in sobreposicao1:
                    sobreposicao1.append(tabuleiro[indice_Inicial + (15 * cont)])
                else:
                    print(jogador, 'ERROR_OVERWRITE_PIECES_VALIDATION')
                    sys.exit()

                cont += 1

            J1.append(embarcacao)
        
        # PEÇA HORIZONTAL
        else:
            while cont < pecaTamanho(peca):
                embarcacao += tabuleiro[indice_Inicial + cont] + '|' # DE 1 EM 1
                validaPosicionamento(tabuleiro[indice_Inicial + cont], jogador) # SIM (CONTINUA) / NÃO (PROGRAMA AUTO FINALIZA)
                if tabuleiro[indice_Inicial + cont] not in sobreposicao1:
                    sobreposicao1.append(tabuleiro[indice_Inicial + cont])
                else:
                    print(jogador, 'ERROR_OVERWRITE_PIECES_VALIDATION')
                    sys.exit()

                cont += 1
        
            J1.append(embarcacao)
    
    # ESTE INDICE JÁ FOI UTILIZADO...
    else:
        print(jogador, 'ERROR_OVERWRITE_PIECES_VALIDATION')
        sys.exit()

# FUNÇÃO PARA VERIFICAR TAMANHO DA PEÇA
def pecaTamanho(peca):
    if peca == 1:
        return 4
    
    elif peca == 2:
        return 5
    
    elif peca == 3:
        return 1
    
    elif peca == 4:
        return 2

# FUNÇÃO PARA VERIFICAR SE EXISTE NO TABULEIRO
def validaPosicionamento(indice, jogador):
    if indice not in tabuleiro:
        print(jogador, 'ERROR_POSITION_NONEXISTENT_VALIDATION')
        sys.exit()

with open('jogador1.txt', 'r') as arquivo:
    linha = arquivo.readline()

    # VARIAVEL AUXILIAR PARA DIVIDIR ID_PEÇA E PEÇA_POSIÇÃO
    reparticao_jogada = ''

    # COLETAR A ID DA PEÇA
    id_peca = ''

    while linha:
        reparticao_jogada = linha.split(';')

        # VERIFICO SE É UM NÚMERO E CONVERTO PARA COLETAR A ID DA PECA
        if reparticao_jogada[0].isdigit():
            id_peca = reparticao_jogada[0]

            # REMOVENDO QUEBRAS DE LINHAS
            reparticao_jogada[1] = reparticao_jogada[1].replace("\n", "")

            # FORMANDO OS INDICES DAS EMBARCAÇÕES EX: (A15V)
            for x in reparticao_jogada[1].split('|'):
                peca_posicao.append(id_peca + x)
        
        # COLETANDO OS INDICES PARA ATAQUE
        if reparticao_jogada[0] == 'T':
            ataque = reparticao_jogada[1].split('|')

        linha = arquivo.readline()

for camp in peca_posicao:
    camposPosicao(camp, peca_posicao, ataque, 'J1')

#-------------------------------------------------------- JOGADOR 2 -----------------------------------------------------------------#

J2 = []

#PEÇA E POSICIONAMENTO
peca_posicao2 = []

ataque2 = []

sobreposicao2 = []

with open('jogador2.txt', 'r') as arquivo:
    linha = arquivo.readline()

    # VARIAVEL AUXILIAR PARA DIVIDIR ID_PEÇA E PEÇA_POSIÇÃO
    reparticao_jogada = ''

    # COLETAR A ID DA PEÇA
    id_peca = ''

    while linha:
        reparticao_jogada = linha.split(';')

        # VERIFICO SE É UM NÚMERO E CONVERTO PARA COLETAR A ID DA PECA
        if reparticao_jogada[0].isdigit():
            id_peca = reparticao_jogada[0]

            # REMOVENDO QUEBRAS DE LINHAS
            reparticao_jogada[1] = reparticao_jogada[1].replace("\n", "")

            # FORMANDO OS INDICES DAS EMBARCAÇÕES EX: (A15V)
            for x in reparticao_jogada[1].split('|'):
                peca_posicao2.append(id_peca + x)
        
        # COLETANDO OS INDICES PARA ATAQUE
        if reparticao_jogada[0] == 'T':
            ataque2 = reparticao_jogada[1].split('|')

        linha = arquivo.readline()


def camposPosicao2(indice, frota, alvo, jogador):

    #VERIFICANDO SE FOI INSERIDO A QUANTIDADE CORRETA DE TORPEDOS
    if(len(frota) != 22 or len(alvo) !=25):
        print(jogador, 'ERROR_NR_PARTS_VALIDATION')
        sys.exit()

    embarcacao = ''
    
    # COLETANDO ID DA PEÇA
    peca = int(indice[0])

    #CASO SEJA UM SUBMRINO
    if peca == 3:
        # REMOÇÃO DO ID DA PEÇA PARA TRATAMENTO
        indice = indice[1:]

        validaPosicionamento(indice, jogador) # SIM (CONTINUA) / NÃO (PROGRAMA AUTO FINALIZA)

        # EVITAR SOBREPOSIÇÃO DE SUBMARINOS
        if indice in sobreposicao2:
             print(jogador, 'ERROR_OVERWRITE_PIECES_VALIDATION')
             sys.exit()
        else:
            sobreposicao2.append(indice)
            embarcacao = indice
            J2.append(embarcacao)
            return

    # CASO NÃO SEJA UM SUBMARINO, CONTINUA DEMAIS VALIDAÇÕES
    # REMOÇÃO DO ID DA PEÇA PARA TRATAMENTO
    indice = indice[1:]

    # CAPTURAR DIRECÃO (ULTIMO CARACTER)
    direcao = indice[-1]

    # REMOVER DIREÇÃO DO INDICE PARA TRATAR NO TABULEIRO
    indice = indice[:-1]

    cont = 0

    indice_Inicial = 0

    indice = indice.upper()

    # ESTE INDICE EXISTE NO TABULEIRO E NÃO FOI USADO...
    if indice not in J2:
        indice_Inicial = tabuleiro.index(indice)

        # verificação de direcao para contagem e posicionamento da peça no tabuleiro
        direcao = direcao.upper()

        # PEÇA NA VERTICAL 
        if direcao == 'V':
            
            # será realizado uma contagem de intervalo para capturar os campos a serem 
            # Ocupados pela peça a partir do index fornecido pela peça

            while cont < pecaTamanho(peca):
                embarcacao += tabuleiro[indice_Inicial + (15 * cont)] + '|' # A CADA 15
                 # INDICE EXISTE NO TABULEIRO ?
                validaPosicionamento(tabuleiro[indice_Inicial + (15 * cont)], jogador) # SIM (CONTINUA) / NÃO (PROGRAMA AUTO FINALIZA)
                if tabuleiro[indice_Inicial + (15 * cont)] not in sobreposicao2:
                    sobreposicao2.append(tabuleiro[indice_Inicial + (15 * cont)])
                else:
                    print(jogador, 'ERROR_OVERWRITE_PIECES_VALIDATION')
                    sys.exit()

                cont += 1

            J2.append(embarcacao)
        
        # PEÇA HORIZONTAL
        else:
            while cont < pecaTamanho(peca):
                embarcacao += tabuleiro[indice_Inicial + cont] + '|' # DE 1 EM 1
                validaPosicionamento(tabuleiro[indice_Inicial + cont], jogador) # SIM (CONTINUA) / NÃO (PROGRAMA AUTO FINALIZA)
                if tabuleiro[indice_Inicial + cont] not in sobreposicao2:
                    sobreposicao2.append(tabuleiro[indice_Inicial + cont])
                else:
                    print(jogador, 'ERROR_OVERWRITE_PIECES_VALIDATION')
                    sys.exit()

                cont += 1
        
            J2.append(embarcacao)
    
    # ESTE INDICE JÁ FOI UTILIZADO...
    else:
        print(jogador, 'ERROR_OVERWRITE_PIECES_VALIDATION')
        sys.exit()

for camp in peca_posicao2:
    camposPosicao2(camp, peca_posicao2, ataque2, 'J2')

def atk(alvo, frota, jogador):
    embarcacao_atingida = []
    pontuacao = 0
    quantidade_embarcacao_atingida = 0
    navio = []
    subs = []
    parcial = ''
    atingidos = []

    for carga in frota: # --> [b2|b3|b4]
        if '|' in carga.strip():
            navio = carga.split('|') # --> [b1,b2,b3,b4]
            atingidos = []
            for complemento in navio: # --> [b1]
                if len(atingidos) + 1 == len(navio):
                    pontuacao += 2
                for fogo in alvo:

                    # INDICE EXISTE NO TABULEIRO ?
                    validaPosicionamento(fogo, jogador) # SIM (CONTINUA) / NÃO (PROGRAMA AUTO FINALIZA)

                    if fogo == complemento and fogo not in atingidos:
                        atingidos.append(complemento)
                        pontuacao += 3

                        #SE NAVIO AINDA NÃO ATINGIDO
                        if carga not in embarcacao_atingida:
                            embarcacao_atingida.append(carga)
        else:
            for fogo in alvo:
                if fogo == carga and fogo not in subs:
                    pontuacao += 5
                    subs.append(carga)
                    embarcacao_atingida.append(carga)

    return(f'{jogador}|{len(embarcacao_atingida)}|{22 - len(embarcacao_atingida)}|{pontuacao}')

resultado_J1 = atk(ataque, J1, 'J1').split('|')
resultado_J2 = atk(ataque2, J2, 'J2').split('|')

if (int(resultado_J1[3]) > int(resultado_J2[3])):
    print(f'{resultado_J1[0]} {resultado_J1[1]}AA {resultado_J1[2]}AE {resultado_J1[3]}PT')

elif (int(resultado_J1[3]) < int(resultado_J2[3])):
    print(f'{resultado_J2[0]} {resultado_J2[1]}AA {resultado_J2[2]}AE {resultado_J2[3]}PT')

else:
    print(f'{resultado_J1[0]} {resultado_J1[1]}AA {resultado_J1[2]}AE {resultado_J1[3]}PT')
    print(f'{resultado_J2[0]} {resultado_J2[1]}AA {resultado_J2[2]}AE {resultado_J2[3]}PT')
