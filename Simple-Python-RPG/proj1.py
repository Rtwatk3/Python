# Code for the Stranger things-esque game.

##################################
#### DO NOT TOUCH THESE LINES ####
from random import randint, seed #
seed(100)                        #
##################################


DESCRIPTION=["Equipable weapon (50 attack)","Travel 1.5 times as far as you normally would each day","Halves The Demogorgon's health at the start of a fight"
			"Travel 1.25 times as far as you normally would each day","Decreases The Demogorgon's attack by 25%","Equipable weapon (100 attack)","Equipable weapon (25 attack)"]

#Stats
BASE_DEM_ATTACK=20
MAX_HEALTH = 100
MIN_HEALTH = 0
DEM_MAX_HEALTH = 300

#constants for survival
SURVIVE_DAYS = 7
SURVIVE_DIST = 150

#choices
EQUIP_ITEM=["Equip","Unequip","I changed my mind."]
DO_YOU_STAY=["Pack up camp and go","Stay where you are"]
FIGHT_CHOICES = ["Fight","Flail","Flee"]
CHOICES=["View Inventory","View Current Stats","Eat an Eggo Waffle","Nothing else"]
YES_OR_NO=["Yes","No"]

#constant lists of food and items
FOODS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread", "Twinkies"]
ITEMS = ["Sword", "Bicycle", "Hi-C", "Heelys",
         "Walkman", "Laser Cannon", "Rubber Band"]
EVENTS=["Food","Shed","Trench"]




def getRandomNum(start,end):
    num = randint(start,end)
    return num
#Returns a random number   #input: start and end of the random numbers    #output: a random number

def displayStats(playerHealth,demHealth):
    print("Your health:",playerHealth)
    print("Monster Health:",demHealth)
#prints player health and monste health   #input: player health and monster health  #output: prints player health and monste health

def getUserChoice(choices):
    numChoices=len(choices)
    playerChoice=int(input("Enter a choice: "))
    while(playerChoice>numChoices):
        print("Invalid choice. Please enter a choice from the list above")
        playerChoice=int(input("Enter a choice: "))
    return playerChoice
#Returns the players choice and validates the input   #input: list of choices    #output: the player's choice
    
def displayMenu(choices):
    index=0
    numChoices=len(choices)
    while (index<numChoices):
        print(index+1,"-",choices[index])
        index+=1
    print()
#prints the numbered menu of choices    #input: list of choices    #output: numbered menu of choices
        
def calcDamage(item):
    damage=0
    if(item=="Flashlight"):
        damage=5
    elif(item=="Walkie Talkie"):
        damage=10
    elif(item=="Rubber Band"):
        damage=25
    elif(item=="Sword"):
        damage=50
    elif(item=="Laser Cannon"):
        damage=100
    else:
        damage=0
    return damage
#Returns the damage of the item   #input: the item    #output: the damage of the item

def getFood(food):
    points=0
    if(food=="Reese's Pieces"):
        points=-30
    elif(food=="Pop Rocks"):
        points=-5
    elif(food=="Ovaltine"):
        points=15
    elif(food=="Wonder Bread"):
        points=25
    elif(food=="Twinkies"):
        points=30
    else:
        points=0
    return points
#Returns how much the food heals  #input: name of the food    #output: a healing points
    
def eat(food, playerHealth):
    foodPoints=getFood(food)
    remainder=0
    if(foodPoints<0):
        playerHealth+=foodPoints
    else:
        if(playerHealth<MAX_HEALTH):
            playerHealth+=foodPoints
        else:
            print("Player health is already full!")
            print()
    if(playerHealth>MAX_HEALTH):
        remainder=playerHealth-MAX_HEALTH
        playerHealth-=remainder
    return playerHealth
#computs how much the player should be healed and then adds it to the health if it is under 100   #input: the food and the player health    #output: the player health

def doFlee():
	randNum=getRandomNum(1,10)
	if(randNum<=3):
		return True
	else:
		return False
#Calls a random number then returns true or false depending on the number   #input: none    #output: True or false

def doDemTurn(attack,playerHealth):
    playerHealth-=attack
    print("The Demogorgon strikes you back for",attack,"damage.")
    return playerHealth
#Completes the monster's turn   #input: attack and player health    #output: player health

def fight(playerHealth, item, inventory):
    print("The Demogorgon appears in front of you.")
    print("Its face opens up like a flower to display rows and rows of teeth. It came here for a fight.")
    demHealth=DEM_MAX_HEALTH
    attack=BASE_DEM_ATTACK
    temp=0
    damage=0
    if("Walkman" in inventory):
        temp=float(attack/25)
        attack-=temp
    if("Hi-C" in inventory):
        demHealth=int(demHealth/2)
    runAway=False
    while(playerHealth>MIN_HEALTH and demHealth>MIN_HEALTH and runAway==False):
        runAway=False
        displayStats(playerHealth,demHealth)
        print("What do you do now?")
        print()
        #Get the choices and do them
        displayMenu(FIGHT_CHOICES)
        playerChoice=getUserChoice(FIGHT_CHOICES)
        if(playerChoice==1):
            damage=calcDamage(item)
            print("You strike the Demogorgon with your",item,"for",damage,"damage.")
            demHealth-=damage
            playerHealth=doDemTurn(attack,playerHealth)
        elif(playerChoice==3):
            flee=doFlee()
            if(flee==True):
                runAway=True
                print("You try to run away from the fight. You are successful, and you live to die another day.")
            else:
                print("You try to run away from the fight. The Demogorgon blocked your attempt to run.")
                temp=float(attack/2)
                attack=temp
                playerHealth=doDemTurn(attack,playerHealth)
        else:
            print("You try to assert your domincance by T-posing. The demogorgon is unfazed, rendering your t-pose \"attack\" useless.")
            print("The demogorgon hits you and knocks you out.")
            playerHealth=0
        
    return playerHealth
#does the fight   #input: players Health player' equipped item and players inventory   #output: a random number

def showInvetory(inventory,oldItem):
    choice=0
    print("Here is what your inventory looks like:")
    print(inventory)
    displayMenu(EQUIP_ITEM)
    choice=getUserChoice(EQUIP_ITEM)
    #equip
    if(choice==1):
        print("Heres what you can equip: ")
        displayMenu(inventory)
        choice=getUserChoice(inventory)
        item=equipItem(inventory,choice)
    #unequip
    elif(choice==2):
        item="No item"
    else:
        item=oldItem
    return item
#shows the invetory and lets the player swap items   #input: player's inventory and players current item    #output: player's new item/ old one

def equipItem(inventory,choice):
    newItem=inventory[choice-1]
    print("You have equipped:",newItem)
    return newItem
#swaps the old item with the new one   #input: player's invetory and players choice    #output: the new item
    
def doTask(playerChoice,inventory,playerHealth,equip,distance):
    numItems=len(inventory)
    #show inventory
    newItem=equip
    if(playerChoice==1):
        newItem=showInvetory(inventory,newItem)
    #Display stats
    elif(playerChoice==2):
        print("Health:",playerHealth)
        print("Distance traveled:",distance)
        print("Equipped Item:",newItem)
        print()
    elif(playerChoice==4):
        print("The Demogorgon looms in the distance. Do you leave your camp, or do you stay?")
    return newItem
#does the task   #input: the player choice, invetory, health, player's equip and the distance traveled    #output: the new item

def waffleTime(numWaffles,playerHealth):
    if(numWaffles==0):
        playerHealth+=10
        print("You ate the Eggo Waffle. So bad, yet so good.")
        print("Your health has increased by 10 points.")
    else:
        print("You have no more waffles")
    return playerHealth
#lets you eat a waffle if you havent eatten one already   #input: number of waffles and player health    #output: player health

def stayCamp(playerHealth, item, inventory):
    randNum=getRandomNum(1,10)
    if(randNum<=7):
        #demogorgon attack
        playerHealth=fight(playerHealth, item, inventory)
    else:
        print("You rest safely.")
        print("Your health has been fully restored.")
        playerHealth=MAX_HEALTH
    return playerHealth
#gets a random number. If it is greater than 7, your health is restored. if not you fight   
#input: player health, item and players invetory    #output: player health

def getDistance(playerHealth,inventory):
	if("Bicycle" in inventory):
		temp=float(((playerHealth/4)+5)*1.5)
		distance=float(((playerHealth/4)+5)+temp)
	elif("Heelys" in inventory):
		temp=float(((playerHealth/4)+5)*1.25)
		distance=float(((playerHealth/4)+5)+temp)
	else:
		distance=float((playerHealth/4)+5)
	return distance
#calculates distance depending on items in invetory   #input: player health and invetory    #output: distance to travel

def getEvent(events):
	randNum=getRandomNum(0,2)
	return events[randNum]
#gets a random number for a random event  #input: list of events    #output: random event

def doShed(inventory):
    print("You pass by and old shed and decide to go inside. Something on the shelf catches your eye.")
    randNum=getRandomNum(0,6)
    newItem=ITEMS[randNum]
    while(newItem in inventory):
    	newItem=ITEMS[randNum]
    print("You reach up to grab the item. It's a",newItem)
    printDescription(randNum)
    print("The",newItem,"has been added to your inventory.")
    return newItem
#does the shed event, gets a random item   #input: player invetory    #output: the new item

def doFood(playerHealth):
	food=FOODS[getRandomNum(0,4)]
	choice=0
	points=0
	print("As you were walking, you found a backpack.")
	print("Inside the backpack, there was some",food)
	print("Do you want to eat it?")
	displayMenu(YES_OR_NO)
	choice=getUserChoice(YES_OR_NO)
	if(choice==1):
		points=getFood(food)
		playerHealth=eat(food, playerHealth)
	else:
		print("You put the",food,"back in the bag")
		playerHealth+=0
	return playerHealth
#gets a random food item and lets the player decide if they eat or not
#input: the players health    #output: the players health, updated

def doTrench(days):
	days+=1
	print("You fell into a trence! You need a day to recover...")
	return days
#does the trench event, skips a day   #input: number of days    #output: the current day +1

def printDescription(itemNum):
	print(DESCRIPTION[itemNum-1])
#prints the description of the item you found   #input: item's index    #output: the description

def main():
    day=1
    distance=0.0
    inventory=["Walkie Talkie","Flashlight"]
    item="No item"
    playerHealth=MAX_HEALTH
    confirm=False
    playerChoice=0
    print("After miles and miles of hiking in the woods, you finally setup your camp.")
    print("You decided to go camping on the wrong weekend.")
    print("Your phone buzzes:")
    print("THE DEMOGORGON HAS ESCAPED.     RUN.")
    #while the days are less than the max, distance is less than max, and player health is above the minimum
    while(day<SURVIVE_DAYS and distance<SURVIVE_DIST and playerHealth>MIN_HEALTH):
        # show menu with the daily choices you can make
        print()
        print("The sun rises on Day",day,"in the forest.")
        print()
        displayMenu(CHOICES)
        print("What do you do today?")
        print()
        confirm=False
        numWaffles=0
        #while the player didnt decide to pack and confirm
        while(playerChoice!=4 and confirm==False):
            playerChoice=getUserChoice(CHOICES)    
            item=doTask(playerChoice,inventory,playerHealth,item,distance)
            if(playerChoice==4):
                displayMenu(DO_YOU_STAY)
                if(getUserChoice(DO_YOU_STAY)==1):
                    confirm=True
                else:
                    confirm=False
                    playerChoice=0
            #Eats the waffle and increments the number of waffles by one
            elif(playerChoice==3):
                playerHealth=waffleTime(numWaffles,playerHealth)
                numWaffles+=1
            print("What else will you do today?")
            displayMenu(CHOICES)
            #leave the camp
        #if the player leaves camp
        if(confirm==True):
            travel=getDistance(playerHealth,inventory)
            eventChance=getRandomNum(1,10)
            #30% chance for the fight
            if(eventChance<=3):
                playerHealth=fight(playerHealth, item, inventory)
                travel=getDistance(playerHealth,inventory)
            #60% chance for and event
            elif(eventChance>3 and eventChance<=9):
                event=getEvent(EVENTS)
                if(event=="Food"):
                    #food event
                    playerHealth=doFood(playerHealth)
                elif(event=="Shed"):
                    #shed event
                    inventory.append(doShed(inventory))
                    travel=getDistance(playerHealth,inventory)
                else:
                    #trench event
                    travel-=float(travel/2)
                    day=doTrench(day)
            else:
                print("You safely walk through the forest.")
                print("You decide that youve had enough walking for today and settle down for the night")                
        else:
            #makes the player stay at camp and calls the stayCamp function. updates th players health
            playerHealth=stayCamp(playerHealth,item,inventory)
        #only travel if the player health is greater than the minimum
        if(playerHealth>MIN_HEALTH):
            if("Bicycle" in inventory):
                print("The Bicycle you found improved your distance traveled.")
            elif("Heelys" in inventory):
                print("The Heelys you found improved your distance traveled.")
            distance+=travel
            print("You have now traveled",distance)
        day+=1
        playerChoice=0
        confirm=False
        #if the day is higher than the max, you won by living 7 days
    if(day>=SURVIVE_DAYS):
        print("Congratulations!")
        print("You survived for 7 days.")
        #if the distance is greater than the max survival distance, you won by distance
    elif(distance>=SURVIVE_DIST):
        print("Congratulations!")
        print("It took",day,"days to go",distance,"miles.")
    else:
        #you died
        print("You have been slain")
        #prints final stats
    print("Final Stats:")
    print("Health:",playerHealth)
    print("Distance traveled:",distance)
    print("Equipped Item:",item)
main()
