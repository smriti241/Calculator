#Bussiness Logic Layer


import sys
c_id = []
c_name = []
c_address = []
c_mob = []


def add():
    identity = int(input("Enter customer's id: "))
    c_id.append(identity)
    name = input("Enter customer's name:")
    c_name.append(name)
    address = input("Enter customer's address:")
    c_address.append(address)
    mobile = input("Enter customer's mobile number:")
    c_mob.append(mobile)


def delete():
    identity = int(input("Enter the customer id to be deleted:"))
    if c_id.__contains__(identity):
        n = c_id.index(identity)
        c_id.pop(n)
        c_mob.pop(n)
        c_address.pop(n)
        c_name.pop(n)
    else:
        print("Customer not found.")


def showall():
    for i in range(len(c_id)):
        print(i + 1, " CUSTOMER ==>")
        print("Id:", c_id[i])
        print("Name:", c_name[i])
        print("Address:", c_address[i])
        print("Mobile number:", c_mob[i])
        print()


def search():
    identity = int(input("Enter the customer id to be searched:"))
    if c_id.__contains__(identity):
        n = c_id.index(identity)
        print(c_name[n], " is the name of customer,\n", c_mob[n], " is the mobile number and")
        print(c_address[n], " is the address.")
    else:
        print("Customer not found!!!")


def update():
    identity = int(input("Enter the customer id to be updated:"))
    if c_id.__contains__(identity):
        n = c_id.index(identity)
        name = input("Enter customer's name:")
        address = input("Enter customer's address:")
        mobile = input("Enter customer's mobile number:")
        c_name.insert(n, name)
        c_address.insert(n, address)
        c_mob.insert(n, mobile)
    else:
        print("Customer not found!!!")


# Presentation Layer


print("***\tCUSTOMER \t MANAGEMENT \t SYSTEM\t***")
print("1 for adding a customer's details, \n"
      "2 for deleting a customer's details,\n"
      "3 for modifications, \n"
      "4 for searching, \n"
      "5 for show all customers, \n"
      "6 for exit.\n")
while True:
    n = int(input())
    if n == 1:
        add()
    elif n == 2:
        delete()
    elif n == 3:
        update()
    elif n == 4:
        search()
    elif n == 5:
        showall()
    elif n == 6:
        sys.exit()
    else:
        print("Invalid input ")
