class PhysicalTraining:
    def __init__(self, trainee_name, total_pushups = 0):
        self.trainee_name = trainee_name
        self.total_pushups = total_pushups
    
    def do_pushups(self, count):
        self.total_pushups += count
        return self.total_pushups

pushups_count = int(input("Enter the number of Push Ups done: "))
do_pushup = PhysicalTraining("Harsira Training")

total_pushups = do_pushup.do_pushups(pushups_count)
total_pushups += 10 # Hard coded as not to disturb user by asking twice if he has done once, adding hard code as I instructed to check my knowledge, if it was a serious project I never do it. Instead of it I can use file i o to save user push up count or use loops

print(f"Training name: Harsira Training\nTotal Pushups: {total_pushups}")