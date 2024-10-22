from random import randint

def guess_the_number():

    name = input("Enter your name : ")

    start = int(input("Choose a starting range : "))
                      
    end = int(input("Choose an ending range : "))
    
    comp = randint(start, end)

    user = int(input("Enter your Guess : "))

    count = 1

    while(comp != user):


        if(user < comp):
            print("Higher number please")

        elif(user > comp):
            print("Lower number please")

        user = int(input("Enter your Guess : "))

        count += 1

    # Fetching hi-score.txt

    try:
        with open("hi-score.txt", "r") as f:

            hiscore = f.read()

            if(hiscore != ""):
                hiscore = int(hiscore)
        
            else:
                hiscore = 0
    except FileNotFoundError:
        hiscore = 0

    # Writing High-Score
    if(count < hiscore or hiscore == 0):
        print("Congratulations! You are the Highest Scorer till now")
        with open("hi-score.txt", "w") as f:
            f.write(str(count))

    print(f"Yay! {name} your Guess is correct.\nYour Final Guess is {user}\nYou Guessed the number in {count} attempts.")

    return count

# Starting game
guess_the_number()
