#definitions
example = {"key" : "value"}
cars = {"rental" : "sentra", "real": "soul"}
print(cars ["rental"])
print(cars ["rental"], cars["real"])

#update is to add in def
cars.update({"dream": "ferrari"})
#assigning
cars["truck"] = "F650"
print(cars)
pets = {"cat": "meow", "dog": "woof"}
cars.update(pets)
print(cars)
#specifiying list in definition
#print (cars["trucks"][2])
