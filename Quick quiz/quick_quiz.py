"""
==================================================
        PROJECT: *** Quick-Quiz ***
==================================================
Author: Dibyajyoti Mishra
Description: A simple command-line quiz application 
that asks the user a series of questions, checks 
their answers (case-insensitive), and calculates 
a final score.
"""
quiz_data = {
    "What is the capital of Japan?" : "Tokyo",
    "Which planet is known as the Red Planet?" : "Mars",
    "What is the largest ocean on Earth?" : "Pacific",
    "Which animal is known as the Ship of the Desert?" : "Camel",
    "How many wonders are in the world?" : "7",
}
score = 0
print("\nYOU HAVE TO ANSWER ALL THE QUESTIONS IN ONE WORD\n")

for question, correct_answer in quiz_data.items():

    print("\nQuestion: " + question)

    user_input_1 = input("Enter your answer here: ")

    if user_input_1.lower() == correct_answer.lower():
        score += 1
    else:
        pass
    
print(f"\nHere is your total score: {score}")