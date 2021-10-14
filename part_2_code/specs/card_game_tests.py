import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("club", 1)
        self.card2 = Card("heart", 8)
        self.card3 = Card('diamond', 9)
        self.card_game1 = CardGame()

        self.cards = [self.card1, self.card2, self.card3]
    
    def test_card_has_suit(self):
        self.assertEqual("club", self.card1.suit)

    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game1.check_for_ace(self.card1))
        
    def test_highest_card(self):
        self.assertEqual(self.card2, self.card_game1.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual(18, self.card_game1.cards_total(self.cards))