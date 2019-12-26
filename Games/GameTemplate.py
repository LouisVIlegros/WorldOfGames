from abc import  ABC, abstractmethod

class game(ABC) :

    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def checkForInputError(self, inputVal, rangeVal, errorMessages):
        pass