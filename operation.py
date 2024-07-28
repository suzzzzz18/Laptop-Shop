from read import read_file
from datetime import datetime

def buyLaptop():
    print("Thank you for buying!")
    print("\n")
    print("----------------------------------------------------------------------")
    print("\n")
    # Input validation for name
    while True:
        try:
            company_name = input("Enter company name: ")
            if not company_name.isalpha():
                raise ValueError("Please enter a valid name!!")
            break
        except ValueError as e:
            print(e)
            print("\n")

    # Input validation for phone number
    while True:
        try:
            phone = input("Enter your phone: ")
            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Please enter a valid phone number!!")
            break
        except ValueError as e:
            print(e)
            print("\n")
    print("-------------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
    print("-------------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("available_laptops.txt", "r")
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("-------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    laptop_bought = []
    while True:
        valid_id = int(
            input("Please enter the ID of the product you want to buy:"))
        print("\n")

         #validating user input for the laptop ID and quantity
        while valid_id <= 0 or valid_id > len(read_file()):
            print("Please enter a valid Laptop ID!!")
            print("\n")
            valid_id = int(
                input("Enter the ID of the laptop you want to buy: "))

        laptop_quantity = int(
            input("Please enter the number of quantity of the Laptop you want to buy: "))
        print("\n")

        # Validating Quantity of laptop in stock
        mylaptop_dict = read_file()
        getlaptop_quantity = mylaptop_dict[valid_id][3]
        while laptop_quantity <= 0 or laptop_quantity > int(getlaptop_quantity):
            print("The quantity of laptop you want to buy is currently unavailable in our store. Please see the above available laptops.")
            print("\n")
            laptop_quantity = int(
                input("Please enter the number of quantity of the Laptop you want to buy: "))
        print("\n")

        # Updating quantity of laptop in the text file
        mylaptop_dict[valid_id][3] = int(mylaptop_dict[valid_id][3]) + int(laptop_quantity)
        file = open("available_laptops.txt", "w")
        for values in mylaptop_dict.values():
            file.write(str(values[0])+"," + str(values[1])+"," + str(values[2]) +
                       "," + str(values[3])+"," + str(values[4])+"," + str(values[5]))
            file.write("\n")
        file.close()

        # Purchasing from manufacturer
        laptop_name = mylaptop_dict[valid_id][0]
        quantity_of_laptop = laptop_quantity
        unit_price = mylaptop_dict[valid_id][2]
        total_price_of_laptop = mylaptop_dict[valid_id][2].replace("$", '')
        final_price = int(total_price_of_laptop)*int(quantity_of_laptop)
        laptop_brand = mylaptop_dict[valid_id][1]
        laptop_bought.append(
            [laptop_name,laptop_brand, quantity_of_laptop, total_price_of_laptop, final_price, laptop_brand])

        buy_more = input("Do you want to buy more laptops? (Y/N): ")
        if buy_more.isalpha() and buy_more.lower() == 'n':
            break
        elif buy_more.isalpha() and buy_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            buy_more = input("Do you want to buy more laptops? (Y/N): ")
        if buy_more.lower() == 'n':
            break
        elif buy_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Exiting loop.")
            buy_more = input("Do you want to buy more laptops? (Y/N): ")
        if buy_more.lower() == 'n':
            break
        elif buy_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Exiting loop.")
            break

    total = 0
    for i in laptop_bought:
        total += int(i[4])
        VAT = 0.13*(total)
    final_total = total + VAT
    date_time = datetime.now()
    print("\n")
    print("\t \t \t \t Welcome to Oliz Laptop Shop!")
    print("\n")
    print("\t \t\t\t\   Sntinagar, Kathmandu | Contact: 9887854743")
    print("\n")
    print("----------------------------------------------------------------------------------------")
    print("Laptop Buying Details: ")
    print("----------------------------------------------------------------------------------------")
    print("Customer Name:" + str(company_name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("----------------------------------------------------------------------------------------")
    print("\n")
    print("Buying Details are:")
    print("-------------------------------------------------------------------------------------------------------------")
    print("Laptop Name \t\t\t\tBrand \t\t Total Quantity \t\t Unit Price \t\t Total")
    print("-------------------------------------------------------------------------------------------------------------")
    for i in laptop_bought:
        print(i[0], "\t\t", i[1],
              "\t\t", i[2], "\t\t\t", i[3], "\t\t", "$", i[4])
    print("-------------------------------------------------------------------------------------------------------------")
    print("Vat Amount:",  VAT)
    print("Grand Total:" + str(final_total))
    print("Note: Vat Amount added to grand total")

    return company_name, phone, date_time, laptop_bought, VAT, final_total


def sallLaptop():
    print("Thank you for visiting our shop!")
    print("\n")
    print("---------------------------------------------------------------------")
    print("Provide your name and number to get the bill.")
    print("---------------------------------------------------------------------")
    print("\n")
    # Input validation for full name
    while True:
        try:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if not (first_name.isalpha() and last_name.isalpha()):
                raise ValueError("Please provide a valid name!!")
            full_name = first_name + " " + last_name
            break
        except ValueError as e:
            print(e)
            print("\n")

    # Input validation for phone number
    while True:
        try:
            phone = input("Enter your phone: ")
            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Please provide a valid phone number !!")
            break
        except ValueError as e:
            print(e)
            print("\n")
    print("-------------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t      Brand \t   Price \t Quantity \t Processor \t Graphic Card")
    print("-------------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("available_laptops.txt", "r")
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("-------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    laptop_sold = []

    while True:
        valid_id = int(input(
            "Enter the ID of the laptop you want to sell: "))
        if valid_id == 0:
            break

       
        #validating user input for the laptop ID and quantity
        while valid_id <= 0 or valid_id > len(read_file()):
            print("Please enter a valid Laptop ID !!")
            print("\n")
            valid_id = int(
                input("Please enter the ID of the laptop you want to sell: "))

        laptop_quantity = int(
            input("Please enter the number of laptops you want to sell: "))
        print("\n")

        # Validating Quantity of laptop in stock

        mylaptop_dict = read_file()
        getlaptop_quantity = mylaptop_dict[valid_id][3]
        while laptop_quantity <= 0 or laptop_quantity > int(getlaptop_quantity):
            print("The quantity of laptop you want to buy is currently unavailable in our store. Please see above for available laptops.")
            print("\n")
            laptop_quantity = int(
                input("Enter the quantity of laptop you want to buy."))
        print("\n")

        # Updating quanity of laptop in the text file

        mylaptop_dict[valid_id][3] = int(
            mylaptop_dict[valid_id][3]) - int(laptop_quantity)

        file = open("available_laptops.txt", "w")

        for values in mylaptop_dict.values():
            file.write(str(values[0])+"," + str(values[1])+"," + str(values[2]) +
                       "," + str(values[3])+"," + str(values[4])+"," + str(values[5]))
            file.write("\n")
        file.close()

        # Details of laptop sold

        laptop_name = mylaptop_dict[valid_id][0]
        quantity_of_laptop = laptop_quantity
        laptop_brand = mylaptop_dict[valid_id][1]
        unit_price = mylaptop_dict[valid_id][2]
        total_price_of_laptop = mylaptop_dict[valid_id][2].replace("$", '')
        final_price = int(total_price_of_laptop)*int(quantity_of_laptop)

        laptop_sold.append(
            [laptop_name,laptop_brand, quantity_of_laptop, total_price_of_laptop, final_price])

        sell_more = input("Do you want to sell more laptops? (Y/N): ")
        if sell_more.isalpha() and sell_more.lower() == 'n':
            break
        elif sell_more.isalpha() and sell_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            sell_more = input("Do you want to sell more laptops? (Y/N): ")
        if sell_more.lower() == 'n':
            break
        elif sell_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Try again.")
            sell_more = input("Do you want to sell more laptops? (Y/N): ")
        if sell_more.lower() == 'n':
            break
        elif sell_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Try again.")
            break

    date_time = datetime.now()

    print("\n")
    print("\t \t \t \t  Welcome to Oliz Laptop Shop")
    print("\t \t Sntinagar, Kathmandu | Contact: 9887854743")
    print("----------------------------------------------------------------------------------------")
    print("\n")
    print("Customer Details: ")
    print("---------------------")
    print("Customer Name:" + str(full_name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("----------------------------------------------------------------------------------------")
    print("\n")
    print("Laptop Selling Details:")
    print("-------------------------------------------------------------------------------------------------------------")
    print("Laptop Name \t\tBrand \t\t Total Quantity \t\t Unit Price \t\t\t Total")
    print("-------------------------------------------------------------------------------------------------------------")

    for i in laptop_sold:
        print(i[0], "\t\t", i[1],"\t\t", i[2], "\t\t\t", i[3], "$", "\t", i[4])
    print("-------------------------------------------------------------------------------------------------------------")

    total = 0
    shipping_Cost = 0
    while True:
        shipping_choice = input(
            "Dear Customer, do you want your laptop to be shipped? (Y/N)")
        if shipping_choice.lower() == "y":
            shipping_Cost = 500
            break
        elif shipping_choice.lower() == "n":
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    print("Shipping Cost:", shipping_Cost)
    print("Note: Shipping cost is added to grand total.")

    for i in laptop_sold:
        total += int(i[4])
    final_total = total + shipping_Cost
    print("Total Amount:" + str(final_total))
    print("Note: Shipping amount is added to total amount.")

    return full_name, phone, date_time, laptop_sold, shipping_Cost, final_total
