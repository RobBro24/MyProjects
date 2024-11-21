import random

#Global variables for doors and items

floorDoors = ["NORTH","SOUTH","EAST","WEST"]
NorthRoomDoors = ["STAIRS","EAST","WEST"]
SouthRoomDoors = ["SOUTH","EAST","WEST"]
EastRoomChest = "1124"
WestRoomDoors = "IT'S A TRAP!!!!!!"
TreasureChest = ["GUN","SWORD","KNIFE","AXE","ROCK","SHEILD","DYNAMITE","BASEBALLBAT","BOW and ARROWS"]
randWeapon = " "
weaponSelection = " "
weaponInHand = False
startGameLoop = True
wrongPasscode = 0
gameProg = 0
ETV = 0
hasKey = False
WIN = False


#Game loop starts

while WIN == False:
     print("You awaken...lying on the floor in a dimly lit Dungeon" )
     print("You bring yourself to your feet and take a moment to gather yourself")
     print('''upon arising you take a scan on the Dungeon and find that there are four doors
               surrounding you from the NORTH,SOUTH,EAST and WEST''')
     print('''You scan the wall and also see the messages \"Ominous Presence...Evil Near\"
               written in what appears to be blood''')
     print("(This message may be useful later, you think)")
     print('''As well as \"I.I.II.IV. is key \" written with...
some form of magic''')
     print("Looks to be a code of some sort...")
     print('''Rather than waiting around for starvation to take you out
               or something worse you decide to enter one of the doors...''')
     print()
     for x in floorDoors:
                print(x)
               

     print()
     gameProg = 1
     while startGameLoop == True and gameProg == 1:
          
          
                floor1Door = input("What door would you like to explore?: ")
#scenario if the NORTH door is explored
                if floor1Door == "NORTH" or floor1Door == "North" or floor1Door == "north":
                     print("You explore the %s door..."%floorDoors[0])
                     print('''You enter the %s room and discover a treasure chest...
                                   along with several flights of  dimly lit STAIRS and a door to the EAST and WEST'''%floorDoors[0])
                     print("Upon further inspection you find that the chest requires a passcode for entry...")

                     while floorDoors[0] == "NORTH" and gameProg == 1:
                        
                         tcExamine = input("Would you like to check the  Treasure Chest?: ")
                         
                         if tcExamine == "YES" or tcExamine == "Yes" or tcExamine == "yes":
                              chestSeq = True
                              gameProg = 2
                              while chestSeq == True:
                              
                                   tcPasscode = input("What is the password?: ")
                                   if tcPasscode == "OPEN" or tcPasscode =="Open" or tcPasscode =="open":
                                        print("The passcode is Accepted!")
                                        print("You hear the locking mechanism release and the chest flies open...")
                                        randWeapon = random.randrange(len(TreasureChest))
                                        weaponSelection = TreasureChest[randWeapon]
                                        weaponInHand = True
                                        print("A blinding flash of light comes from the box and a(n) %s appears"%weaponSelection)
                                        print("You equip the weapon and turn back to the stairs and doors to continue your journey")

                                        chestSeq = False
                                   
                                        
                                   

                                   elif tcPasscode != "OPEN" or tcPasscode !="Open" or tcPasscode !="open":
                                        print("Passcode Invalid!")
                                        wrongPasscode = wrongPasscode+1
                                        if wrongPasscode >2:
                                             print("You have entered an Incorrect passcode too many times")
                                             print("The chest opens releasing a deadly neurotoxin slowly killing you")
                                             print("Leaving you the newest victim of the Dungeon...")
                                             gameProg = 0
                                             StartGameLoop = False
                                             WIN = True
                                             chestSeq = False
                                             
                                        
                                        
                                   

                                        
                                        
                         elif tcExamine =="NO" or tcExamine == "No" or tcExamine == "no":
                              print("You decide not to examine the chest and turn back to the stairs and doors...")
                              gameProg = 2

                         else:
                              print("Im not sure I understand")
                              
                              


                         while floorDoors[0]=="NORTH" and gameProg == 2:
                              for x in NorthRoomDoors:
                                   print(x)
                              northFloorDoors = input("Which path would you like to explore?: ")
                              
                         
                              if northFloorDoors == "STAIRS" or northFloorDoors == "Stairs" or northFloorDoors =="stairs":
                                   print("You decide to ascend the stairs to an unknown fate")
                                   print('''As you begin your ascent of the stairs
     the deafening silence of the stairwell makes your footsteps sound similar to a tunderstorm ''')
                                   print(".....")
                                   print(".....")
                                   print(".....")
                                   print("As you finally make it to the stairs peak you notice the mechanical whirring of a vault door")
                                   print("and in a flash...A DEADLY MINOTAUR APPEARS weilding a battle Axe!")
                                   
                                   fightSeq = True
                                   
                                   while fightSeq == True and gameProg == 2:
                                        print("You prepare to batlle the ferocious Beast!")
                                        if  weaponInHand == True:
                                             print("You raise your %s and strike the Beast and in an instant he is defeated"%weaponSelection)
                                             fightSeq = False
                                             print("After defeating the beast you then turn to the vault door which is requiring a four digit PIN or KEY to exit")
                                             gameProg = 3
                                             if hasKey == True and gameProg == 3 :
                                                  print("You recover THE MYSTERIOUS KEY from earlier in your adventure...")
                                                  print("You inspect the keyhole and place the key inside..")
                                                  print("You turn the key and open the vault door...")
                                                  print("To your surprise you step into a chamber and are greeted by two armed guards")
                                                  print('''They inform you that you were chosen by their leaders to partake in the Dungeon challange
     to select a new leader for their kingdom. They quickly direct you to the chamber exit, to start your new life as KING.. ''')
                                                  StartGameLoop = False
                                                  WIN = True
                                                  gameProg = 0
                                             elif hasKey == False and gameProg == 3:
                                                  print("You approach the PIN pad which display the numbers 0-9")
                                                  TRIES = 0
                                                  PIN = input("What PIN do you enter?:")
                                                  if PIN == "4211":
                                                       print("PIN ACCEPTED!")
                                                       print("You hear the locking mechanism start to turn and the door slowly starts to open...")
                                                       print("To your surprise you step into a chamber and are greeted by two armed guards")
                                                       print('''They inform you that you were chosen by their leaders to partake in the Dungeon challange
     to select a new leader for their kingdom. They quickly direct you to the chamber exit, to start your new life as KING.. ''')
                                                  elif PIN !="4211" and TRIES ==3:
                                                       print("Too many incorrect tries...")
                                                       print("The ground below you starts to crumble and cave in dropping you into the chasm below...")
                                                       WIN = True
                                                       gameProg = 0
                                                  else:
                                                       print("Invalid Input...please retry")
                                                       TRIES = TRIES+1
                                                       gameProg = 3
                                                       
                                                  
                                        elif weaponInHand == False and gameProg == 2:
                                             print("Without a means of Defense the Beast mauls you...perhaps expolring a chest couldve proven to be useful...")
                                             print("Maybe our next adventurer will be more fortunte...")
                                             StartGameLoop = False
                                             WIN = True
                                             gameProg = 0

                                             
                              elif northFloorDoors == "EAST" or northFloorDoors =="East" or northFloorDoors == "east":
                                   print("You enter the room very cautiously...")
                                   print("Once in the room in an instant the door closes behind you trapping you inside")
                                   print("With no lantern to lantern to light your way you try to move forward only to drop into a pit falling to your death...")
                                   WIN = True
                                   gameProg = 0

                              elif northFloorDoors == "WEST" or northFloorDoors =="West" or northFloorDoors == "west":
                                   print("You walk into the room and hear a low pitch hiss...")
                                   print("You think to look and examine the room but beofre you can you are attacked by a Venomous snake...")
                                   print("You lose conciousness and succumb to your injuries")
                                   WIN = True
                                   gameProg = 0
                              else:
                                   print("Invalid Input...please retry")
                                   

                                   
                         
                              
                         
#scenario if the SOUTH door is explored                         
                elif floor1Door == "SOUTH" or floor1Door == "South" or floor1Door == "south":
                    print("You explore the %s door..."%floorDoors[1])
                    
                    
                    while floorDoors[1] == "SOUTH" and gameProg == 1:
                         print("You enter the %s room and discover a find a room with 3 doors...SOUTH,EAST and WEST"%floorDoors[1])
                         print("You also feel a slight breeze throught out the room but cannot determine where its originating...")
                         southFloorDoors=input("Which would you like to inspect?: ")
                         if southFloorDoors == "SOUTH" or southFloorDoors == "South" or southFloorDoors =="south":
                              print("You open the %s door and a gust of wind shoots out at you")
                              print("You make it into the room and discover a wall of debris and what seems to be light illuminating from it...")
                              print("Feeling lucky, you decide to remove one of the rocks from the rubble causing the wall to start to fall...")
                              print("Quickly you run to take cover during the commotion...")
                              print("...")
                              print("...Finally the commotion subsides revealing...An open path to FREEDOM")
                              print("...A satisfied smirk starts to form on your face as you move towards the path leaving the dungeon forever...")
                              StartGameLoop = False
                              WIN = True
                              gameProg = 0

                         elif southFloorDoors == "EAST" or southFloorDoors == "East" or southFloorDoors =="east":
                              print("You enter the room and see a sword stuck in stone.")
                              print("You decide to try to remove it, as it may be of use later in your adventure.")
                              print("You firmly grasp the hilt and try to draw the sword from the stone but unknown to you the sword has a freezing spell cast over it which freezes you in place.")
                              print("After you are frozen a cave gollum appears from the shadows and collects your frozen statue-like body adding you to a collection of other fools who have tried before you to remove the sword...")
                              WIN = True
                              gameProg = 0

                         elif southFloorDoors == "WEST" or southFloorDoors == "West" or southFloorDoors =="west":
                              print("You take a step and feel one of the floor tiles sink in...")
                              print("You hear and feel a sudden gust of wind breeze by you but think nothing of it")
                              print("You attempt to move forward only to fall face first onto the ground...")
                              print("In that moment you realize that you had been struck by several poison arrows with no other option than to wait for the poison to take its course.")
                              WIN = True
                              gameProg = 0

                              
                         else:
                              print("Invalid Input...please retry")
                         
#scenario if the EAST door is explored                        
                elif floor1Door == "EAST" or floor1Door == "East" or floor1Door == "east" and ETV == 0:
                    print("You explore the %s door..."%floorDoors[2])
                    
                    x1 = 0
                    while floorDoors[2] == "EAST" and x1 == 0 and gameProg == 1:
                         print("You enter the %s room and discover a loot chest..."%floorDoors[2])
                         print("Upon further inspection you find that the chest has a NUMBER LOCK on it")
                         lockGuess = input("Lets try to open up this chest,shall we?: ")
                         if lockGuess == EastRoomChest:
                              print("The box slowly starts levitate...")
                              print("The lid begins to rise...")
                              print("Then suddenly you feel a strange object appear in your hand...")
                              print("Nervously...You open your hand to reavel...")
                              print("A MYSTERIOUS KEY")
                              print("Confidently you close your hand and turn back to the door to return to the room from which you had awaken")
                              hasKey = True
                              x1 = 1
                              ETV = 1

                         else:
                              print("That did not seem to work...")
                               
#scenario if the WEST door is explored
                elif floor1Door == "WEST" or floor1Door == "West" or floor1Door == "west":
                    print("You enter the %s room"%floorDoors[3])
                    print(WestRoomDoors)
                    print("As soon as you enter the room the door closes behind you and locks itself...")
                    print("Once the door locks the room starts to crumble and collapse")
                    print("Eventually the ceiling caves in and crushes you ending your escape...")
                    print("Game Over!!!")
                    StartGameLoop = False
                    WIN = True
                    gameProg = 0

                elif floor1Door == "EAST" or floor1Door == "East" or floor1Door == "east" and ETV == 1:
                     print("The east room cannot be revisited...")

                
                else:
                     print("Invalid Input...please retry")

WIN = True
