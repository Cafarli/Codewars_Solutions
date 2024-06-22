"""
You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

Given the following input array:

list1 = [  
  { "first_name": "Nikau", "last_name": "R.", "contry": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" },
  { "first_name": "Precious", "last_name": "G.", "contry": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
  { "first_name": "Maria", "last_name": "S.", "contry": "Peru", "continent": "Americas", "age": 30, "language": "C" },
  { "first_name": "Agustin", "last_name": "V.", "contry": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" }
]
Write a function that returns the array sorted alphabetically by the programming language. In case there are some developers that code in the same language,
sort them alphabetically by the first name:

[ 
  { "first_name": "Maria", "last_name": "S.", "contry": "Peru", "continent": "Americas", "age": 30, "language": "C" },
  { "first_name": "Agustin", "last_name": "V.", "contry": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" },
  { "first_name": "Precious", "last_name": "G.", "contry": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
  { "first_name": "Nikau", "last_name": "R.", "contry": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" }
]
Notes:

The input array will always be valid and formatted as in the example above.
The array does not include developers coding in the same language and sharing the same name.
"""

def sort_by_language(arr):
    return sorted(arr, key = lambda k: (k['language'], k['first_name']))
