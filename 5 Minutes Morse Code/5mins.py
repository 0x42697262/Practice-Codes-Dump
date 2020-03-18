

import random
import os
import re

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

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_CHART.keys())[list(MORSE_CODE_CHART.values()).index(citext)]
                citext = ''
    return decipher


def morse_word():
    total = 0
    points = 0
    while True:
        print("\nScore: {p}/{t}".format(p=points,t=total))
        total += 1
        words = get_word()
        word_morse = encrypt(words.upper().rstrip())
        
        print("Word: {a}".format(a=word_morse))
        word_answer = input("> ")
        word_answer = encrypt(word_answer.upper())
        
        if word_answer == word_morse:
            print("Correct!")
            points += 1
        elif word_answer == '':
            main()
        else:
            print("Wrong!\nCorrect word is \" {w} \"".format(w=words.rstrip()))

def word_morse():
    total = 0
    points = 0
    while True:
        print("\nScore: {p}/{t}".format(p=points,t=total))
        total += 1
        words = get_word()
        
        
        print(words)
        word_answer = input("> ")
        if len(word_answer) > 0:
            
            
            word_answer = decrypt(word_answer)
        else:
            main()        

        words = words.rstrip().upper()
        if word_answer == words:
            print("Correct!")
            points += 1
        elif word_answer == '':
            main()
        else:
            print("Wrong!\nCorrect code is \" {w} \"".format(w=encrypt(words)))

def main():

    os.system('cls')
    print('''1) Convert Morse Code into English Text
2) Convert English Text to Morse Code
''')
    rx = int(input("> "))
    if rx == 1:
        morse_word()
    elif rx == 2:
        word_morse()
    else:
        exit()

if __name__ == "__main__":
    os.system('cls')
    main()
