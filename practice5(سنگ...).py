import random
game=["rock","paper","scissors",]
robot=random.choice(game)
print(robot)

user=input("enter rock or paper or scissors: ")

if robot==user:
    print("equal")
    
elif robot=="rock" and user=="scissors" and robot=="paper" and user=="rock" and robot=="scissors" and user=="paper":
    print("robot win")

elif user=="rock" and robot=="scissors" and user=="paper" and robot=="rock" and user=="scissors" and robot=="paper":
    print("user win")

print("robot:",robot)
print("user:",user)