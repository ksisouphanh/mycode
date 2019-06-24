# Working with lists
first_list = ["eggs", "bacon", "milk", "butter", "bread", "cheddar", 5, 2.75]
# identify - 
print(first_list)

#specify butter only
print(first_list[3])

#specifiy two items butter and cheddar
print(first_list[3], first_list[5])


#print I need to get eggs, bacon, milk butter, bread, and cheddar before 5. It will be more than 2.75

#print(f"{first_list[0]}, {first_list[1]}...")
#print(f"...{first_list[0]}, {first_list[1]}...")
print("I need to get {}, {},i {}, {}, {}, and {} before {}. It will be more than ${}".format(*first_list))


new_list = ["cat", "dog", "hamster"]
new_list.append("squirrel")
print(new_list)
new_list.insert(1, "marmot")
print(new_list)
new_list[1] = "weasel"

new_list.append(first_list)
print(new_list)
print(new_list[5])
inner = new_list[5]
print(inner[3])
print(new_list[5][3])

for_realz = ["sasquatch", "yeti", "bigfoot"]
new_list.extend(for_realz)
print(new_list)
