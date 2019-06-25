#!/usr/bin/env python3
"""using cvs data"""
import csv

def main():
    # open the csv data set
    with open("vendor.csv", "r") as vendorfile:
        vendata = csv.reader(vendorfile, delimiter=",")
        # the csv data is now nicely preapred
        #each new row is a python list
        #we can reference the items we want to print
        # as we loop over th e data
        for row in vendata:
            print("The IP address " + row[2] + " requires the driver " + row[3])


main()
