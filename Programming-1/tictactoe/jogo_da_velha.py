import random

tabuleiro = [
  ['   ', '   ', '   '],
  ['   ', '   ', '   '],
  ['   ', '   ', '   ']
]

player = ' X '

def exibe_tabuleiro(tabuleiro):
  for linha in tabuleiro:
    print('|'.join(linha))
    print('-'*11)

def movimento_humano(tabuleiro):
  while True:
    try:
      linha = int(input('Escolha a linha (0, 1, 2): '))
      coluna = int(input('Escolha a coluna (0, 1, 2): '))
      if tabuleiro[linha][coluna] == '   ':
        return linha, coluna
      else:
        print('Esta casa está ocupada, tente outra!')
    except (ValueError, IndexError):
      print('Entrada inválida! Utilize apenas numeros entre 0 e 2.')
player = ' X '

def movimento_ia(tabuleiro):
  for i, linha in enumerate(tabuleiro):
    if linha.count(" X ") == 2 and linha.count("   ") == 1:
      coluna = linha.index("   ")
      return i, coluna

  for j in range(len(tabuleiro[0])):
    coluna = [tabuleiro[i][j] for i in range(len(tabuleiro))]
    if coluna.count(" X ") == 2 and coluna.count("   ") == 1:
      linha = coluna.index("   ")
      return linha, j
  
  diagonal_principal = [tabuleiro[i][i] for i in range(len(tabuleiro))]
  if diagonal_principal.count(" X ") == 2 and diagonal_principal.count("   ") == 1:
    linha = diagonal_principal.index("   ")
    return linha, linha
      
  diagonal_secundaria = [tabuleiro[i][len(tabuleiro) - 1 - i] for i in range(len(tabuleiro))]
  if diagonal_secundaria.count(" X ") == 2 and diagonal_secundaria.count("   ") == 1:
    linha = diagonal_secundaria.index("   ")
    return linha, len(tabuleiro) - 1 - linha

  while True: 
      linha = random.randint(0, 2)
      coluna = random.randint(0, 2)
      if tabuleiro[linha][coluna] == "   ":
        return linha, coluna
        
def movimento_ia_inteligente(tabuleiro):
  for linha in tabuleiro:
    if linha.count(" X ") == 2:
      while True:
        linha = linha
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == "   ":
          return linha, coluna

def verificar_linhas(tabuleiro, player):
  for linha in tabuleiro:
      if linha[0] == linha[1] == linha[2] != "   ":
        return True
  return False

def verificar_colunas(tabuleiro, player):
  for i in range(len(tabuleiro[0])):
    if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "   ":
      return True
  return False

def verificar_diagonais(tabuleiro, player):
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "   ":
      return True
    
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "   ":
      return True
    
    return False

def verificar_vitoria(tabuleiro, player):
  if verificar_linhas(tabuleiro, player) or verificar_colunas(tabuleiro, player) or verificar_diagonais(tabuleiro, player):
    return True
  return False

def verificar_empate(tabuleiro):
  for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[0])):
      if tabuleiro[i][j] == "   ":
        return False
  return True

while True:
  print(f'Turno do Jogador {player}')
  exibe_tabuleiro(tabuleiro)
  if player == " X ":
    x, y = movimento_humano(tabuleiro)
  else:
    x, y = movimento_ia(tabuleiro)
  tabuleiro[x][y] = player
  if verificar_vitoria(tabuleiro, player):
    exibe_tabuleiro(tabuleiro)
    print(f'O Jogador {player} ganhou!')
    break
  if verificar_empate(tabuleiro):
    exibe_tabuleiro(tabuleiro)
    print(f'O jogo empatou!')
    break
  
  
  player = ' O ' if player == ' X ' else ' X '
  