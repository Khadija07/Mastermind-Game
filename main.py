import random

COLORS = ["G", "B", "R", "Y", "W", "B"]
TRIES = 9
CODE_LENGTH = 3

def generate_color_code():
    code = []  

    for _ in range(COLORS):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_the_code():
     while True:
         guess_code = input("Guess the color code: ".upper().split(" "))      #it will convert all the letters to uppercase and convert it into list using the blank space in the input.
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

         

         
             