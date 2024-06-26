"""
You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

Notes:

Each student will have a unique name
There will always be a clear winner: either one person has the most, or everyone has the same amount
If there is only one student, then that student has the most money
"""

def most_money(students):
    wallet = {}
    for i in students:
        wallet[i.name] = sum([i.fives*5, i.tens*10, i.twenties * 20])
    max_money = max(wallet.values())
    names = [name for name, money in wallet.items() if money == max_money]
    return names[0] if len(names)==1 else 'all'
