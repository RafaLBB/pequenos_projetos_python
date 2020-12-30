# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random



# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']



# Classe
class Hangman:
    # Método Construtor
    def __init__(self, word):
        self.hide_word = word

    #Método para adivinhar a letra
    def guess(self, letter, secret, word, acerto):
        #self.letter = letter
        #self.secret = secret
        i = 0
        # Varrendo a palavra
        for y in word:
            if letter == y:
                # Acertou uma letra
                secret[i]=letter
                acerto = 1
            i += 1
        return secret, acerto

    # Método para verificar se o jogo terminou
    def hangman_won(self, secret):
        won = secret.count("_")
        if won == 0:
            return True

    # Método para não mostrar a letra no board
    #def hide_word(self):

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self, x):
        global board
        print(board[x])

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("/home/rafaela/Área de Trabalho/jogo_forca/palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    secret = []
    acerto = 0
    game = Hangman(rand_word())
    word = game.hide_word
    cont = len(word)
    print(cont)
    print(word)
    game.print_game_status(0)
    for v in range(0, cont):
        secret.append("_")
        v += 1
    print(secret)
    for x in range(0, 6):
        letter = input("Digite uma letra: \n")
        secret, acerto = game.guess(letter, secret, word, acerto)
        print(secret, acerto)

        if acerto == 0:
            x+=1
            # Verifica o status do jogo
            game.print_game_status(x)

        if game.hangman_won(secret):
        #won = secret.count("_")
        #if won == 0:
            break

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won(secret):
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.hide_word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
