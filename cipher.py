# Cipher Module Collection

import sys

def Vcipher(word, key, direct):
    text = ""
    i = 0
    for letter in word:
        if i > (len (key)-1):
            i = 0
        a = ord (letter)
        if letter.isalpha():
            if direct == "E" or direct == "e":
                num = a+key[i]
            elif direct == "D" or direct == "d":
                num = a-key[i]
            if letter.isupper():
                if num > ord('Z'):
                    num = num - 26
                elif num < ord('A'):
                    num = num + 26
            elif letter.islower():
                if num > ord('z'):
                    num = num - 26
                elif num < ord('a'):
                    num = num +  26
            text = text + chr(num)
            i = i + 1
        else:
            text = text + letter
    return text

def numConvert (word):
    wordnum=[0]*len(word)
    for i in range (0, len(word)):
        wordnum[i] = ord(word[i])-1
        if word[i].isupper():
            wordnum[i]=wordnum[i]-64
        elif word[i].islower():
            wordnum[i]=wordnum[i]-96

    return wordnum

def vigenere (word, key, direct):
    keylist = numConvert(list (key))
    text = Vcipher(word, keylist, direct)
    
    return text

def caesar (word, skip, direct):
    
    if skip > 26:
        skip = skip%26
    elif skip < -26:
        skip = skip%26
        
    key = [skip]
    text = Vcipher(word, key, direct)

    return text

def autokey (word, key, direct):
    keynew = key + word.replace(" ","")
    keylist = numConvert(list (keynew))
    text = Vcipher(word, keylist, direct)
    
    return text

def tableau(word, alpha):
    text = ""
    base = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    for i in range(0,len(word)):
        if word[i] != " ":
            for k in range(0,len(base)):
                if word[i] == base[k]:
                    text = text + alpha [k]
        else:
            text = text + " "
        
    return text

def rot13(word, direct):
    text = caesar(word, 13, direct)

    return text

def flip(word):
    alpha = "zyxwvutsrqponmlkjihgfedcba"

    text = tableau(word,alpha)

    return text
