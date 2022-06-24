import database

welcome_message = "Welcome to the Travel booking!"

menu = """
Please select one of the following option:
1. Add new entry.
2. View entries.
3. Exit.

Your selection: """


def prompt_user_entry():
    entry_name = input("Enter Name: ")
    entry_place = input("Enter place: ")
    entry_date = input("Enter date: ")
    database.add_entry(entry_name, entry_place, entry_date)


def display_entries(entries):
    for entry in entries:
        print(f"{entry[0]}\n{entry[1]}\n{entry[2]}\n\n")


database.create_table()

user_input = input(menu)
while(user_input != "3"):
    if (user_input == "1"):
        prompt_user_entry()
    elif (user_input == "2"):
        display_entries(database.get_entries())
    else:
        print("invalid input")
    user_input = input(menu)

database.close()