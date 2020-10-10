import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame()
        self.card = Card("Hearts", 1)
        self.card1 = Card("Clubs", 6)
        self.card2 = Card("Hearts", 5)
        self.card3 = Card("Spades", 8)
        self.cards = [self.card1, self.card2, self.card3]
        
    
    def test_check_for_ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card))

    def test_check_for_highest_card(self):
        self.assertEqual (6, self.cardgame.highest_card(self.card1, self.card2))

    def test_for_cards_total(self):
        self.assertEqual("You have a total of 19", self.cardgame.cards_total(self.cards))

