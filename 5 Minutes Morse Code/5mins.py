

import random
import os

MORSE_CODE_CHART = {'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----',
                    ',':'--..--',
                    '.':'.-.-.-',
                    '?':'..--..',
                    '/':'-..-.',
                    '!':'-.-.--',
                    '&':'.-...',
                    '-':'-....-',
                    '+':'.-.-.',
                    '=':'-...-',
                    '(':'-.--.',
                    ')':'-.--.-',
                    ':':'---...',
                    '\'':'.----.',
                    '"':'.-..-.'}

def get_word():
    return random.choice(open('words.txt').readlines())

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_CHART[letter] + ' '
        else:
            cipher += ' '
    return cipher


def main():
    total = 0
    points = 0
    while True:
        print("Score: {p}/{t}".format(p=points,t=total))
        total += 1
        words = get_word()
        word_morse = encrypt(words.upper().rstrip())
        
        print("Word: {a}".format(a=word_morse))
        word_answer = input("Answer: ")
        word_answer = encrypt(word_answer.upper())
        
        if word_answer == word_morse:
            print("Correct!")
            points += 1
        else:
            print("Wrong!\nCorrect word is \"{w}\"".format(w=words.rstrip()))


if __name__ == "__main__":
    os.system('cls')
    main()