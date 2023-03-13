import pandas

# functions go here

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


# calculate the ticket price based on the age
def calc_ticket_price(var_age):

    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for uses between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# checks that users enter a valid response (eg yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "please choose {} or {}".format(valid_responses[0], valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine goes here

# set max num of tickets below
MAX_TICKETS = 5
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]


# lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# asks user if they want to see the instructions
want_instructions = string_checker("do you want to read the instructions (y/n): ", 1, yes_no_list)

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

    # calculate tickets cost
    ticket_cost = calc_ticket_price(age)

    # get payment method
    pay_method = string_checker("Choose a payment method", 2, payment_list)

    if pay_method == "cash":
        surcharge = 0
    else:
        # calculate 5% surcharge if users are paying by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)


# output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("congrats you have sold all the tickets")
else:
    print("you have sold {} ticket/s. there is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))