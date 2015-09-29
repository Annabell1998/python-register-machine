import sys
import os
from decimal import Decimal
article = {}
inventory = {}
print "WELCOME TO THE REGISTER MASHINE"
def menu():
    print """
      please select an option:
      1. Add item
      2. Sell articles
      3.Exit/Quit\n"""
    selection =raw_input("enter your option: ")
    if selection == "1":
        os.system("clear")
        Add()
    elif selection == "2":
        os.system("clear")
        Sell()
    elif selection == "3":
        os.system("clear") 
        print"\nGood bye, thank you for visiting\n"
        sys.exit()
def Add():
    again = True
    while again == True:
        item = raw_input("Enter the item that you want to add: ")
        if item.isalpha():
          break
        else:
          print " esta malo pendejo"
    price = ""
    while price == "":
        try:
            price = float(raw_input("Enter the price: "))
            unit = float(raw_input("Enter the units that exist: "))
            print item, price
            article[item] = price
            inventory[item] = unit
            print article
            print "Your item was added"
        except ValueError :
            print "You need enter a value"
            price = ""
    another = ""
    while another == "":
        another = raw_input("Do you want to enter another item?  Y/N: ")
        another = another.lower()
        if another  == "y":
            Add()
        elif another == "n":
            again = False
            menu()
        else: 
            print "Remember, enter Y/N"
            another = ""
def Sell():
    if article == {}:
        print "You have not enter items"
        Add()
    else: 
        for i in article:
            print "article: ", i 
            print "price: ", article[i]
            print "unit: ", Decimal(inventory[i])
        article2 = []
        count1 = ""
        total = 0
        count1 = count1.lower()
        while count1 != "n" :
          item_sell= raw_input("enter the item you want to sell: ")
          article2.append(item_sell)
          print article2
          count1=raw_input("Do you want to enter another item to sell? Y/N: ")
          if count1 == "Y" :
            count1 != "N"
          elif count1 == "n":
            Done = raw_input("\nIf you want to go to the bill enter 'done', if you want to enter another item to sell enter 'other': ")
            Done = Done.lower()
            if Done == "done":
                print "================================="
                print "item", " |  price"  ," | quantity"
                print "================================="
                for i in article:
                  repeat = article2.count(i) 
                  sell = article[i] * repeat
                  total += sell
                  print i,"   ",article[i],"     *",repeat 
                print "the total price is: " + str(total)
                menu()
            elif Done == "other":
                count1 != "n"
          else: 
            print "Remember, enter Y/N"
            count1 != "N"
def Cards():
    pass  

menu()


