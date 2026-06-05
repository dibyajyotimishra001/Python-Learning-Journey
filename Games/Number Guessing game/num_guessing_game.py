import random
try:
    rand_num = random.randint(1, 10)
    print("Select a number between 1 to 10")
    user_guess = int(input("Enter your guess: "))

    if user_guess > 10 or user_guess < 0:
        print("Please select a num between 1 to 10")
    else:
        count = 0
        while user_guess != rand_num:
            print("\nYou could not able guess the num")
            user_guess = int(input("Try again: "))
            count += 1

        score = rand_num - count # Score will be depend upon the rand_num, also score can be negetive
        
        with open("Score.txt", "a") as score_storage:
            score_storage.write(f"Your Score: {score}\n")

        print(f"\nYou guessed the num.\nYour score: {score}")
        print(f"You guessed {user_guess}, and computer {rand_num}")

except ValueError:
    print("Something went wrong!")