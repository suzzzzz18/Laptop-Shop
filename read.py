def read_file():
    file = open("available_laptops.txt","r")
    laptop_SN = 1
    myLaptop_dict = {}
    for line in file:
        line = line.replace("\n","")
        myLaptop_dict[laptop_SN] = (line.split(","))
        laptop_SN += 1
    file.close()
    return myLaptop_dict
