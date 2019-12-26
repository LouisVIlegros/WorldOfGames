from random import randint
from Config.config import config
from Games.GameTemplate import game
import numpy
import time
class MemoryGame(game):

    __slots__ = ["length", "sequence", "UI"]

    def __init__(self, level):
        self.length = level
        self.sequence = []
        self.UI = config["UI"]["Games"][1]["prompt"]

    def play(self):

        self.generate_sequence()
        self.get_list_from_user()

    def generate_sequence(self):
        print(self.UI["start"])
        for i in reversed(range(0,5)) :
            print(i, end="\r")
            time.sleep(1)
        for i in range(0, self.length) :
            self.sequence.append(randint(0,101))
        print(' '.join([str(i) for i in self.sequence]), end="\r")
        time.sleep(0.7)
    def get_list_from_user(self):

        input_user_list = []
        while len(input_user_list) != len(self.sequence) :
            input_number = input("Type the {} number : \n".format(str(self.UI["Numbers"][len(input_user_list)])))
            errorMessage = self.checkForInputError(input_number, 101, self.UI)
            while errorMessage :
                print(errorMessage)
                input_number = input("Type the {} number : \n".format(str(self.UI["Numbers"][len(input_user_list)])))
                errorMessage = self.checkForInputError(input_number, 101, self.UI)
            input_user_list.append(int(input_number))
        self.compareList(input_user_list)

    def compareList(self, inputList):
        test = numpy.all(numpy.asarray(self.sequence) == numpy.asarray(inputList))
        message = self.UI["Success"] if test else self.UI["Fail"]
        print(message)



    def checkForInputError(self, inputVal, rangeVal, errorMessages):
        if not inputVal.isdigit() :
            return errorMessages['NotDigitError']
        if not int(inputVal) in range(1,rangeVal+1) :
            return errorMessages['NotExistrror'].format((str(rangeVal)))
        return False







