# functions go here

# checks user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("sorry this cant be blank, please try again")
        else:
            return response


# main routine goes here
while True:
    name = not_blank("enter your name, or 'xxx' to quit")
    if name == "xxx":
        break

print("we are done")
