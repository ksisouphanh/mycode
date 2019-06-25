#!/usr/bin/env python3
##if elif else

choice  = int(input("Enter Channel Number: "))

def channel_sorter(chan):
    if chan > 0 and chan <11:
        print("Basic Package")
    elif chan > 10 and chan <51:
        print("Premium Package")
    elif chan > 50 and chan <300:
        print("Extras Package")
    else:
        print("Not a Valid Channel, please try again")

channel_sorter(choice)
