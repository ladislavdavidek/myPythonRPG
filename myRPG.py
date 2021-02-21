from random import randint, shuffle
from math import floor
from time import sleep

from enemyTypesLib import enemyTypes as enemyTypes

inputName = "TEST_NAME"#input("What is your name, hero? >>> ")
patternOfTypes = [4,3,3,2,2,1,1]
indexOfTypes = []

class Enemy:
    def __init__(self, name: str, health: int, attack: int, defense: int, experience: int):
        self.name = name
        self.health = health 
        self.attack = attack 
        self.defense = defense
        self.experience = experience

    def calculateStats(self, getDifficulty):
        difficulty = getDifficulty
        enemyStats = ["",0,0,0,0]
        enemyStats[0] = enemyTypes[difficulty]["enemyType"][randint(0,1)]
        enemyStats[1] = randint(enemyTypes[difficulty]["health"][0], enemyTypes[difficulty]["health"][1])
        enemyStats[2] = randint(enemyTypes[difficulty]["attack"][0], enemyTypes[difficulty]["attack"][1])
        enemyStats[3] = randint(enemyTypes[difficulty]["defense"][0], enemyTypes[difficulty]["defense"][1])
        enemyStats[4] = floor((enemyStats[2] * 3.236 + enemyStats[3] * 2.89 + enemyStats[1] * 2) * 4.56)
        # return enemyStats
        pass

    def generateEnemy(self, difficultyIndex):
        difficulty = ""
        enemyStats = ["",0,0,0,0]

        # tento humus zrefactorovat!!
        if difficultyIndex == 0:
            difficulty = "Very easy"
            enemyStats[0] = enemyTypes[difficulty]["enemyType"][randint(0,1)]
            enemyStats[1] = randint(enemyTypes[difficulty]["health"][0], enemyTypes[difficulty]["health"][1])
            enemyStats[2] = randint(enemyTypes[difficulty]["attack"][0], enemyTypes[difficulty]["attack"][1])
            enemyStats[3] = randint(enemyTypes[difficulty]["defense"][0], enemyTypes[difficulty]["defense"][1])
            enemyStats[4] = floor((enemyStats[2] * 3.236 + enemyStats[3] * 2.89 + enemyStats[1] * 2) * 4.56)
            return enemyStats
        
        elif difficultyIndex == 1:
            difficulty = "Easy"
            enemyStats[0] = enemyTypes[difficulty]["enemyType"][randint(0,1)]
            enemyStats[1] = randint(enemyTypes[difficulty]["health"][0], enemyTypes[difficulty]["health"][1])
            enemyStats[2] = randint(enemyTypes[difficulty]["attack"][0], enemyTypes[difficulty]["attack"][1])
            enemyStats[3] = randint(enemyTypes[difficulty]["defense"][0], enemyTypes[difficulty]["defense"][1])
            enemyStats[4] = floor((enemyStats[2] * 3.236 + enemyStats[3] * 2.89 + enemyStats[1] * 2) * 4.56)
            return enemyStats
        
        elif difficultyIndex == 2:
            difficulty = "Medium"
            enemyStats[0] = enemyTypes[difficulty]["enemyType"][randint(0,1)]
            enemyStats[1] = randint(enemyTypes[difficulty]["health"][0], enemyTypes[difficulty]["health"][1])
            enemyStats[2] = randint(enemyTypes[difficulty]["attack"][0], enemyTypes[difficulty]["attack"][1])
            enemyStats[3] = randint(enemyTypes[difficulty]["defense"][0], enemyTypes[difficulty]["defense"][1])
            enemyStats[4] = floor((enemyStats[2] * 3.236 + enemyStats[3] * 2.89 + enemyStats[1] * 2) * 4.56)
            return enemyStats
        
        elif difficultyIndex == 3:
            difficulty = "Hard"
            enemyStats[0] = enemyTypes[difficulty]["enemyType"][randint(0,1)]
            enemyStats[1] = randint(enemyTypes[difficulty]["health"][0], enemyTypes[difficulty]["health"][1])
            enemyStats[2] = randint(enemyTypes[difficulty]["attack"][0], enemyTypes[difficulty]["attack"][1])
            enemyStats[3] = randint(enemyTypes[difficulty]["defense"][0], enemyTypes[difficulty]["defense"][1])
            enemyStats[4] = floor((enemyStats[2] * 3.236 + enemyStats[3] * 2.89 + enemyStats[1] * 2) * 4.56)
            return enemyStats
        
        elif difficultyIndex == 4:
            difficulty = "Very hard"
            enemyStats[0] = enemyTypes[difficulty]["enemyType"][randint(0,1)]
            enemyStats[1] = randint(enemyTypes[difficulty]["health"][0], enemyTypes[difficulty]["health"][1])
            enemyStats[2] = randint(enemyTypes[difficulty]["attack"][0], enemyTypes[difficulty]["attack"][1])
            enemyStats[3] = randint(enemyTypes[difficulty]["defense"][0], enemyTypes[difficulty]["defense"][1])
            enemyStats[4] = floor((enemyStats[2] * 3.236 + enemyStats[3] * 2.89 + enemyStats[1] * 2) * 4.56)
            return enemyStats
        
        elif difficultyIndex == 5:
            difficulty = "Boss"
            enemyStats[0] = enemyTypes[difficulty]["enemyType"][randint(0,1)]
            enemyStats[1] = randint(enemyTypes[difficulty]["health"][0], enemyTypes[difficulty]["health"][1])
            enemyStats[2] = randint(enemyTypes[difficulty]["attack"][0], enemyTypes[difficulty]["attack"][1])
            enemyStats[3] = randint(enemyTypes[difficulty]["defense"][0], enemyTypes[difficulty]["defense"][1])
            enemyStats[4] = floor((enemyStats[2] * 3.236 + enemyStats[3] * 2.89 + enemyStats[1] * 2) * 4.56)
            return enemyStats
        else:
            return "INDEX_OUT_OF_RANGE"
        
        difficulty = ""
        enemyStats = ["",0,0,0,0]

class TextFormatting:
    def __init__(self, listsOfWords: list):
        self.listOfLengths = []
        self.lengthOfLine = 28
        self.lengthOfSpace = 0
        for innerList in listsOfWords:
            for words in innerList:
                self.listOfLengths.append(len(str(words)))   
            self.lengthOfSpace = 28 - sum(self.listOfLengths)
            print(str(innerList[0])+self.lengthOfSpace*" "+str(innerList[1]))
            self.listOfLengths = []
            self.lengthOfSpace = 0
        
class Player:
    def __init__(self, name: str, health: int, attack: int, defense: int, experience: int, level: int, nextLevel: int, dead: bool):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience
        self.level = level
        self.nextLevel = nextLevel
        self.dead = dead

        

class Game:
    def __init__(self, countOfEnemies):
        self.enemiesList = []

        # vyplneni indexu podle patternu pro naslednou generaci nepratel
        for i in range(len(patternOfTypes)):
            for j in range(patternOfTypes[i]):
                indexOfTypes.append(i)
                
        # generovani nepratel
        for i in range(countOfEnemies):
                self.enemiesList.append(Enemy(Enemy.generateEnemy(self, indexOfTypes[i])[0], Enemy.generateEnemy(self, indexOfTypes[i])[1], Enemy.generateEnemy(self, indexOfTypes[i])[2], Enemy.generateEnemy(self, indexOfTypes[i])[3], Enemy.generateEnemy(self, indexOfTypes[i])[4]))
            
        # generovani hrace # nemenit !!!!
        self.hero = Player(inputName, 20, 4, 4, 0, 1, 200, False) 

        # zamichani seznamu nepratel
        shuffle(self.enemiesList) 
        
        print()
        print(inputName + ", You are in the forrest, where are these creatures:\n")
   
        self.openGame()

    def openGame(self):
        while self.hero.dead == False:
            print("YOUR STATS:\n")
            TextFormatting([["NAME:",self.hero.name],["ATTACK:", self.hero.attack],["DEFENSE:", self.hero.defense],["HEALTH:", self.hero.health],["LEVEL:", self.hero.level],["EXP:", self.hero.experience],["NEXT LVL:", self.hero.nextLevel]])
            print()
            print("Choose your oponnent:\n")
            # vypis nepratel
            TextFormatting([ ["ENEMY NAME", "AT DF HP"]])
            for i in range(len(self.enemiesList)):
                TextFormatting([ [str(i+1) + ")"+str(self.enemiesList[i].name), str(str(self.enemiesList[i].attack) + " " + str(self.enemiesList[i].defense) + " " +  str(self.enemiesList[i].health)) ]])
                #print(str(i+1) + ")"+str(self.enemiesList[i].name), self.enemiesList[i].attack, self.enemiesList[i].defense, self.enemiesList[i].health)
            print()
            # add validation for 'selectedEnemy'
            selectedEnemy = int(input("Select your oponnent >>> "))
            print()
            self.enemyStats = []
            # refactor this
            self.enemyStats.append(self.enemiesList[selectedEnemy-1].name)
            self.enemyStats.append(self.enemiesList[selectedEnemy-1].attack)
            self.enemyStats.append(self.enemiesList[selectedEnemy-1].defense)
            self.enemyStats.append(self.enemiesList[selectedEnemy-1].health)
            self.enemyStats.append(self.enemiesList[selectedEnemy-1].experience)

            print("You attacked", self.enemyStats[0],"\n")
            print(28*"*")
            cycleCount = 0
            while self.hero.dead == False and self.enemyStats[3] > 0:
                
                print("You get hit with power of", self.enemyStats[1])
                self.hero.health -= self.enemyStats[1]
                print("Remaining health points: ", self.hero.health)
                if self.hero.health <= 0:
                    cycleCount += 1
                    self.hero.dead = True
                    print(28*"*")
                    print("YOU died after", cycleCount, "round(s).")
                    print(28*"*")
                    break
                print()
                print("You hit", self.enemyStats[0],"with power of", self.hero.attack)
                self.enemyStats[3] -= self.hero.attack
                cycleCount += 1
                print("His emaining health points: ", self.enemyStats[3])
                if self.enemyStats[3] <= 0:
                    print(28*"*")
                    print(self.enemyStats[0], "died after", cycleCount, "round(s).")
                    print(28*"*")
                    self.enemiesList.remove(self.enemiesList[selectedEnemy-1])
                    self.enemyStats = []
                    break
                print()
                print(28*"*")
                sleep(1.5)

        if self.hero.dead == True:
            decide = input("Try again? >>> ")
            if decide == "yes" or decide == "y":
                g = Game(15)
            else:
                print("Ok, bye.")
        else:
            print("Thanks for playing, Champion!")

g = Game(15)
