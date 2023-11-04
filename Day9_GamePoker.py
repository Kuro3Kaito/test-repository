import random


class Card(object):
    """Thẻ"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)
    
    def __repr__(self):
        return self.__str__()


class Poker(object):
    """một bộ bài"""

    def __init__(self):
        self._cards = [Card(suite, face) 
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """Xáo trộn (ngẫu nhiên)"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """Chia bài"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """Kiểm tra bài"""
        return self._current < len(self._cards)


class Player(object):
    """người chơi"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """Rút bài"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """Người chơi sắp xếp thẻ của họ"""
        self._cards_on_hand.sort(key=card_key)


# Quy tắc sắp xếp - sắp xếp theo chất trước rồi đến điểm
def get_key(card):
    return (card.suite, card.face)


def main():
    p = Poker()
    p.shuffle()
    players = [Player('A'), Player('B'), Player('C'), Player('D')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)


if __name__ == '__main__':
    main()