#Guess program

n=18
a=0
y = 1
print("Number of guesses is limited to only 4 times")
while a<=3:
    z=int(input("Enter your choice="))

    if z>n:
        print("Please less your number")
        a+=1
    elif z<n:
        print("Please increase your number")
        a += 1
    else:
        print("You win")
        print(y,"Number of guesses you take to finish the game")
        break

    print(4-y,"Guesses left")
    y+=1
if(a>3):
    print("Game over")



