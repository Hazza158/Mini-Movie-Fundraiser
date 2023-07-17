import pandas

# functions go here


def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")


def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


def string_checker(question, num_letters, valid_responses):

    error = "Error: that is the incorrect response, please try again"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# checks users enter an integer t oa given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response


        except ValueError:
            print("please enter an integer")


# currency formatting
def currency(x):
    return f"${x:.2f}"
    # return "${:.2f}".format(x)


# main routine goes here
# Gets expenses, returns list wish has the data frame and sub-total

def get_expenses(var_fixed):
    # Set up dictionaries and lists

    item_list = []
    amount_list = []
    price_list = []
    unit_list = ["gram", "kilogram", "millilitre", "Litre"]

    variable_dict = {
        "Item": item_list,
        "Amount": amount_list,
        "Price": price_list,
        "Unit": unit_list

    }

    # loop to get component, Amount and price
    item_name = ""

    while item_name.lower() != "xxx":

        print()
        # get name, amount and item
        item_name = not_blank("Ingredient name: ",
                              "The ingredient name can't be blank.")

        if item_name.lower() == "xxx":
            break

        amount = num_check("Amount:", "The amount must be a whole number which is more than zero", int)
        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)
        unit = string_checker("Please enter the measurement unit (g, kg, mL, L):", "Incorrect response", unit_list)
        # add item, quantity, price, and unit to lists
        item_list.append(item_name)
        amount_list.append(amount)
        price_list.append(price)
        unit_list.append(unit)

        expense_frame = pandas.DataFrame(variable_dict)
        expense_frame = expense_frame.set_index('Item')

        expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['Price'] + unit_frame['Unit']
        # Find sub-total
        expense_sub = expense_frame['Cost'].sum()

        add_dollars = ['Price', 'Cost']
        for item in add_dollars:
            expense_frame[item] = expense_frame[item].apply(currency)

        return [expense_frame, expense_sub, unit_frame]


# **** Main routine begins ****

# Get Recipe name
recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank.")

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]
unit_frame = variable_expenses[2]

# **** Printing Area ****

print()
print(variable_frame)
print()

print("Variable Costs: ${:.2f}".format(variable_sub))
