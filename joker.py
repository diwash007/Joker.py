""" joker package """
import random
from jokes import joke_list, pun_list


class Joker:
    """Joker class
        joke() -> returns a random joke
        jokes(n) -> returns a list of n jokes
        pun() -> returns a random joke
        puns(n) -> returns a list of n jokes
    """
    def joke(self) -> str:
        """ returns a random joke """
        return random.choice(joke_list)

    def jokes(self, num:int = 10) -> list:
        """ returns a list of n jokes """
        random.shuffle(joke_list)
        return joke_list[0:num]

    def pun(self) -> str:
        """ returns a random pun """
        return random.choice(pun_list)

    def puns(self, num:int = 10) -> list:
        """ returns a list of n puns """
        random.shuffle(pun_list)
        return pun_list[0:num]
