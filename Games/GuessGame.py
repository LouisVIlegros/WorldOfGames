from random import randint
from Games.GameTemplate import game

from Config.config import config
class GuessGame(game):

    __slots__ = ["secret_number", "highest", "UI"]
    def __init__(self, level):
        self.highest = level
        self.secret_number = randint(0, self.highest)
        self.UI = config["UI"]["Games"][0]["prompt"]
    def play(self):
        guess_num = input(self.UI["start"].format(str(self.highest)))
        error_message = self.checkForInputError(guess_num, self.highest, self.UI)
        while error_message :
            guess_num = input(error_message)
            error_message = self.checkForInputError(guess_num, self.highest, self.UI)

        while int(guess_num) != self.secret_number :
            error_message = self.checkForInputError(guess_num, self.highest, self.UI)
            while error_message:
                guess_num = input(error_message)
                error_message = self.checkForInputError(guess_num, self.highest, self.UI)
            guess_num = int(guess_num)
            if guess_num < self.secret_number :
                guess_num = input("The number is higher")
            else :
                guess_num = input("the number is lower")
        print("Bravo ! {} is the right number".format(str(guess_num)))

    def checkForInputError(self, inputVal, rangeVal, errorMessages):
        if not inputVal.isdigit() :
            return errorMessages['NotDigitError']
        if not int(inputVal) in range(1,rangeVal+1) :
            return errorMessages['NotExistrror'].format((str(self.highest)))
        return False