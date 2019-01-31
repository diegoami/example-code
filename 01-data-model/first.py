from frenchdeck import FrenchDeck, Card

beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))
print(deck[:3])
print(deck[12::13])
print(Card('Q', 'hearts') in deck)
print(Card('Z', 'clubs') in deck)
for card in deck:  # doctest: +ELLIPSIS
    print(card)

for card in reversed(deck):  # doctest: +ELLIPSIS
    print(card)
for n, card in enumerate(deck, 1):  # doctest: +ELLIPSIS
    print(n, card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

print(spades_high(Card('2', 'clubs')))
print(spades_high(Card('A', 'spades')))
for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
    print(card)

