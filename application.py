"""if you want to buy something you have to enter the items you want to sell so
that you can fill yor inventory then its you enter the items you want to buy and you
decide if you want to buy with a gold card or a silver card if you enter each of them you
will have a descount and then the machine will make your invoice"""
import sys
import os
ARTICLE = {}
DISCOUNT = 0
print"=========================================================================================="
print "\t\t\t\tWELCOME TO THE 'CHOCO CHAVO'S' STORE"
print"=========================================================================================="
def menu():
    """This function is use to choose your option"""
    print """
        please select an option:
        
        1. Add item
        2. Sell articles
        3. Exit/Quit\n"""
    selection = raw_input("       enter your option: ")
    if selection == "1":
        os.system("reset")
        add()
    elif selection == "2":
        os.system("reset")
        sell()
    elif selection == "3":
        os.system("reset")
        print"\n*********Good bye, thank you for buy with us******"
        print "  ****************Comeback soon*****************"
        print "    ******P.S. CHOCO CHAVO'S STORE*****"
        sys.exit()
    else:
        print "Enter a number from 1 to 3"
        os.system("reset")
        menu()
def add():
    """This Fuction ask the user a item and the price that itmen, then save the information"""
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
            print "       ", item, "   ", "%.2f" % (price)
            print "___________________________________"
            ARTICLE[item] = price
            print "Your item was added"
        except ValueError:
            print "You need enter a value"
            price = ""
    another = ""
    while another == "":
        another = raw_input("Do you want to enter another item?  Y/N: ")
        another = another.lower()
        if another == "y":
            os.system("reset")
            add()
        elif another == "n":
            again = False
            os.system("reset")
            menu()
        else:
            print "Remember, enter Y/N"
            another = ""

def sell():
    LIST = []
    """this Fuction ask the user the itemas that he want buy and then print a bill"""
    if ARTICLE == {}:
        print "You have not enter items"
        add()
    else:
        print"______ARTICLES_THAT_EXISTS_____"
        for i in ARTICLE:
            print "article: ", i
            print "price: ", "%.2f" % (ARTICLE[i])
        print "______________________________"
        article2 = []
        nototal = 0
        Sell2 = True
        while  Sell2 == True:
            print """if you have a card enter Gold or Silver
and if you want go to the bill enter DONE"""
            item_sell = raw_input("enter the item you want to sell: ")
            article2.append(item_sell)
            if ( item_sell == "silver" or item_sell == "SILVER" or  item_sell == "Silver")\
    or (item_sell == "gold" or item_sell == "GOLD" or  item_sell == "Gold"):
                print "\nYou have selected a Card\n"
            elif item_sell in ARTICLE :
                    LIST.append(item_sell)
                    print "\nyou have in your car shop"
                    print ",".join(LIST)
                    print ""
            else: 
                print "that item don't exists"
                Sell2 = True
            def bill(item_sell, nototal):
                """ this fuction print the bill"""
                if item_sell == "done" or item_sell == "DONE" or item_sell == "Done":
                    item_sell = "done"
                else:
                    card = cards(DISCOUNT, article2)
                card = cards(DISCOUNT, article2)
                if item_sell == "done" or item_sell == "DONE" or item_sell == "Done":
                    os.system("reset")
                    print "\t\t\t CHOCO CHAVO'S STORE"
                    thename = raw_input("   client name: ")
                    thenit = raw_input("   client NIT: ")
                    print "========================================="
                    print "item", "   |    price", " |    quantity"
                    print "========================================="
                    for i in ARTICLE:
                        repeat = article2.count(i)
                        sell1 = ARTICLE[i]*repeat
                        nototal += sell1
                        iva = nototal*0.12
                        total_iva = nototal + iva
                        total_card = card*total_iva
                        total = total_iva-total_card
                        if repeat >= 1:
                            print i, "      ", "%.2f" % (ARTICLE[i]), "  *    ", repeat
                    print "-------------------------------------------"
                    print "the IVA is: " + "%.2f" % (iva)
                    print "-------------------------------------------"
                    print "the total price whithout IVA is: $" "%.2f" % (nototal)
                    print "-------------------------------------------"
                    print "the total price whith IVA is: $"+"%.2f" % (total_iva)
                    print "-------------------------------------------"
                    if card == 0:
                        print "You don't have a card"
                    else:
                        print "your descount with your card is %", card
                        print "The total with card descount is: $"+"%.2f" % (total)
                        print "-----------------------------------------"
                    while True:
                        try:
                            pay = float(raw_input("cash: "))
                            change = pay - total
                            if change < 0:
                                print "isn't enough"

                            else:
                                print "the change is: $"+"%.2f" % (change)
                                print "the NIT:", thenit
                                print"\n*********Good bye, thank you %s for buy with us******" % (thename)
                                print "  ***************Comeback soon*****************"
                                print "     ******P.S. CHOCO CHAVO'S STORE*****"
                                menu()
                        except ValueError:
                            print "need money"

            bill(item_sell, nototal)
def cards(discount, article2):
    """make a sentence that cards if is gold make a descount of 0.05+"""
    if "gold" in article2 or "GOLD" in article2 or "Gold" in article2:
        discount = 0.05
    elif "Silver" in article2 or"silver" in article2 or "SILVER" in article2:
        discount = 0.02
    elif ("silver" in article2 or "SILVER" in article2 or "Silver" in article2)\
    and ("gold" in article2 or "GOLD" in article2 or "Gold" in article2):
        discount = 0.05
    return discount
menu()
