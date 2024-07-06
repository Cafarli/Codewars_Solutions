"""
A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards in the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original top card is still on top.

For example, faro shuffling the list

['ace', 'two', 'three', 'four', 'five', 'six']
gives

['ace', 'four', 'two', 'five', 'three', 'six' ]
If 8 perfect faro shuffles are performed on a deck of 52 playing cards, the deck is restored to its original order.

Write a function that takes an integer n and returns an integer representing the number of faro shuffles it takes to restore a deck of n cards to its original order.

Assume n is an even number between 2 and 2000.
"""

def faro_cycles(n):
    deck = list(range(n))
    original_deck = list(range(n))
    cnt = 0
    
    while True:
        new_deck = []
        for i in range(n // 2):
            new_deck.append(deck[i])
            new_deck.append(deck[i + n // 2])
        
        deck = new_deck
        cnt += 1
        
        if deck == original_deck:
            return cnt

