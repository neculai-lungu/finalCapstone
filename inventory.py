from tabulate import tabulate

#Shoe class is created
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return int(self.cost)

    def get_quantity(self):
        return int(self.quantity)

    def __str__(self):
        return f"Country:{self.country}, Code:{self.code}, Product:{self.product}, Cost:{self.cost}, Quantity:{self.quantity}"

#The list will be used to store the class objects.
shoe_list = []

#Function will read text file and create a list of lists
def read_shoes_data():
    f = open("inventory.txt", "r")
    inventory = []
    for line in f:
        inventory.append(line.strip("\n").split(","))
    f.close()
    return inventory

#This function will capture data and create a list of shoe objects
def capture_shoes(list, inventory):
    for line in inventory[1:]:
        list.append(Shoe(line[0], line[1], line[2], line[3], line[4]))
    return list

#Using tabulate this function will display all the shoe objects in a easy to read way
def view_all():
    print(tabulate(read_shoes_data()))
    #for line in shoe_list:
        #print(line)

#This function will find the lowest stock shoe
def re_stock():
    #Dictionary is used to store index and quantity of shoe
    amount = {}
    for index, line in enumerate(shoe_list):
        result = int(line.quantity)
        amount[index] = result
    #Lowest value is stored and user is asked for input
    low_stock = min(amount, key=amount.get)
    print(f"The item {shoe_list[low_stock].product} from {shoe_list[low_stock].country} is low in stock\n")
    restock = input("Would you like to restock: Y/N\n").upper()
    try:
        if restock == "N":
            pass
        elif restock == "Y":
            try:
                #User is asked to input the amount of units to be restocked
                restock_amount = int(input("Enter the amount uou want to restock:\n"))
                #shoe_list and inventory are updated with the new amount
                amount[low_stock] += restock_amount
                shoe_list[low_stock].quantity = amount[low_stock]
                inventory[low_stock + 1][4] = amount[low_stock]
                #The new data is written to text file
                f = open("inventory.txt", "w")
                for line in inventory:
                    ",".join(str(x) for x in line)
                    f.write(",".join(str(x) for x in line))
                    f.write("\n")
                f.close()
            except ValueError:
                print("No such option!\n")
    except TypeError:
        print("No such option!\n")

#This function will search for a specific shoe using a code provided by user
def search_shoe():
    shoe_code = input("Please enter the code of the shoe: \n")
    for item in shoe_list:
        if item.code == shoe_code:
            print(item)


#Function will display total value of each shoe in stock
def value_per_item():
    for item in shoe_list:
        value = item.get_quantity() * item.get_cost()
        print(f"Total value of {item.product}'s from {item.country}: {value}")

#This will display the shoe with the highest stock
def highest_qty():
    amount = {}
    for index, line in enumerate(shoe_list):
        amount[index] = int(line.quantity)
    high_stock = max(amount, key=amount.get)
    print(f"The {shoe_list[high_stock].product}'s are high in stock. You should put this shoe on sale.\n")

#List from text file is stored in inventory
inventory = read_shoes_data()
capture_shoes(shoe_list, inventory)

user_choice = ""

#Main menu
while user_choice != "quit":
    user_choice = input("Please enter a choice from the following:\n"
                        "-------------------------------------------------\n"
                        "va - View all the shoes in stock\n"
                        "low - View the lowest item in stock\n"
                        "high - View the highest item in stock\n"
                        "ss - Search fo a specific shoe by code\n"
                        "vi - Calculate total value of stock for each item\n"
                        "quit - Exit the program\n"
                        "-------------------------------------------------\n").lower()
    if user_choice == "va":
        view_all()
    elif user_choice == "low":
        re_stock()
    elif user_choice == "high":
        highest_qty()
    elif user_choice == "ss":
        search_shoe()
    elif user_choice == "vi":
        value_per_item()
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("No such option!")
