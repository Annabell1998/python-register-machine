import sys
import os
from decimal import Decimal
article = {}
print "WELCOME TO THE 'CHOCO CHAVO'S' STORE"
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
        print"\nGood bye, thank you for buy with us\n"
        sys.exit()
    else: 
        print "Enter a number from 1 to 3"
        os.system("clear")
        menu()
def Add():
    again = True
    while again == True:
        item = raw_input("Enter the item that you want to add: ")
        if item.isalpha():
          break
        else:
          print "just words please"
    price = ""
    while price == "":
        try:
            price = float(raw_input("Enter the price: "))
            print item, price
            article[item] = price
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
            os.system("clear")
            Add()
        elif another == "n":
            again = False
            os.system("clear")
            menu()
        else: 
            print "Remember, enter Y/N"
            another = ""
Discount = 0
def Sell():
    if article == {}:
        print "You have not enter items"
        Add()
    else: 
        for i in article:
            print "article: ", i 
            print "price: ", article[i]
        article2 = []
        No_total = 0
        while True :
            print """if you have a card enter Gold or Silver
and if you want go to the bill enter DONE"""
            item_sell= raw_input("enter the item you want to sell: ")
            article2.append(item_sell)
            print article2
            if item_sell == "done":
                item_sell = "done"
            else: 
                card = cards(item_sell, Discount,article2)
            if item_sell == "done" or item_sell == "DONE" or item_sell == "Done":
                print "================================="
                print "item", " |  price"  ," | quantity"
                print "================================="
                for i in article:
                    repeat = article2.count(i) 
                    sell = article[i] * repeat
                    No_total += sell
                    iva = No_total * 0.12 
                    total_iva = No_total + iva
                    #card = cards(item_sell, Discount)
                    #b = raw_input("salimos de cards")
                    total_card = card * total_iva 
                    total = total_iva - total_card 
                    if repeat >= 1:
                        print i,"   ","%.2f" % (article[i]),"     *",repeat
                print "the IVA is: " + "%.2f" % (iva)
                print "the total price whithout IVA is: $" "%.2f" % (No_total)
                print "the total price whith IVA is: $" + "%.2f" % (total_iva)
                print card
                if card == 0: 
                    print "You don't have a card"
                else: 
                    print "The total with card descount is: $" + "%.2f" % (total)
                pay = float(raw_input("pay with: "))
                change = pay - total
                print "the change is: $" + "%.2f" % (change)
                menu() 
def cards(item_sell, Discount,article2):
    for i in article2: 
        if i == "gold" or i == "GOLD" or i == "Gold":
            Discount = 0.05 
        elif i == "silver" or i == "SILVER" or i == "Silver":
            Discount = 0.02
        if (i == "gold" or i == "GOLD" or i == "Gold") and (i == "silver" or i == "SILVER" or i == "silver"):
            Discount = 0.05

    return Discount
menu()