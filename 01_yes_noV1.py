#functions go here




# main routine goes here
# checks for yes / no, returns "yes" / "no"
want_instructions = input("do you want to read the instructions?")

if want_instructions == "yes" or want_instructions == "y":
    print("instructions go here")
elif want_instructions == "no" or want_instructions == "n":
    pass
else:
    print("please answer yes / no")

print("we are done")

