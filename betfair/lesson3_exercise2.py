# The program should ask for the word to guess and the number of chances to be given.
# It should then split the characters in the word into individual items in a list.
# The other player should then be allowed to guess characters in the word.
# The program should display correctly guessed characters and unknown characters

string = str(input("Player1 Please Enter the word to guess: "))
lives = int(input("Player1 Please Enter the number of changes: "))

my_list = list(string)
len_list = len(string)
empty_list = ["_"] * len_list
char_posit = ''

  # if is True player is not died yet
alive = True

while alive is True:
    char = str(input("Lives %d, %s :" % (lives, empty_list)))

    if char in string:
        char_posit = string.index(char)
        empty_list[char_posit] = char

    elif lives == 0:
        alive = False
        print("You died!")
    else:
        lives = lives - 1





