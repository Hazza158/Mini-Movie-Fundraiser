# functions go here

# checks user has entered yes / no to a question
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")


# checks user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("sorry this cant be blank, please try again")
        else:
            return response


# checks users enter an integer t oa given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response


        except ValueError:
            print("please enter an integer")


# main routine goes here

# set max num of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# asks user if they want to see the instructions
want_instructions = yes_no("do you want to read the instructions?")

if want_instructions == "yes" or want_instructions == "y":
    print("instructions go here")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("enter your name, or 'xxx' to quit")

    if name == 'xxx':
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

# output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("congrats you have sold all the tickets")
else:
    print("you have sold {} ticket/s. there is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))