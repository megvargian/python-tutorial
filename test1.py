x = 100

if x == 5 and type(x) is int:
	print("x is 5 and is an integer");
	print(x);
elif x == 10 and type(x) is int:
	print("x is an integer but it is not equal to 5")

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
for each_vendor in vendors:
	print(each_vendor)

my_string = "Cisco"

for letter in my_string:
	print(letter)
	print(letter * 2)
	print(letter * 3)

for element in vendors:
	print(element)
else:
	print("The end of the list has been reached")