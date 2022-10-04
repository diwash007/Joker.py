# Joker.py

## About

A simple python package to get jokes and puns.

## How to use?

You can use this by package from [Joker.py](https://pypi.org/project/joker.py/)

```sh
pip install joker.py
```

## Why use this?

To fetch jokes and puns on your projects.

## How to use?

```py
from joker import Joker


joker = Joker()
joke = joker.joke()
print(joke)

puns = joker.puns(5)
for pun in puns:
    print(pun)

```

## Available functions

- joke() - returns a random joke
- jokes(n) - returns n random jokes
- pun() - returns a random pun
- puns(n) - returns n random puns

## Want To Contribute?

You can send a pull request or open an issue to contribute.
Check out [Code Of Conduct](CODE_OF_CONDUCT.md) before contributing.

## License

[MIT Liscense](LICENSE)
