""" joker package """
import random
from jokes import jokes


class Joker:
    """
        class for joker
        joke() -> returns a random joke
        jokes(n) -> returns a list of n jokes
    """

    def joke(self) -> str:
        """ returns a random joke """
        return random.choice(jokes)

    def jokes(self, num: int) -> list:
        """ returns a list of n jokes """
        random.shuffle(jokes)
        return jokes[:num]
