print("""
I Can Cook Day choose your own adventure by BL '23
Story: You are stranded in a forest. Your plane has crashed while flying to Argentina and you don't know where it is. You have to create a proper meal in order to survive! Good Luck, and remember: Half a heart, but you are not through, a line to the right, now that's a two! If you don't get the congrats statement, you DO NOT WIN.
""")

#start() is used to start the game and to reset it if you choose the wrong path
def start():
  
  #Stranded in forest
  
  print("You know that water is needed to survive, but so is shelter. Do you choose to go and find a river, or stay and build a shelter?")
  x=input("Stay or Go?: ")
  print("")
  if x=="Stay" or x=="stay":
    print("While Looking for different fallen branches to build a shelter, a pinecone hits you in the head and knocks you out. \nWhen you wake, you find yourself in the mouth of some weird bear/bunny hybrid. You get eaten.")
    print("")
    start()
  else:
    print("After walking for what seemed like miles, the sound of running water catches your ear. Sprinting to the river, you drop a random, meaningless coin. \nWhen there, you remember where your water bottle is. \nDo you choose to stay and make camp, or go back and get your water bottle? ")
    
  #Decide on stay or go find water
  y=input("Stay or go back: ")
  print("")
  if y=="stay" or y=="Stay":
    print("After Drinking From the Water, you randomly die of dysentary.")
    print("")
    start()
  else: 
    print("When walking back, you stumble across a bright berry bush that, to your knowledge, looks fairly poisonous. Do you choose to take it for a snack, or leave it be?")

  #Choose To take or leave berries
  z=input("Leave it or take it: ")
  print("")
  if z=="Leave it" or z=="leave it" or z=="Leave It":
   print("")
   print("After getting hungry, you have nothing to do but wander into the forest. After getting lost, you die by falling into a random pit of tigers. Wait, really?")
   start()
  else:
   print("Cautiously, you grab the berries and head on. After getting back to where you woke up, you set the berries down in a little hole. \nAfter looking for the water bottle and finding nothing, you are debating whether or not to go get food.")
   
  #Go out for food or not
  a=input("Stay or go get food?: ")
  print("")
  if a=="Stay" or a=="stay":
    
    print("After staying, you try to eat the berries only to find out that they are indeed poisonous. You are now dead.")
    start()
  else:

    print("After walking over leaves and branches for a while, you come across a dead squirrel.")
    
  #Take the squirrel? 
  
  b=input("Do you take it or leave it be?: ")
  print("")
  if b=="Leave it" or b=="leave it" or b=="Take It":
    print("After leaving the squirrel, you go back and eat the berries, but they are indeed poisonous. You dead.")
    start()
  else:
    print("Trying to hold your vomit back, you take the dead squirrel back to where you woke up. After making a fire and cooking and eating the squirrel, \nyou fall asleep. You wake up to the sound of voices, and you turn over to see Ryan Reynolds drop down from a helicopter and save you! \nHe sweeps you up and you ascend up into the helicopter where Arnold Schwarzenegger and Keanu Reeves are up there. Surrounded by celebrities, you travel back to civilization!")
   
    #This is where the game ends, because it TOTALLY isn't obvious already.
start()

w=0
#No matter what, they get this wrong.
while w==0:
  c=input("Do You Wish To Leave The Game or Gain 1,000,000 Dollars? Take the money or leave: ")
  print("")
  if c=="Take the money" or c=="take the money":
    w=2
  else:
    w=1

for w in range(2,3):
    d=int(input("You Greedy Boi. Ight U Bout To Head Out. Press 1 to restart:  "))
    w=0
if d==1:
  start()
  

if d==2:
  print("Congrats! You Found the Secret Ending! Thanks For Playing!")
