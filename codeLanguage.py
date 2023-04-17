import random

ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
JOINER = ""


def coding(word):
    if len(word) < 3:
        codedWord = word[::-1]

    else:
        codeOne = word[1:]
        firstLetter = word[0]
        codeTwo = codeOne + firstLetter
        wordList = list(codeTwo)
        firstThree = random.choices(ALPHABETS, k=3) 
        lastThree = random.choices(ALPHABETS, k=3)
        codedWord = JOINER.join(firstThree + wordList + lastThree)
    return codedWord


def decoding(word):
    if len(word) < 3:
        decodedWord = word[::-1]

    else:
        decodeOne = word[3:-3]
        decodedWord = decodeOne[-1] + decodeOne[:-1]
        
    return decodedWord


print("----" *7)
word = input("Please enter your word: ").lower()

choose = input("Do you want to code or decode it?\nEnter 'c' to code or 'd' to decode: ").lower()



while True:
    if choose == "c":
        print(f"Your word is succesfully coded into: '{coding(word)}'")
        break
    elif choose == "d":
        print(f"Your decoded word is: {decoding(word)}")
        break
    else:
        choose = input("Please choose between 'c' & 'd': ")
