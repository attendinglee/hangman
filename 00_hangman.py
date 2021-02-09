# 행맨 게임

import random
words = ["apple","coffee","guitar","harmony","programmers","spaghetti"]
question = random.choice(words)  #리스트인 words 값들을 입력받아 하나를 랜덤으로 리턴

letters = ""  # ""도 문자

print("-"*50)
print("Welcome To Hangman Game")
print("-"*50)
life = len(question) + 2   #랜덤으로 리턴받은 단어의 글자수를 세어 2를 더함
while True:   #무한반복
    answer = True
    for w in question:   #question에 담긴 단어에서 문자를 하나씩 꺼냄
        if w in letters: print(w, end="")  #단어가 있다면 해당 단어를 출력
        else: 
            print("_", end=" ")  #단어가 없다면 _을 출력
            answer = False
    print()

    if answer: 
        print("^^ Congraulations!!")
        break
    if life == 0:
        print("--; You Died")
        break

    letter = input("Guess a letter: ")
    if letter not in letters: letters += letter  #사용자가 입력한 단어가 letters에 없다면, 
    if letter in question: print("YES")
    else: 
        life -= 1
        print(f"NO! Your life {life}")
    print()

print("-"*50)
print("Goodbye")
print("-"*50)
