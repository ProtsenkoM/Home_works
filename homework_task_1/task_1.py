
john_salary = 1.500
marta_salary = 2.500
john_age = 24
marta_age = 35
john_name = "John"
marta_name = "Marta"
john_gender = False
marta_gender = True
john_friends = ["Bill", "Anna", "Alex", "Bill"]
marta_friends = ["Max","Peter","Yana", "Mike"] 
test_list_of_names = ["Max","Peter","Yana", "Mike", "Bill", "Anna", "Alex", "Bill"]


print (f'Name of user 1 - {marta_name}, \nage = {marta_age},\nsalary = {marta_salary:.3f},\ngender = {marta_gender},\nlist of friends {marta_friends}\n')
print (f'Name of user 2 - {john_name}, \nage ={john_age}, \nsalary = {john_salary:.3f}, \ngender = {john_gender}, \nlist of friends {john_friends}\n')
print (f'List of users without dublicates {set(test_list_of_names)}')