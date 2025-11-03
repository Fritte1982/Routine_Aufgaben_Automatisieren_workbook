from pprint import pprint
spam = 1
if spam == 1:
    print("Howdy")
elif spam == 2:
    print("greetings")
else:
    print("spam")

def collatz(number):
    if  number  == 1:
        print("done")
    elif number % 2 == 0:
        print ( number / 2)
        collatz(number / 2)
    else:
        print ( number * 3 + 1)
        collatz ( number * 3 + 1)

def iteratives_collatz(number):
    number = prove_number(number)
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2 )
            print (number)
        else:
            number = number * 3 + 1
            print (number)

def prove_number(number):
    try:
        number = int(number)
    except ValueError as e:
        print (number, " is not an integer" +"\n"+ str(e) )
    return number
iteratives_collatz(3)

spam = ['apples', 'bananas', 'tofu', 'cats']


## Page 142
def and_sentence(liste: list):
    sentence = ""
    for i, word in enumerate(liste):
     
        if i < len(liste) - 1:
            sentence = sentence + word + ", "
        else:
            sentence = sentence +  "and " + word
    print (sentence)

and_sentence(spam)

grid = [
 ['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']
]

def pivotierung(grid: list[list[str]]):
    pivotierte_list = []
    for i in range(len(grid[0])):
        new_row= []
        for j in range(len(grid)):
            new_row.append( grid[j][i])
        pivotierte_list.append(new_row)
    pprint(pivotierte_list)

pivotierung(grid)


tic_tac_toe =  {
    "top-L": " ", "top-M": " ", "top-R": " ",
    "mid-L": " ", "mid-M": " ", "mid-R": " ",
    "low-L": " ", "low-M": " ", "low-R": " ",
}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(tic_tac_toe)

def play_tic_tac_toe(board: dict[str, str]):
    board = board
    turn = "X"
    for i in range (9):
        printBoard(board)
        print(f"Zug für {turn} welches Feld wählen Sie? ")
        move = input()
        board[move] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    printBoard(board)

play_tic_tac_toe(tic_tac_toe)



