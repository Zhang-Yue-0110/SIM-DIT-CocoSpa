# This program was specifically designed for Coco Spa Company, and it is aimed at assisting managers and
# employees with various tasks, including product management, sales management, and numerous other functionalities.

# This function is to calculate the total price, generate the order ID and display the order summary
def process_order(matching_names, choice_index, order, customerService_dict, numberID):
    while xx == 0:
        print("\n\t\t\t\t\t\t\t\t\t\tOrder Summary")
        total = 0
        for orders in order:
            itemName, thing, itemCode, itemPrice = orders
            print("{:<15}\t{:<40}\t{:<20}\t{:<20}".format(itemName, thing, itemCode,
                                                          "$" + str(itemPrice)))
            total += itemPrice
        customerService_dict[matching_names[choice_index]]["Loyalty Point"] = total + int(
            customerService_dict[matching_names[choice_index]]["Loyalty Point"])
        print("\nTotal", "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   ", "$" + str(total))
        print("Customer\'s name:", matching_names[choice_index])
        print("----------------------------------------")
        orderCustomer = matching_names[choice_index]
        additionalTotal.append(total)
        option = input("Enter 1 to confirm, 0 to cancel: ")
        if option == "1":
            x = str(numberID)
            orderID = "CCO-24-000" + x
            print("The Order ID: " + orderID)
            print()
            orderOpen[matching_names[choice_index], orderID] = order
            numberID += 1
            break
        elif option == "0":
            print()
            break


# This function is to update or delete the services, packages and products
def case_a(list_A_B_C, index, delete):
    if list_A_B_C == listA:
        print('%s, %s, %s' % list_A_B_C[index])
        update = input("Do you want to update or delete the service? ")
    elif list_A_B_C == listB:
        print('%s, %s, %s, %s, %s' % list_A_B_C[index])
        update = input("Do you want to update or delete the package? ")
    elif list_A_B_C == listC:
        print('%s, %s, %s, %s' % list_A_B_C[index])
        update = input("Do you want to update or delete the product? ")
    # To update
    if update == "update":
        listD = list_A_B_C[index]
        list_A_B_C.remove(list_A_B_C[index])
        if list_A_B_C == listA:
            print('%s, %s, %s' % listD)
            pay = input("The price of the service is ")
            after = (listD[0], listD[1], "$" + pay)
            list_A_B_C.insert(index, after)
            print('%s, %s, %s' % list_A_B_C[index])
            print()
        elif list_A_B_C == listB:
            print('%s, %s, %s, %s, %s' % listD)
            payOriginal = int(input("The original price of the service is "))
            pay = int(input("The new price of the package is "))
            if pay > payOriginal:
                pay = input("Please make the price less than " + listD[2] + ": ")
            else:
                print()
            after = (listD[0], listD[1], "$" + str(pay), listD[3], listD[4])
            list_A_B_C.insert(index, after)
            print('%s, %s, %s, %s, %s' % list_A_B_C[index])
            print()
        elif list_A_B_C == listC:
            print('%s, %s, %s, %s' % listD)
            pay = input("The price of the product is ")
            after = (listD[0], listD[1], "$" + pay, listD[3])
            list_A_B_C.insert(index, after)
            print('%s, %s, %s, %s' % list_A_B_C[index])
            print()
    # To delete
    elif update == "delete":
        list_A_B_C.remove(list_A_B_C[index])
        list_A_B_C.insert(index, delete)
    else:
        print("Invalid")
    return list_A_B_C


# This function is to create a list to match the customer
def search_customers_alternative(customers, search_term):
    matches = []
    for customer in customers:
        if search_term.lower() in customer.lower():
            matches.append(customer)
    return matches


# To open and upload the services in user's computer
with open("listA.txt", 'r', encoding='utf-8') as file:
    lista = [line.strip() for line in file]
listA = []
for item in lista:
    elements = item.split(',')
    listA.append((elements[0], elements[1], elements[2]))
# To open and upload the packages in user's computer
with open("listB.txt", 'r', encoding='utf-8') as file:
    listb = [line.strip() for line in file]
listB = []
for item in listb:
    elements = item.split(',')
    listB.append((elements[0], elements[1], elements[2], elements[3], elements[4]))
# To open and upload the product in user's computer
with open("listC.txt", 'r', encoding='utf-8') as file:
    listc = [line.strip() for line in file]
listC = []
for item in listc:
    elements = item.split(',')
    listC.append((elements[0], elements[1], elements[2], elements[3]))
# Customer information
customerService_dict = {
    "Tan Ah Mee": {"Gender": "Male", "Birthday": "1999-01-01", "Contact": "123456789",
                   "SV001": ["30 min Express Face treatment", 1, "left"],
                   "SV002": ["Face Cleansing", 10, "left"],
                   "Loyalty Point": "2000"},
    "John Tan": {"Gender": "Female", "Birthday": "2000-04-01", "Contact": "987654321",
                 "SV002": ["Face Cleansing", 10, "left"],
                 "Loyalty Point": "0"},
    "Kristan Wu": {"Gender": "Male", "Birthday": "2002-06-01", "Contact": "192837465",
                   "SV005": ["Full rejuvenation treatment", 10, "left"],
                   "Loyalty Point": "100"},
}

numberID = 1
order = []
orderOpen = {}
xx = 0
additionalTotal = []
orderCustomer = 0
endProgram = 100
p = 0
# Main program
print("@@@ Coco Spa @@@")
position = input("Enter your position in the Coco Spa: ")
# To identify the user's identity
if position == "Admin":
    while p == 0:
        # To identify the user's identity
        companyCode = input("Enter your company code: ")
        if companyCode == "001":
            p = 1
            # Four function for administrator to use
            while endProgram == 100:
                print(" 1.Product management\n", "2.Sales management\n", "3.Sales report\n", "0.Exit")
                option = int(input("Enter option: "))
                # function 1 : Product management
                if option == 1:
                    while endProgram == 100:
                        print(" a.View / Update services\n", "b.Add new services\n", "c.View / Update Packages\n",
                              "d.Add new Package\n", "e.View / Update Products\n", "f.Add new Product\n",
                              "g.Back to main menu")
                        option = input("Enter option: ")
                        # Match the function the user choose
                        match option:
                            # Function 1.a
                            case "a":
                                # Display the appendix A
                                for item in listA:
                                    print(f"{item[0]},{item[1]},{item[2]}")
                                # Choose the service or back to previous menu
                                print(
                                    "To update a service, enter the item code. Or enter 0 to go back to previous menu.")
                                option = input("Enter option: ")
                                match option:
                                    # Service 1
                                    case "SV001":
                                        index = 0
                                        delete = ("", "", "")
                                        listA = case_a(listA, index, delete)
                                    # Service 2
                                    case "SV002":
                                        index = 1
                                        delete = ("", "", "")
                                        listA = case_a(listA, index, delete)
                                    case "SV003":
                                        index = 2
                                        delete = ("", "", "")
                                        listA = case_a(listA, index, delete)
                                    # Service 4
                                    case "SV004":
                                        index = 3
                                        delete = ("", "", "")
                                        listA = case_a(listA, index, delete)
                                    # Service 5
                                    case "SV005":
                                        index = 4
                                        delete = ("", "", "")
                                        listA = case_a(listA, index, delete)
                                    case "0":
                                        print()
                                    case default:
                                        print("Appropriate error message")
                            # Function 1.b
                            case "b":
                                newService = int(input("The number of new service is : "))
                                b = 1
                                while b <= newService:
                                    # To create new service
                                    newName = input("The new service name is : ")
                                    a = 1
                                    while a == 1:
                                        # Manually enter the item code or automatically generate the item code
                                        option = input(
                                            "You can choose manually entered(A) or automatically generated(B) the item code: ")
                                        # Manually entered
                                        if option == "A":
                                            while a == 1:
                                                new1 = input("The new service code is : ")
                                                newCode = str(new1)
                                                if newCode != "SV001" and "SV002" and "SV003" and "SV004" and "SV005":
                                                    newPrice = input("The new service price is : ")
                                                    newItem = (newCode, newName, "$" + newPrice)
                                                    listA.append(newItem)
                                                    print()
                                                    b += 1
                                                    a = 2
                                                else:
                                                    print("The item code has be unique")
                                        # Automatically generated
                                        else:
                                            c = str(b + 5)
                                            newCode = "SV00" + c
                                            newPrice = input("The new service price is : ")
                                            newItem = (newCode, newName, "$" + newPrice)
                                            listA.append(newItem)
                                            b += 1
                                            a = 2
                                            print()

                            # Function 1.c
                            case "c":
                                for item in listB:
                                    print(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}")
                                print(
                                    "To update a package, enter the item code. Or enter 0 to go back to previous menu.")
                                option = input("Enter option: ")
                                # Match the function the user choose
                                match option:
                                    case "PK001":
                                        index = 0
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listB = case_a(listB, index, delete)
                                    case "PK002":
                                        index = 1
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listB = case_a(listB, index, delete)
                                    case "PK003":
                                        index = 2
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listB = case_a(listB, index, delete)
                                    case "PK004":
                                        index = 3
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listB = case_a(listB, index, delete)
                                    case "PK005":
                                        index = 4
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listB = case_a(listB, index, delete)
                                    case "PK006":
                                        index = 5
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listB = case_a(listB, index, delete)
                                    case "0":
                                        print()
                                    case default:
                                        print("Appropriate error message")
                            # Function 1.d
                            case "d":
                                packageNumber = int(input("The number of new package is "))
                                b = 1
                                while b <= packageNumber:
                                    packageName = input("The name of the package is ")
                                    a = 1
                                    while a == 1:
                                        # Manually enter the item code or automatically generate the item code
                                        option = input(
                                            "You can choose manually entered(A)or automatically generated(B)")
                                        # Manually entered
                                        if option == "A":
                                            e = 1
                                            while e == 1:
                                                new1 = input("The new item code is ")
                                                newCode = str(new1)
                                                if (new1 != "PK001" and new1 != "PK002" and new1 != "PK003"
                                                        and new1 != "PK004" and new1 != "PK005" and new1 != "PK006"):
                                                    for item in listA:
                                                        print(f"{item[0]},{item[1]},{item[2]}")
                                                    changePrice = int(
                                                        input(
                                                            "Enter the number of  service  you want to create a package: "))
                                                    index = changePrice - 1
                                                    element = listA[index]
                                                    print('%s, %s, %s' % element)
                                                    price = int(input("The retail price is "))
                                                    times = int(input("How many times of the "
                                                                      "service including in this package"))
                                                    packageRetail = price * times
                                                    e = e + 1
                                                    c = 1
                                                    while c == 1:
                                                        newPrice = int(input("The new package price is "))
                                                        # To compare the new package price and the retail price multiply times
                                                        if newPrice <= packageRetail:
                                                            servicePackage = element[0]
                                                            priceNew = str(newPrice * times)
                                                            packageNew = (
                                                                newCode, packageName, "$" + priceNew, servicePackage,
                                                                times)
                                                            listB.append(packageNew)
                                                            c = c + 1
                                                            a = a + 1
                                                            b = b + 1
                                                            print()
                                                        else:
                                                            print("Please set a reasonable price")
                                                else:
                                                    print("The service code has be unique")
                                        # Automatically generated
                                        else:
                                            d = str(b + 6)
                                            newCode = "PK00" + d
                                            for item in listA:
                                                print(f"{item[0]},{item[1]},{item[2]}")
                                            changePrice = int(input("Which service do you want to create a package?"))
                                            index = changePrice - 1
                                            element = listA[index]
                                            print('%s, %s, %s' % element)
                                            price = int(input("The retail price is "))
                                            times = int(
                                                input("How many times of the service including in this package"))
                                            packageRetail = price * times
                                            newPrice = int(input("The new package price is "))
                                            c = 1
                                            # To compare the new package price and the retail price multiply times
                                            while c == 1:
                                                if newPrice <= packageRetail:
                                                    servicePackage = element[0]
                                                    priceNew = str(newPrice * times)
                                                    packageNew = (
                                                        newCode, packageName, "$" + priceNew, servicePackage, times)
                                                    listB.append(packageNew)
                                                    c = c + 1
                                                    a = a + 1
                                                    b = b + 1
                                                    print()
                                                else:
                                                    print("Please set a reasonable price")
                            # Function 1.e
                            case "e":
                                for item in listC:
                                    print(f"{item[0]},{item[1]},{item[2]},{item[3]}")
                                print(
                                    "To update a Product, enter the item code. Or enter 0 to go back to previous menu.")
                                option = input("Enter option: ")
                                match option:
                                    case "P001":
                                        index = 0
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listC = case_a(listC, index, delete)
                                    case "P002":
                                        index = 1
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listC = case_a(listC, index, delete)
                                    case "P003":
                                        index = 2
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listC = case_a(listC, index, delete)
                                    case "P004":
                                        index = 3
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listC = case_a(listC, index, delete)
                                    case "P005":
                                        index = 4
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listC = case_a(listC, index, delete)
                                    case "P006":
                                        index = 5
                                        delete = ('', '', '', '')
                                        # Calling function
                                        listC = case_a(listC, index, delete)
                                    case "0":
                                        print()
                                    case default:
                                        print("Appropriate error message")
                            # Function 1.f
                            case "f":
                                newProduct = int(input("The number of new product is "))
                                b = 1
                                while b <= newProduct:
                                    newName = input("The new product name is : ")
                                    a = 1
                                    while a == 1:
                                        # Manually enter the item code or automatically generate the item code
                                        option = input(
                                            "You can choose manually entered(A) or automatically generated (B)")
                                        e = 1
                                        while e == 1:
                                            # Manually entered
                                            if option == "A":
                                                new1 = input("The new product code is : ")
                                                newCode = str(new1)
                                                q = 1
                                                while q == 1:
                                                    if newCode != "P001" and newCode != "P002" and newCode != "P003" and newCode != "P004" and newCode != "P005" and newCode != "P006":
                                                        newPrice = input("The new product price is : ")
                                                        newItem = (newCode, newName, "$" + newPrice, "Available")
                                                        listC.append(newItem)
                                                        b += 1
                                                        a = 2
                                                        e += 1
                                                        q = 2
                                                        print()
                                                    else:
                                                        print("The item code has be unique")
                                                        break
                                            # Automatically generated
                                            else:
                                                c = str(len(listC) + 1)
                                                newCode = "P00" + c
                                                newPrice = input("The new product price is: ")
                                                newItem = (newCode, newName, "$" + newPrice, "Available")
                                                listC.append(newItem)
                                                print()
                                                b += 1
                                                a = 2
                                                e += 1
                            # Exit the function 1
                            case "g":
                                print("Back to main menu")
                                break
                            case default:
                                break
                # Function 2 : Sales management
                elif option == 2:
                    while endProgram == 100:
                        print(" a.Create order\n", "b.View order\n", "c.Create customer\n",
                              "d.View customer\n", "e.Back to main menu")
                        option = input("Enter option: ")
                        # Match the function the user choose
                        match option:
                            # Function 2.a
                            case "a":
                                input_name = input("Enter the name you want to search or enter 0 to back to main menu:")
                                # Identify the name in the customer information file
                                matching_names = [name for name in customerService_dict.keys() if
                                                  input_name.lower() in name.lower()]
                                # If the name in the file
                                if matching_names:
                                    print("Name list：")
                                    for i, name in enumerate(matching_names, 1):
                                        print(f"{i}. {name}")
                                    choice_index = int(input("Enter the number you choose：")) - 1
                                    while True:
                                        # Display the function of a
                                        functionChoice = int(input("1) Use Service\n2) Buy Package\n3) Buy product\n"
                                                                   "4) Back to main menu\nEnter your choice: "))
                                        # function 2.a.1
                                        if functionChoice == 1:
                                            itemName = "Service"
                                            chosen_name = matching_names[choice_index]
                                            for item in listA:
                                                print(f"{item[0]},{item[1]},{item[2]}")
                                            input_service = input("Enter the item code you choose：")
                                            # To identify whether the service the customer have
                                            if input_service in customerService_dict[chosen_name]:
                                                print("You have", customerService_dict[chosen_name][input_service][0],
                                                      ": ",
                                                      customerService_dict[chosen_name][input_service][1],
                                                      customerService_dict[chosen_name][input_service][2])
                                                # To identify the service quantity greater than 0
                                                if customerService_dict[chosen_name][input_service][1] > 0:
                                                    print(
                                                        "Quantity will be deducted automatically when order is complete")
                                                    thing = customerService_dict[chosen_name][input_service][0]
                                                    itemCode = input_service
                                                    itemPrice = 0
                                                    order.append((itemName, thing, itemCode, itemPrice))
                                                # Service quantity less than 0
                                                else:
                                                    print("You don't have enough service time to use")
                                                    thing = customerService_dict[chosen_name][input_service][0]
                                                    itemCode = input_service
                                                    itemPrice = int(
                                                        input("Enter the retail price of the service you choose"))
                                                    order.append((itemName, thing, itemCode, itemPrice))
                                                customerService_dict[chosen_name][input_service][1] -= 1
                                                if customerService_dict[chosen_name][input_service][1] == 0:
                                                    del (customerService_dict[chosen_name][input_service])
                                            # Customer don't have enough service times
                                            else:
                                                print("You don't have enough service times")
                                                thing = input("Enter the service name ")
                                                a = int(input("Enter the retail price of the service you choose "))
                                                itemPrice = a
                                                itemCode = input_service
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            # Continue ordering or complete order
                                            customerOption = input("Do want to continue ordering, or complete order? ")
                                            if customerOption != "continue":
                                                # Calling function
                                                process_order(matching_names, choice_index, order, customerService_dict,
                                                              numberID)
                                                numberID += 1
                                                order = []
                                                break
                                        # Function 2.a.2
                                        elif functionChoice == 2:
                                            chosen_name = matching_names[choice_index]
                                            for item in listB:
                                                print(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}")
                                            choice = input("Which package you want to buy? ")
                                            itemName = "Package"
                                            if choice == "PK001":
                                                thing = "Express Package"
                                                itemCode = "PK001"
                                                itemPrice = 620
                                                customerService_dict[chosen_name]["SV001"] = [
                                                    "30 min Express Face treatment", 10,
                                                    "left"]
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "PK002":
                                                thing = "Express Package"
                                                itemCode = "PK002"
                                                itemPrice = 1200
                                                customerService_dict[chosen_name]["SV001"] = [
                                                    "30 min Express Face treatment", 20,
                                                    "left"]
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "PK003":
                                                thing = "Face Cleansing"
                                                itemCode = "PK003"
                                                itemPrice = 1125
                                                customerService_dict[chosen_name]["SV002"] = ["Face Cleansing", 10,
                                                                                              "left"]
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "PK004":
                                                thing = "Deep Face Cleansing"
                                                itemCode = "PK004"
                                                itemPrice = 1600
                                                customerService_dict[chosen_name]["SV003"] = ["Deep Face Cleansing", 10,
                                                                                              "left"]
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "PK005":
                                                thing = "Laser Face treatment"
                                                itemCode = "PK005"
                                                itemPrice = 1290
                                                customerService_dict[chosen_name]["SV004"] = ["Laser Face treatment", 6,
                                                                                              "left"]
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "PK006":
                                                thing = "Full rejuvenation"
                                                itemCode = "PK006"
                                                itemPrice = 1560
                                                customerService_dict[chosen_name]["SV005"] = [
                                                    "Full rejuvenation treatment", 6, "left"]
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            else:
                                                thing = input("Package name: ")
                                                itemCode = choice
                                                itemPrice = int(input("Package price: "))
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            customerOption = input("Do want to continue ordering, or complete order? ")
                                            # Continue ordering or complete order
                                            if customerOption != "continue":
                                                # Calling function
                                                process_order(matching_names, choice_index, order, customerService_dict,
                                                              numberID)
                                                numberID += 1
                                                order = []
                                                break
                                        # Function 2.a.3
                                        elif functionChoice == 3:
                                            for item in listC:
                                                print(f"{item[0]},{item[1]},{item[2]},{item[3]}")
                                            choice = input("Which package you want to buy? ")
                                            itemName = "Product"
                                            if choice == "P001":
                                                thing = "Whitening cream"
                                                itemCode = "P001"
                                                itemPrice = 128
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "P002":
                                                thing = "Eye cream"
                                                itemCode = "P002"
                                                itemPrice = 90
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "P003":
                                                thing = "Facelift cream"
                                                itemCode = "P003"
                                                itemPrice = 188
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "P004":
                                                thing = "Eye mask"
                                                itemCode = "P004"
                                                itemPrice = 60
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "P005":
                                                thing = "Cleanser"
                                                itemCode = "P005"
                                                itemPrice = 65
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            elif choice == "P006":
                                                thing = "Anti aging serum"
                                                itemCode = "P006"
                                                itemPrice = 168
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            else:
                                                thing = input("Product name: ")
                                                itemCode = choice
                                                itemPrice = int(input("Product price: "))
                                                order.append((itemName, thing, itemCode, itemPrice))
                                            customerOption = input("Do want to continue ordering, or complete order? ")
                                            # Continue ordering or complete order
                                            if customerOption != "continue":
                                                # Calling function
                                                process_order(matching_names, choice_index, order, customerService_dict,
                                                              numberID)
                                                numberID += 1
                                                order = []
                                                break
                                        # Function 2.a.4
                                        elif functionChoice == 4:
                                            break
                                elif input_name == "0":
                                    print()
                                # If the name isn't in the file
                                else:
                                    print("No such name you search")
                            # Function 2.b
                            case "b":
                                for key, value in orderOpen.items():
                                    print(f"Customer Name: {key[0]}\n \tOrder ID: {key[1]}")
                                    for item in value:
                                        print(" \t{:<15}{:<40}{:<20}{:<20}".format(item[0], item[1], item[2],
                                                                                   "$" + str(item[3])))
                                    print()
                            # Function 2.c
                            case "c":
                                newCustomer = input("Enter the customer name: ")
                                customerGender = input("Enter the customer gender: ")
                                customerBirthday = input("Enter the customer birthday: ")
                                customerContact = input("Enter the customer contact: ")
                                customerService_dict[newCustomer] = {"Gender": customerGender,
                                                                     "Birthday": customerBirthday,
                                                                     "Contact": customerContact, "Service": [""],
                                                                     "Loyalty Point": "0"}
                            # Function 2.d
                            case "d":
                                for name, details in customerService_dict.items():
                                    print(f"Name: {name}")
                                    print(f"Gender: {details['Gender']}")
                                    print(f"Birthday: {details['Birthday']}")
                                    print(f"Contact: {details['Contact']}")
                                    for service, service_details in details.items():
                                        if service not in ["Gender", "Birthday", "Contact"]:
                                            print(f"{service}: {"".join(str(item) for item in service_details)}")
                                    print()
                                option = int(input("Enter number to view customer, or 0 to return to main menu: "))
                                print()
                                if option in range(1, len(customerService_dict) + 1):
                                    name = list(customerService_dict.keys())[option - 1]
                                    details = customerService_dict[name]
                                    print(f"Name: {name}")
                                    print(f"Gender: {details['Gender']}")
                                    print(f"Birthday: {details['Birthday']}")
                                    print(f"Contact: {details['Contact']}")
                                    for service, service_details in details.items():
                                        if service not in ["Gender", "Birthday", "Contact", "Loyalty Point"]:
                                            print(f"{service}: {''.join(str(item) for item in service_details)}")
                                    # To update the customer information or not
                                    while True:
                                        choice = input("Do you want to update？(yes/no): ")
                                        if choice.lower() == 'yes':
                                            service = input("Enter the which one you want to update: ")
                                            if service in details:
                                                print(service, details[service])
                                                new_value = input("Enter the update things: ")
                                                details[service] = new_value
                                                print(service, details[service])
                                                print("Update successfully saved")
                                            else:
                                                print("Invalid choice")
                                        elif choice.lower() == 'no':
                                            break
                                        else:
                                            print("Invalid choice! Please enter yes or no")
                                elif option == 0:
                                    continue
                                # To identify the user's input
                                else:
                                    print("Invalid choice!")
                            # Function 2.e
                            case "e":
                                break
                # Function 3
                elif option == 3:
                    print(" 1.See total order amount by month\n 2.See top 10 customers")
                    additionalOption = int(input("Enter option: "))
                    # Monthly sales
                    if additionalOption == 1:
                        print("The total order amount by month: " + "$" + str(sum(additionalTotal)))
                        print()
                    # Top 10 customer
                    elif additionalOption == 2:
                        sorted_items = sorted(customerService_dict.items(), key=lambda x: int(x[1]["Loyalty Point"]),
                                              reverse=True)
                        for name, details in sorted_items[0: 10]:
                            print(f"Name: {name}, Loyalty Point: {details['Loyalty Point']}")
                        print()
                elif option == 0:
                    print("Exit")
                    break
        else:
            print("You company code is wrong")
# Staff
elif position == "Staff":
    while p == 0:
        # Display the function that the staff can use
        print(" a.Create order\n", "d.View customer\n", "e.Exit")
        # Input the staff chose
        option = input("Enter option: ")
        # Match the function the user choose
        match option:
            # Function a
            case "a":
                input_name = input("Enter the name you want to search or enter 0 to back to main menu:")
                # Identify the name in the customer information file
                matching_names = [name for name in customerService_dict.keys() if
                                  input_name.lower() in name.lower()]
                # If the name in the file
                if matching_names:
                    print("Name list：")
                    for i, name in enumerate(matching_names, 1):
                        print(f"{i}. {name}")
                    choice_index = int(input("Enter the number you choose：")) - 1
                    while True:
                        # Display the function of a
                        functionChoice = int(input("1) Use Service\n2) Buy Package\n3) Buy product\n"
                                                   "4) Back to main menu\nEnter your choice: "))
                        # Function a.1
                        if functionChoice == 1:
                            itemName = "Service"
                            chosen_name = matching_names[choice_index]
                            for item in listA:
                                print(f"{item[0]},{item[1]},{item[2]}")
                            input_service = input("Enter the item code you choose：")
                            if input_service in customerService_dict[chosen_name]:
                                print("You have", customerService_dict[chosen_name][input_service][0],
                                      ": ",
                                      customerService_dict[chosen_name][input_service][1],
                                      customerService_dict[chosen_name][input_service][2])
                                if customerService_dict[chosen_name][input_service][1] > 0:
                                    print(
                                        "Quantity will be deducted automatically when order is complete")
                                    thing = customerService_dict[chosen_name][input_service][0]
                                    itemCode = input_service
                                    itemPrice = 0
                                    order.append((itemName, thing, itemCode, itemPrice))

                                else:
                                    print("You don't have enough service time to use")
                                    thing = customerService_dict[chosen_name][input_service][0]
                                    itemCode = input_service
                                    itemPrice = int(
                                        input("Enter the retail price of the service you choose"))
                                    order.append((itemName, thing, itemCode, itemPrice))
                                customerService_dict[chosen_name][input_service][1] -= 1
                                if customerService_dict[chosen_name][input_service][1] == 0:
                                    del (customerService_dict[chosen_name][input_service])
                            # Customer don't have enough time to use
                            else:
                                print("You don't have enough service times")
                                thing = input("Enter the service name ")
                                a = int(input("Enter the retail price of the service you choose "))
                                itemPrice = a
                                itemCode = input_service
                                order.append((itemName, thing, itemCode, itemPrice))
                            customerOption = input("Do want to continue ordering, or complete order? ")
                            # Continue ordering or complete order
                            if customerOption != "continue":
                                # Calling function
                                process_order(matching_names, choice_index, order, customerService_dict,
                                              numberID)
                                numberID += 1
                                order = []
                                break
                        # Function a.2
                        elif functionChoice == 2:
                            chosen_name = matching_names[choice_index]
                            for item in listB:
                                print(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}")
                            choice = input("Which package you want to buy? ")
                            itemName = "Package"
                            if choice == "PK001":
                                thing = "Express Package"
                                itemCode = "PK001"
                                itemPrice = 620
                                customerService_dict[chosen_name]["SV001"] = [
                                    "30 min Express Face treatment", 10,
                                    "left"]
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "PK002":
                                thing = "Express Package"
                                itemCode = "PK002"
                                itemPrice = 1200
                                customerService_dict[chosen_name]["SV001"] = [
                                    "30 min Express Face treatment", 20,
                                    "left"]
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "PK003":
                                thing = "Face Cleansing"
                                itemCode = "PK003"
                                itemPrice = 1125
                                customerService_dict[chosen_name]["SV002"] = ["Face Cleansing", 10,
                                                                              "left"]
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "PK004":
                                thing = "Deep Face Cleansing"
                                itemCode = "PK004"
                                itemPrice = 1600
                                customerService_dict[chosen_name]["SV003"] = ["Deep Face Cleansing", 10,
                                                                              "left"]
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "PK005":
                                thing = "Laser Face treatment"
                                itemCode = "PK005"
                                itemPrice = 1290
                                customerService_dict[chosen_name]["SV004"] = ["Laser Face treatment", 6,
                                                                              "left"]
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "PK006":
                                thing = "Full rejuvenation"
                                itemCode = "PK006"
                                itemPrice = 1560
                                customerService_dict[chosen_name]["SV005"] = [
                                    "Full rejuvenation treatment", 6, "left"]
                                order.append((itemName, thing, itemCode, itemPrice))
                            else:
                                thing = input("Package name: ")
                                itemCode = choice
                                itemPrice = int(input("Package price: "))
                                order.append((itemName, thing, itemCode, itemPrice))
                            customerOption = input("Do want to continue ordering, or complete order? ")

                            if customerOption != "continue":
                                # Calling function
                                process_order(matching_names, choice_index, order, customerService_dict,
                                              numberID)
                                numberID += 1
                                order = []
                                break
                        # Function a.3
                        elif functionChoice == 3:
                            for item in listC:
                                print(f"{item[0]},{item[1]},{item[2]},{item[3]}")
                            choice = input("Which package you want to buy? ")
                            itemName = "Product"
                            if choice == "P001":
                                thing = "Whitening cream"
                                itemCode = "P001"
                                itemPrice = 128
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "P002":
                                thing = "Eye cream"
                                itemCode = "P002"
                                itemPrice = 90
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "P003":
                                thing = "Facelift cream"
                                itemCode = "P003"
                                itemPrice = 188
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "P004":
                                thing = "Eye mask"
                                itemCode = "P004"
                                itemPrice = 60
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "P005":
                                thing = "Cleanser"
                                itemCode = "P005"
                                itemPrice = 65
                                order.append((itemName, thing, itemCode, itemPrice))
                            elif choice == "P006":
                                thing = "Anti aging serum"
                                itemCode = "P006"
                                itemPrice = 168
                                order.append((itemName, thing, itemCode, itemPrice))
                            else:
                                thing = input("Product name: ")
                                itemCode = choice
                                itemPrice = int(input("Product price: "))
                                order.append((itemName, thing, itemCode, itemPrice))

                            customerOption = input("Do want to continue ordering, or complete order? ")

                            if customerOption != "continue":
                                # Calling function
                                process_order(matching_names, choice_index, order, customerService_dict,
                                              numberID)
                                numberID += 1
                                order = []
                                break
                        # Function a.4
                        elif functionChoice == 4:
                            break

                elif input_name == "0":
                    print()
                else:
                    print("No such name you search")
            # Function d
            case "d":
                for name, details in customerService_dict.items():
                    print(f"Name: {name}")
                    print(f"Gender: {details['Gender']}")
                    print(f"Birthday: {details['Birthday']}")
                    print(f"Contact: {details['Contact']}")
                    for service, service_details in details.items():
                        if service not in ["Gender", "Birthday", "Contact"]:
                            print(f"{service}: {', '.join(str(item) for item in service_details)}")
                    print()
                option = int(input("Enter number to view customer, or 0 to return to main menu: "))
                print()
                if option in range(1, len(customerService_dict) + 1):
                    name = list(customerService_dict.keys())[option - 1]
                    details = customerService_dict[name]
                    print(f"Name: {name}")
                    print(f"Gender: {details['Gender']}")
                    print(f"Birthday: {details['Birthday']}")
                    print(f"Contact: {details['Contact']}")
                    for service, service_details in details.items():
                        if service not in ["Gender", "Birthday", "Contact"]:
                            print(f"{service}: {', '.join(str(item) for item in service_details)}")
                    # To update customer information or not
                    while True:
                        choice = input("Do you want to update？(yes/no): ")
                        if choice.lower() == 'yes':
                            service = input("Enter the which one you want to update: ")
                            if service in details:
                                print(service, details[service])
                                new_value = input("Enter the update things: ")
                                details[service] = new_value
                                print(service, details[service])
                                print("Update successfully saved")
                            else:
                                print("Invalid choice")
                        elif choice.lower() == 'no':
                            break
                        else:
                            print("Invalid choice! Please enter yes or no")
                else:
                    print("Invalid choice!")
            case "e":
                break
# Additional function (stored the information)
with open("listA.txt", 'w', encoding='utf-8') as file:
    for item in listA:
        file.write(f"{item[0]},{item[1]},{item[2]}\n")
with open("listB.txt", 'w', encoding='utf-8') as file:
    for item in listB:
        file.write(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}\n")
with open("listC.txt", 'w', encoding='utf-8') as file:
    for item in listC:
        file.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")
with open("customer information.txt", 'w', encoding='utf-8') as file:
    for customer_name, customer_info in customerService_dict.items():
        file.write("Customer Name: " + customer_name + "\n")
        file.write("Gender: " + customer_info["Gender"] + "\n")
        file.write("Birthday: " + customer_info["Birthday"] + "\n")
        file.write("Contact: " + customer_info["Contact"] + "\n")
        for service_code, service_details in customer_info.items():
            if service_code not in ["Gender", "Birthday", "Contact", "Loyalty Point"]:
                file.write("Service: " + service_code + "\t")
                file.write("Details: " + service_details[0] + "\t")
                file.write("Quantity Left: " + str(service_details[1]) + "\n")
        file.write("Loyalty Point: " + str(customer_info["Loyalty Point"]) + "\n" + "\n")
