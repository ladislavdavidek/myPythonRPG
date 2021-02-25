from random import randint, shuffle
from math import floor
from time import sleep
import tkinter as tk

# 854x480 window resolution
from enemyTypesLib import enemyTypes as enemyTypes

inputName = "Ladislav Mocný" #input("What is your name, hero? >>> ")
patternOfTypes = [4,3,3,2,2,1]
indexOfTypes = []


class Enemy:
    def __init__(self, name: str, health: int, attack: int, defense: int, experience: int):
        self.name = name
        self.health = health 
        self.attack = attack 
        self.defense = defense
        self.experience = experience

    def generateEnemy(self, difIndex):
        difficulty = ["Very easy","Easy","Medium","Hard","Very hard","Boss"]
        enemyStats = ["",0,0,0,0]
        enemyStats[0] = enemyTypes[difficulty[difIndex]]["enemyType"][randint(0,1)]
        enemyStats[1] = randint(enemyTypes[difficulty[difIndex]]["health"][0], enemyTypes[difficulty[difIndex]]["health"][1])
        enemyStats[2] = randint(enemyTypes[difficulty[difIndex]]["attack"][0], enemyTypes[difficulty[difIndex]]["attack"][1])
        enemyStats[3] = randint(enemyTypes[difficulty[difIndex]]["defense"][0], enemyTypes[difficulty[difIndex]]["defense"][1])
        enemyStats[4] = floor((enemyStats[2] * 3.234 + enemyStats[3] * 2.91 + enemyStats[1] * 2.11) * 4.49)
        return enemyStats
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
    def __init__(self, name: str, health: int, attack: int, defense: int, experience: int, level: int, nextLevel: int):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience
        self.level = level
        self.nextLevel = nextLevel
        
class Game:
    def __init__(self, countOfEnemies):
        self.enemiesList = []
        self.playerStats = 0
        # vyplneni indexu podle patternu pro naslednou generaci nepratel
        for i in range(len(patternOfTypes)):
            for j in range(patternOfTypes[i]):
                indexOfTypes.append(i)
                
        # generovani nepratel
        for i in range(countOfEnemies):
                self.enemiesList.append(Enemy(Enemy.generateEnemy(self, indexOfTypes[i])[0], Enemy.generateEnemy(self, indexOfTypes[i])[1], Enemy.generateEnemy(self, indexOfTypes[i])[2], Enemy.generateEnemy(self, indexOfTypes[i])[3], Enemy.generateEnemy(self, indexOfTypes[i])[4]))
            
        # generovani hrace # nemenit !!!!
        self.hero = Player(inputName, 20, 4, 4, 0, 1, 200)
        self.playerHealth = self.hero.health

        # zamichani seznamu nepratel
        #shuffle(self.enemiesList) 
        
        print()
        print(inputName + ",\nWelcome in The Forrest,\nwith these monsters:\n")
   
        self.openGame()        

    def openGame(self):
        while self.hero.health > 0 and len(self.enemiesList) > 0:
            self.hero.health = self.playerHealth
            print("YOUR STATS:\n")
            TextFormatting([["NAME:",self.hero.name],["ATTACK:", self.hero.attack],["DEFENSE:", self.hero.defense],["HEALTH:", self.hero.health],["LEVEL:", self.hero.level],["EXP:", self.hero.experience],["NEXT LVL:", self.hero.nextLevel]])
            print()
            print("Choose your oponnent:\n")
            # vypis nepratel
            TextFormatting([ ["ENEMY NAME", "AT DF HP"]])
            for i in range(len(self.enemiesList)):
                TextFormatting([ [str(i+1) + ")"+str(self.enemiesList[i].name), str(str(self.enemiesList[i].attack) + " " + str(self.enemiesList[i].defense) + " " +  str(self.enemiesList[i].health)) ]])
            print()
            # add validation for 'selectedEnemy'
            selectedEnemy = int(input("Select your oponnent >>> "))
            print()
            print("You attacked", self.enemiesList[selectedEnemy-1].name,"!\n")
            print(28*"*")
            cycleCount = 0
            while self.hero.health > 0 and self.enemiesList[selectedEnemy-1].health > 0:
                print(self.enemiesList[selectedEnemy-1].name+"'s attack: ", self.enemiesList[selectedEnemy-1].attack)
                # utok na hrace
                self.hero.health -= (self.enemiesList[selectedEnemy-1].attack - ((self.hero.defense/100)*self.enemiesList[selectedEnemy-1].attack))
                print("Your health: ", self.hero.health)
                if self.hero.health <= 0:
                    cycleCount += 1
                    self.hero.dead = True
                    print(28*"*")
                    sleep(1.5)
                    print("YOU died after", cycleCount, "hit(s).")
                    print(28*"*","\n")
                    sleep(1.5)
                    break
                print()
                print("Your attack:", self.hero.attack)
                # utok na enemaka
                self.enemiesList[selectedEnemy-1].health -= (self.hero.attack - ((self.enemiesList[selectedEnemy-1].defense/100)*self.hero.attack))
                cycleCount += 1
                print(self.enemiesList[selectedEnemy-1].name+"'s health: ", self.enemiesList[selectedEnemy-1].health)
                if self.enemiesList[selectedEnemy-1].health <= 0:
                    print(28*"*")
                    sleep(1.5)
                    print(self.enemiesList[selectedEnemy-1].name, "died after", cycleCount, "hit(s).")
                    print("You got", self.enemiesList[selectedEnemy-1].experience,"EXPs.")
                    self.hero.experience += self.enemiesList[selectedEnemy-1].experience
                    if self.hero.experience >= self.hero.nextLevel:
                        self.hero.nextLevel += round(self.hero.nextLevel*1.2)
                        self.hero.level += 1
                        self.hero.attack+=randint(6,13)
                        self.hero.defense+=randint(6,14)
                        self.playerHealth+=randint(6,15)
                        print(28*"*","\nLEVEL UP!")
                    print(28*"*","\n")
                    self.enemiesList.remove(self.enemiesList[selectedEnemy-1])
                    sleep(1.5)
                    break
                print(28*"*")
                sleep(1.5)

        if self.hero.health < 0:
            decide = input("Try again?  y/n >>> ")
            if decide == "yes" or decide == "y":
                g = Game(15)
            else:
                print("Ok, bye.")
                input("***leave by pressing enter***")
        else:
            print("You killed all the monsters!\n")
            print("YOUR FINAL STATS:\n")
            TextFormatting([["NAME:",self.hero.name],["ATTACK:", self.hero.attack],["DEFENSE:", self.hero.defense],["HEALTH:", self.hero.health],["LEVEL:", self.hero.level],["EXP:", self.hero.experience],["NEXT LVL:", self.hero.nextLevel]])
            print()
            print("Thanks 4 playing, Champion!")
            #add next level -> multiplier base enemy stats * stage
g = Game(15)


