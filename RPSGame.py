import random
rps=["rock","papper","Sissor"]
print(rps)
# player =input("enter your value from list ")
# print("Your selected value is "+player)
ran=rps[random.randint(0,2)]
print("genrated value is "+ran)

# make player to False
player=False
  
while player==False:
               player=input("enter your value from list ")
               print("Your selected value is "+player)
               if player==ran:
                              print("match is Tie!")
               elif player=="rock":
                              if ran=="papper":
                                             print("Your loos!")
                              else :
                                             print("You Win!")

               elif player=="papper":
                              if ran=="rock":
                                             print("Your win!")
                              else :
                                             print("You loss!")



               elif player=="papper":
                              if ran=="Sissor":
                                             print("Your loos!")
                              else :
                                             print("You Win!")


               elif player=="Sissor":
                              if ran=="rock":
                                             print("Your loss!")
                              else :
                                             print("You Win!")

               elif player=="rock":
                              if ran=="Sissor":
                                             print("Your Win!")
                              else :
                                             print("You loss!")



               elif player=="papper":
                              if ran=="rock":
                                             print("Your loos!")
                              else :
                                             print("You Win!")


                             


               
                                                            