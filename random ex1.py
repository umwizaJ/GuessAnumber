import random
RandomNum=random.randint(0,20)
print(RandomNum)
def guessedNum():
    GuessNum=int(input("please guess a number between 0 and 20: "))
    if GuessNum is range (0,20):
       print("please enter valid number")
    if GuessNum==RandomNum:
       print("your guess is right")
    elif GuessNum>RandomNum:
        print("your guess number is too high")
    elif GuessNum<RandomNum:
        print("your guess is too low");
guessedNum();

