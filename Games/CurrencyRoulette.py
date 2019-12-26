import requests
from random import randint
from Config.config import config
from Games.GameTemplate import game
class CurrencyRoulette(game):

    def __init__(self, level):
        self.difficulty = int(level)
        self.random_amount = randint(1,100)
        self.config = config["UI"]["Games"][2]
        currency = requests.get(self.config["Currency_URL"])
        self.converted_amount = self.random_amount * currency.json()["rates"]["ILS"]
        self.tolerance = range(int(self.converted_amount) - (5-self.difficulty), int(self.converted_amount) + (5-self.difficulty))

    def play(self):

        self.get_guess_from_user()

    def get_guess_from_user(self):
        print(self.config["prompt"]["AskFromUser"].format(str(self.random_amount)))
        guess_amount = input(self.config["prompt"]["GuessFromUser"])
        error_message = self.checkForInputError(guess_amount, 100, self.config["prompt"])
        while error_message :
            guess_amount = input(error_message)
            error_message = self.checkForInputError(guess_amount, 100, self.config["prompt"])
        if int(guess_amount) in self.tolerance :
            print(self.config["prompt"]["win"].format(self.converted_amount))
        else :
            print(self.config['prompt']["loose"].format(self.converted_amount))



    def checkForInputError(self, inputVal, rangeVal, errorMessages):
        if not inputVal.isdigit():
            return errorMessages['NotDigitError']
        return False



