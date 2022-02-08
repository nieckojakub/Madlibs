import json
import random


class Madlibs:

    def __init__(self, userName):
        self.userName = userName

        self.noun = []
        self.adjective = []
        self.place = []

        self.nounNumber = None
        self.adjectiveNumber = None
        self.placeNumber = None

        self.storyName = None
        self.storyNumber = None

        self.storyText = []
        self.story = None

        self.whereAdj = None
        self.whereANoun = None
        self.wherePlace = None

    def chooseStory(self):
        while True:
            try:
                print("Hello, ", self.userName, "!")
                self.storyNumber = int(input("Choose a story: \n1. About Star Wars\n2. About Dog\n "))

                if self.storyNumber == 1:
                    self.storyName = "Star Wars"
                    break
                elif self.storyNumber == 2:
                    self.storyName = "Dog"
                    break
                else:
                    print("There is no such story with this value")

            except:
                print("Type integer number! ")

    def getWordFromUser(self):
        for i in range(self.nounNumber):
            nounInput = input(f"Enter {i + 1} noun: ")
            self.noun.append(nounInput)

        for i in range(self.adjectiveNumber):
            adjectiveInput = input(f"Enter {i + 1} adjective: ")
            self.adjective.append(adjectiveInput)

        for i in range(self.placeNumber):
            placeInput = input(f"Enter {i + 1} place: ")
            self.place.append(placeInput)

    def loadStory(self):
        with open("story.json", 'r') as f:
            data = json.load(f)
            self.storyText = data[self.storyName]["text"]
            self.nounNumber = data[self.storyName]["nounNumber"]
            self.adjectiveNumber = data[self.storyName]["adjNum"]
            self.placeNumber = data[self.storyName]["placeNumber"]

            self.whereAdj = data[self.storyName]["whereAdj"]
            self.wherePlace = data[self.storyName]["wherePlace"]
            self.whereANoun = data[self.storyName]["whereNoun"]

    def createStory(self):
        x = self.storyText
        split_txt = str(x).split(" ")
        amount = self.adjectiveNumber + self.nounNumber + self.placeNumber

        y1 = self.whereAdj
        whereAdjList = str(y1).split(",")

        y2 = self.whereANoun
        whereNounList = str(y2).split(",")

        y3 = self.wherePlace
        wherePlaceList = str(y3).split(",")

        for i in split_txt:
            for j in range(amount + 1):
                if i == str(j):
                    if str(j) in wherePlaceList:
                        index = split_txt.index(str(j))

                        radnomChoice = random.choice(self.place)
                        self.place.remove(radnomChoice)
                        split_txt[index] = radnomChoice

                    elif str(j) in whereNounList:
                        index = split_txt.index(str(j))

                        radnomChoice = random.choice(self.noun)
                        self.noun.remove(radnomChoice)
                        split_txt[index] = radnomChoice

                    elif str(j) in whereAdjList:
                        index = split_txt.index(str(j))

                        radnomChoice = random.choice(self.adjective)
                        self.adjective.remove(radnomChoice)
                        split_txt[index] = radnomChoice

        self.story = " ".join(split_txt)

    def printStory(self):
        print(self.story)


## -------------------- Main   -------------------


if __name__ == "__main__":

    while True:
        userName = input("Hello User !\nEnter your name: ")
        if userName.isdigit():
            print("Invalid! Enter String")
        else:
            break

    madlibs = Madlibs(userName)
    madlibs.chooseStory()
    madlibs.loadStory()
    madlibs.getWordFromUser()
    madlibs.createStory()
    madlibs.printStory()
