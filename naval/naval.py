import sys

# Lista com as letras
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

# Lista das colunas
numeros = [str(i) for i in range(1, 16)]

#tabuleiro
tabuleiro = [letra + numero for letra in letras for numero in numeros]



def camposPosicao(indice):

    embarcacao = ''

    # COLETANDO ID DA PEÇA
    peca = int(indice[0])

    #CASO SEJA UM SUBMRINO
    if peca == 3:
        # REMOÇÃO DO ID DA PEÇA PARA TRATAMENTO
        indice = indice[1:]

        validaPosicionamento(indice) # SIM (CONTINUA) / NÃO (PROGRAMA AUTO FINALIZA)

        # EVITAR SOBREPOSIÇÃO
        if indice in J1:
             print('ERROR_OVERWRITE_PIECES_VALIDATION')
             sys.exit()
        else:
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

    # INDICE EXISTE NO TABULEIRO ?
    validaPosicionamento(indice) # SIM (CONTINUA) / NÃO (PROGRAMA AUTO FINALIZA)

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
                cont += 1

            J1.append(embarcacao)
        
        # PEÇA HORIZONTAL
        else:
            while cont < pecaTamanho(peca):
                embarcacao += tabuleiro[indice_Inicial + cont] + '|' # DE 1 EM 1 
                cont += 1
        
            J1.append(embarcacao)
    
    # ESTE INDICE JÁ FOI UTILIZADO...
    else:
        print('ERROR_OVERWRITE_PIECES_VALIDATION')
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
def validaPosicionamento(indice):
    if indice not in tabuleiro:
        print('ERROR_POSITION_NONEXISTENT_VALIDATION')
        sys.exit()


#-------------------------------------- LEITURA JOGADOR 01 ----------------------------------------#
# Abre o arquivo para leitura

#PEÇA E POSICIONAMENTO
peca_posicao = []

J1 = []

ataque = []

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
    camposPosicao(camp)

def atk(alvo, frota):
    pontuacao = 0
    quantidade_embarcacao_atingida = 0
    embarcacao_atingida = False
    parcial = ''
    atingidos = []
    
    for embarcacao in frota:
        if '|' in embarcacao:
            parcial = embarcacao.split('|')
            for fogo in alvo:
                if fogo in parcial:
                    if embarcacao_atingida == False:
                        quantidade_embarcacao_atingida += 1
                    embarcacao_atingida = True
                    if fogo not in atingidos:
                        atingidos.append(fogo)

            embarcacao_atingida = False
            if len(atingidos) == len(parcial):
                pontuacao += (3 * len(parcial)) + 2

        else:
            for fogo in alvo:
                if fogo in embarcacao:
                    if embarcacao_atingida == False:
                        quantidade_embarcacao_atingida += 1
                    embarcacao_atingida = True
                    pontuacao += 5
                    
            embarcacao_atingida = False
            
            

    print('pontucao: ', pontuacao, ' ' ,quantidade_embarcacao_atingida, ' alvos errado: ', 13 - quantidade_embarcacao_atingida, ' alvos: ', atingidos)

atk(ataque, J1)
