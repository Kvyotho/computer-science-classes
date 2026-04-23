
tabuleiro = [
  ['   ', '   ', '   '],
  ['   ', '   ', '   '],
  ['   ', '   ', '   ']
]

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

while True:
  print(f'Turno do Jogador {player}')
  exibe_tabuleiro(tabuleiro)
  x, y = movimento_humano(tabuleiro)
  tabuleiro[x][y] = player
  
  player = ' O ' if player == ' X ' else ' X '