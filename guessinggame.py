import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} Is an incorrect Value, Please try again.".format(temp))


highest = 1000
answer = random.randint(1, highest) #Gives random number between 1 and 10
#print(answer)   #TODO: Remove after testing   #Tells me the answer so I know how to test it. Can find below on todo tab
guess = 0 #initialize to any number that doesn't equal the answer. 0 can't be the answer here
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ") #Needed since user won't know if the answer was ran when they put an incorrect value in

    if guess == 0:  #If user gives up and puts 0, it ends program
        print("Better luck next time")
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        #guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")






