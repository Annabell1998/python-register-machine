from datetime import *
import sys
import os
from decimal import Decimal
article = {}
print"=========================================================================================="
print "\t\t\t\tWELCOME TO THE 'CHOCO CHAVO'S' STORE"
print"=========================================================================================="
def menu():
    print """
        please select an option:
        
        1. Add item
        2. Sell articles
        3.Exit/Quit\n"""
    selection = raw_input("       enter your option: ")
    if selection == "1":
        os.system("clear")
        Add()
    elif selection == "2":
        os.system("clear")
        Sell()
    elif selection == "3":
        os.system("clear")
        print"\n*********Good bye, thank you for buy with us******"
        print "  ****************Comeback soon*****************"
        print "    ******P.S. CHOCO CHAVO'S STORE*****"
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
            print "_______ARTICLE____PRICE____________"
            print "       ", item, "   ", price
            print "___________________________________"
            article[item] = price
            print "Your item was added"
        except ValueError:
            print "You need enter a value"
            price = ""
    another = ""
    while another == "":
        another = raw_input("Do you want to enter another item?  Y/N: ")
        another = another.lower()
        if another == "y":
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
            print"______ARTICLES_THAT_EXISTS_____"
            print "article: ", i
            print "price: ", article[i]
            print "______________________________"
        article2 = []
        No_total = 0
        while True:
            print """if you have a card enter Gold or Silver
and if you want go to the bill enter DONE"""
            item_sell = raw_input("enter the item you want to sell: ")
            article2.append(item_sell)
            print "you have in your car shop"
            print " ".join(article2)
            if item_sell == "done":
                item_sell = "done"
            else:
                card = cards(item_sell, Discount, article2)
            if item_sell == "done" or item_sell == "DONE" or item_sell == "Done":
                os.system("clear")
                print "\t\t\t CHOCO CHAVO'S STORE"
                print "   today :", datetime.today()
                name = raw_input("   client name: ")
                nit = raw_input("   client NIT: ")
                print "========================================="
                print "item", "   |    price", " |    quantity"
                print "========================================="
                for i in article:
                    repeat = article2.count(i)
                    sell = article[i]*repeat
                    No_total += sell
                    iva = No_total*0.12
                    total_iva = No_total+iva
                    #card = cards(item_sell, Discount)
                    #b = raw_input("salimos de cards")
                    total_card = card*total_iva
                    total = total_iva-total_card
                    if repeat >= 1:
                        print i, "      ", "%.2f" % (article[i]), "  *    ", repeat
                print "-------------------------------------------"
                print "the IVA is: " + "%.2f" % (iva)
                print "-------------------------------------------"
                print "the total price whithout IVA is: $" "%.2f" % (No_total)
                print "-------------------------------------------"
                print "the total price whith IVA is: $"+"%.2f" % (total_iva)
                print "-------------------------------------------"
                if card == 0:
                    print "You don't have a card"
                else:
                    print "your descount with your card is %", card 
                    print "The total with card descount is: $"+"%.2f" % (total)
                    print "-----------------------------------------"
                pay = float(raw_input("pay with: "))
                change = pay - total
                print "the change is: $"+"%.2f" % (change)
                print"\n*********Good bye, thank you for buy with us******"
                print "  ***************Comeback soon*****************"
                print "     ******P.S. CHOCO CHAVO'S STORE*****"
                menu()
def cards(item_sell, Discount,article2):
    if "gold" in article2 or "GOLD" in article2 or "Gold" in article2:
        Discount = 0.05
    elif "Silver" in article2 or"silver" in article2 or "SILVER" in article2:
        Discount = 0.05
    elif ("silver" in article2 or "SILVER" in article2 or "Silver" in article2) and ("gold" in article2 or "GOLD" in article2 or "Gold" in article2):
        Discount = 0.02
    return Discount
menu()