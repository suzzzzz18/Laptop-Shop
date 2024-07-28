from operation import buyLaptop
from operation import sallLaptop
from write import write_buying, write_sellDetails


def displayLaptops():
    print("------------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
    print("------------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("available_laptops.txt", "r")
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")


print("\n")
print("----------------------------------------------------------------------------------------------------")
print("\t \t \t \t Welcome to Oliz Laptop Store")
print("-----------------------------------------------------------------------------------------------------")
print("\t \t \t Sntinagar, Kathmandu | Contact: 9888888888 ")
print("-----------------------------------------------------------------------------------------------------")
print("\n")

continueLoop = True
while continueLoop:
    print("\n")
    print("Press 1 to buy laptops from manufacture.")
    print("Press 2 to sell laptops to customer.")
    print("Press 3 to display available laptops.")
    print("Press 4 to exit.")
    print("\n")
    print("---------------------------------------------------------------------------")
    try:
        userinput = int(input("Press 1,2,3 or 4 :"))
        if userinput == 1:
            company_name, phone, date_time, laptop_bought, VAT, final_total = buyLaptop()
            write_buying(company_name, phone, date_time,
                         laptop_bought, VAT, final_total)

        elif userinput == 2:
            full_name, phone, date_time, laptop_sold, cost_of_shipping, final_total = sallLaptop()
            write_sellDetails(full_name, phone, date_time,
                              laptop_sold, cost_of_shipping, final_total)

        elif userinput == 3:
            displayLaptops()

        elif userinput == 4:
            continueLoop = False
            print("Thank you for visiting our shop.")

        else:
            print("Invalid input! Please Try again.")
    except ValueError:
        print("Invalid input! Please enter a number from 1, 2, 3 or 4.")
