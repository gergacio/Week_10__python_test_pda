import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame:
    def setUp(self):
        self.card = Card("Spade", 1)
        self.card1 = Card("Heart", 2)
        self.card2 = Card("Club", 3)
        self.card3 = Card("Diamond", 4)
        self.card_game = CardGame()

    def test_check_for_ace_true(self):
        self.card_game.check_for_ace(self.card)
        self.assertEqual(True, self.card.value == 1)

    def test_check_for_ace_false(self):
        self.card_game.check_for_ace(self.card)
        self.assertEqual(False, self.card.value == 10)

    def test_check_for_highest_card_first_card_higher(self):
        self.assertEqual(
            self.card2, self.card_game.highest_card(self.card1, self.card2)
        )

    def test_check_for_highest_card_last_card_higher(self):
        self.assertEqual(
            self.card3, self.card_game.highest_card(self.card2, self.card3)
        )

    def test_cards_total(self):
        cards = [self.card, self.card1, self.card2, self.card3]
        self.assertEqual("You have a total of 10", self.card_game.cards_total(cards))