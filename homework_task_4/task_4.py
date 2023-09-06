"""
4 - You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist. 
Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.
"""

casino_blacklist  = {"John Dow", "Alice Smith", "Bob Johnson", "Mary Brown", "Eva Davis"}
poker_blacklist = {"Michael Johnson", "Alice Smith", "David Lee", "Linda Harris", "Jennifer Clark"}
alcohol_blacklist = {"Robert Davis", "Alice Smith", "Daniel Moore", "Olivia Johnson", "William Smith"}
all_black_list = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
for person in all_black_list:
    print(person)

