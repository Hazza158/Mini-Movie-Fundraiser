# functions go here

# checks users enter an integer t oa given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response


        except ValueError:
            print("please enter an integer")


# main routine goes here
tickets_sold = 0

while True:

    name = input("enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry you are too young for this movie")
        continue
    else:
        print("?? that looks like a typo, please try again.")
        continue

    tickets_sold += 1

print(" you have sold {} tickets".format(tickets_sold))
