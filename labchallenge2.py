#Lab Challenge 2
#Use the list to print out the following:
#I need to access IP's 10.10.10.25, 10.20.30.40, and 10.10.24.47

my_list = ["10.10.10.25", "10.10.24.47", "10.20.30.40"]
print(f"I need to access IP's {my_list[0]}, {my_list[2]}, and {my_list[1]}")

print("I need to access IP's {0}, {2}, and {1}".format(*my_list))
