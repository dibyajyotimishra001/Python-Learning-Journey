import random

try:
    rand_num = random.randint(1, 10)
    print("Select a number between 1 to 10") 
    
    negative_marking = 0
    
    while True:
        user_guess = int(input("Enter your guess: "))

        if user_guess > 10 or user_guess < 1:
            print("Please select a number strictly between 1 to 10")
            negative_marking += 1
            continue 

        if user_guess == rand_num:
            break 
        
        print("\nYou could not guess the number")
        negative_marking += 1

    score = 10 - negative_marking
    
    with open("Score.txt", "a") as score_storage:
        score_storage.write(f"Your Score: {score}\n")

    print(f"\nYou guessed the number.\nYour score: {score}")
    print(f"You guessed {user_guess}, and the computer chose {rand_num}")

except ValueError:
    print("Something went wrong! Please enter a valid integer.")