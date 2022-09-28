from random import *
words = ["apple","banana","watermelon","peach","orange","grape","mango"]
word = choice(words)
length = len(word)
print(word) 
letters = ""

while True:
    succed = True
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succed = False
    print()

    if succed == True:
        print("Success")
        break
            
    letter = input("Input lertter > ")
    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct")
    else:
        print("Wrong")   

# import random
# word = random.choice(['apple', 'banana', 'orange']) # 맞춰야할 단어
# guess_word = list('_' * len(word)) # 사용자가 추리한 단어
# try_ = 10 # 기회
# print(' '.join(guess_word))
# while try_ > 0:
#     guess = input("Input letter :")
#     if guess == 'break':break # 강제 종료
#     if guess in word:
#         print("Correct")
#         for i in range(len(word)):
#             if word[i] == guess:         
#                 guess_word[i] = guess
#         print(' '.join(guess_word))
#     else:
#         print("Wrong")
#         try_ -= 1
#     if guess_word == list(word):
#         print("Success!")
#         break
