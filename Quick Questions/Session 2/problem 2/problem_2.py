def game():
    import random
    num = int(input("Enter a num you wanna guess between 1 to that num: "))
    rand_num = random.randint(1, num)
    print(rand_num)
    negetive_marking = 0
    while negetive_marking <= num:
        user_guess = int(input("Enter your guessed num: "))
    # Score will depend on the num you choose
        scores = num - negetive_marking
        if user_guess == rand_num:
            print(f"You gussed the num, in {negetive_marking} attempts\nYour score = {scores}")
            break
        else:
            print("You could not able to guess the num")
        negetive_marking += 1

    previous_score = scores

    with open("pre-score.txt", "a") as pre_score:
        pre_score.write(f"Privious Score:- {previous_score}\n")

    return scores

game()