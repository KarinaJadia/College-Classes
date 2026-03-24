from Cards import Card, Deck, Hand
import unittest

class TestCard(unittest.TestCase):
    def test_init(self):
        c1 = Card(4, 'hearts') # smallest
        c2 = Card(2, 'spades') # middle
        c3 = Card(3, 'spades') # largest

        # testing getVal()
        assert c1.getVal() == 4 # true
        assert not(c2.getVal() == 4) # false
        
        # testing getSuit()
        assert c1.getSuit() == 'hearts' # true
        assert not(c3.getSuit() == 'clubs') # false

        # testing repr()
        assert c1.repr() == '4 of hearts' # true
        assert not(c1.repr()  == '3 of spades') # false
        
        # testing __lt__()
        assert c2 < c3 # true
        assert not(c2 < c1) # false

    class TestDeck(unittest.TestCase):
        d1 = Deck()
        d2 = Deck((1,2), ('hearts', 'clubs'))
        d3 = Deck((),())

        # testing __len__()
        assert len(d1) == 52
        assert len(d2) == 4

        # testing draw_top()
        assert d2.draw_top() == '2 of clubs' # true
        assert d3.draw_top() == 'error: cannot draw from empty deck' # true
        assert not(d2.draw_top() == '1 of hearts') # false

        # testing shuffle() (not using d2 because there are only 4 cards and it might still fail)
        d1.shuffle() # now it should be randomized
        assert not(d1.draw_top() == '13 of spades') # false
        
        # testing sort()
        d1.sort() # should now take 13 of spades
        assert d1.draw_top() == '13 of spades' # true

    class TestHand(unittest.TestCase):
        h1 = Hand((1, 2, 3), ('clubs', 'hearts'))
        h2 = Hand((1, 2), ('spades', 'diamonds'))

        # testing __repr()__
        assert str(h1) == 'hand: (1 of clubs) (2 of clubs) (3 of clubs) (1 of hearts) (2 of hearts) (3 of hearts) ' # true
        assert str(h2) == 'hand: (1 of spades) (2 of spades) (1 of diamonds) (2 of diamonds) ' # true

        # testing play()
        assert h1.play((Card(1, 'clubs'))) == '1 of clubs' # true
        assert h1.play((Card(1, 'clubs'))) == 'error: card does not exist' # true because I removed it
        assert not(h2.play((Card(1, 'clubs'))) == '1 of clubs') # false

unittest.main() 