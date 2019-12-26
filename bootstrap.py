from Config.config import config
from registry import registry
UI = config['UI']["welcome_interface"]
PromptMessages = UI["prompt"]

class Bootstrap :

    __slots__ = ["player_name", "game", "level", "game_UI"]

    def __init__(self):
        self.player_name = ''
        self.game = None
        self.level = None
        self.game_UI = None


    def welcome(self) :
        self.player_name = input(PromptMessages["PlayerName"])
        print(UI["welcome_message"].format(self.player_name))


    def load_game(self) :
        self.displayChoices()
        self.game = int(self.choose(PromptMessages["ChooseGame"], len(config['UI']["Games"]) ))
        self.game_UI = config['UI']["Games"][int(self.game) -1]
        print(PromptMessages["ChooseGame"]["GameChoosen"].format(self.game_UI["Title"]))
        self.level = int(self.choose(PromptMessages["ChooseLevel"], 5))

    def choose(self, PromptMessages, rangeVal):
        val = input(PromptMessages["Prompt"])
        errorMessage = self.checkForInputError(val, rangeVal, PromptMessages)
        while errorMessage :
            val = input(errorMessage)
            errorMessage = self.checkForInputError(val, rangeVal, PromptMessages)
        return val


    def displayChoices(self):
        i = 1
        for game in config['UI']["Games"]:
            print ('{}. {}-{}'.format(str(i), game["Title"], game['SubTitle']))
            i +=1

    def checkForInputError(self, inputVal, rangeVal, errorMessages):
        if not inputVal.isdigit() :
            return errorMessages['NotDigitError']
        if not int(inputVal) in range(1,rangeVal+1) :
            return errorMessages['NotExistrror']
        return False

    def start_playing(self):
        print(UI["start_message"].format(self.game_UI["Title"], self.level))
        try :
            new_game = registry[self.game -1](self.level)
            new_game.play()
        except IndexError as e :
            print(PromptMessages["Game_no_available"].format(self.game_UI["Title"]))



