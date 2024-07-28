def write_sellDetails(name, phone, date_time, laptop_sold, shipping_Cost, final_total):
    with open(str(name) + str(phone) + ".txt", "w")as file:
        file.write("\n")
        file.write("\t \t \t \t Welcome to Oliz Laptop Shop")
        file.write("\n")
        file.write("\t \t \t Sntinagar, Kathmandu | Contact: 9887854743 ")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("\n")
        file.write("\t\t\t\t\t Laptop Selling Details: ")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("Customer Name:" + str(name))
        file.write("\n")
        file.write("Phone Number: " + str(phone))
        file.write("\n")
        file.write("Date and Time: " + str(date_time))
        file.write("\n")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write(
            "Laptop Name \t\t   Brand \t\t\t   Quantity \t\t     Unit Price \t\tTotal")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        for i in laptop_sold:
             file.write(str(i[0]) + "\t" + str(i[1]) + "\t\t\t" +
                       str(i[2]) + "\t\t\t\t" +  str(i[3]) + "\t\t\t\t"+ "$" + str(i[4])+"\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("\n")
        if shipping_Cost == 500:
            file.write("Shipping Cost:" + "" + str(shipping_Cost) + "\n")
            file.write("\n")
            file.write("Total Amount: $" + str(final_total) + "\t\t\t"
                       "[Note: Shipping Amount added to total amount]" + "\n")
            file.write("\n")
        else:
            file.write("Total Amount: $" + str(final_total))
        file.write(
            "\n \t\t\t \t Thank you for your purchase! We really appreciate your business!! \n")
        file.write("\t\t\t    Please keep the receipt for your records. ")


def write_buying(name, phone, date_time, laptop_bought, VAT, final_total):
    with open(str(name) + str(phone) + ".txt", "w")as file:
        file.write("\n")
        file.write("\t \t \t \t  Welcome To Oliz Laptop Shop")
        file.write("\n")
        file.write("\t \t\t Sntinagar, Kathmandu | Contact: 9887854743 ")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t Laptop Buying Details ")
        file.write("\n")
        file.write(
            "--------------------------------------------------------------------------------------------\n")
        file.write("Company Name:" + str(name))
        file.write("\n")
        file.write("Contact: " + str(phone))
        file.write("\n")
        file.write("Date and Time: " + str(date_time))
        file.write("\n")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("Laptop Name \t\t Brand \t\t Quantity \t\t Unit Price \t\t Total")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        for i in laptop_bought:
             file.write(str(i[0]) + "\t" + str(i[1]) + "\t\t\t" +
                       str(i[2]) + "\t\t\t" +  str(i[3]) + "\t\t\t\t"+ "$" + str(i[4])+"\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("\n")
        if VAT:
            file.write("Vat Amount:" + "" + str(VAT) + "\n")
            file.write("\n")
            file.write("Total Amount: $" + str(final_total) +
                       "\t\t[Note: Total Amount include VAT Amount + Total]"+"\n")
            file.write("\n")
        else:
            file.write("Total Amount: $" + str(final_total))
        file.write(
            "\n \t\t\t \t Thank you for your purchase! We really appreciate your business!! \n")
        file.write("\t\t\t    Please keep the receipt for your records. ")