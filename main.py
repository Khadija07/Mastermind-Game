import random

COLORS = ["G", "B", "R", "Y", "W", "B"]
TRIES = 9
CODE_LENGTH = 3

def generate_color_code():
    code = []  

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_the_code():
     while True:
         guess_code = input("Guess the color code: ").upper().split(" ")    #it will convert all the letters to uppercase and convert it into list using the blank space in the input.
         if len(guess_code) != CODE_LENGTH:
             print(f"You must guess with {CODE_LENGTH} colors.")
             continue
         
         for color in guess_code:
             if color not in COLORS:
                 print(f"Invalid color chosen: {color}, try again.")
                 break
         else:
             break
     return guess_code

def check_code(guess, real_code):

    color_counts = {}

    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game_logic():

    print(f"Welcome to the MASTERMIND game, you have {TRIES} chances to guess the code from the valid colors of {COLORS}.")


    code = generate_color_code()
    for tries in range(1, TRIES + 1):
        Guess = guess_the_code()
        correct_pos, incorrect_pos = check_code(Guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You won and have guessed the correct code in {tries} tries!")
            break

        print(f"Correct positions: {correct_pos} and Incorrect positions: {incorrect_pos}.")

    else:
        print("you ran out of maximum tries, the real code is: ", *code)
    
         
if __name__ == "__main__":
    game_logic()
             