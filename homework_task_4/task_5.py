"""
5-
The list of names is given: names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
Using the continue statement, print only the correct names to the console
"""

list_of_names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for name in list_of_names:
    if not isinstance(name, str):
        continue
    print(name)