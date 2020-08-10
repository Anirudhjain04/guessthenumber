n=18
guesses=1
print("You Have Only 5 lifes: ")
while (guesses<=5):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("Please Enter Greater Number.\n")
    elif guess_number>18:
        print("Please Enter Smaller Number.\n ")
    else:
        print("Winner Winner Chicken Dinner\n")
        print("Numbers of guesses You took to finish.", guesses)
        break
    print(5-guesses,"no. of guesses left")
    guesses = guesses+1

if(guesses>5):
    print("Game Over!!", "The Number was", n)