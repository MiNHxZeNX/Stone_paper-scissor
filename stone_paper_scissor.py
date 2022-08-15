import random

genNum = random.randint(1,3)

userIn = input("Welcome to Stone, Paper, Scissor game!!!\nPlease choose between stone, paper scissor : ")
userInL = userIn.lower()

if userInL=="stone":
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)
    if genNum==1:
        print("The computer choose : Stone")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("\n\nIts a Draw")
    elif genNum==2:
        print("The computer choose : Paper")
        print("""
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("\n\nYou lost")
    elif genNum==3:
        print("The computer choose : Scissor")
        print("""
    _______
---'    ____)____
           ______)
           _______)
     _______)
---.______)
""")
        print("\n\nIts a Win")
elif userInL=="paper":
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """)
    if genNum==1:
        print("The computer choose : Stone")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        """)
        print("\n\nIts a Win")
    elif genNum==2:
        print("The computer choose : Paper")
        print("""
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("\n\nIts a Draw")
    elif genNum==3:
        print("The computer choose : Scissor")
        print("""
    _______
---'    ____)____
           ______)
          _______)
      _______)
---.______)
""")
        print("\n\nYou lost")
elif userInL=="scissor":
    print("""
     _______
---'    ____)____
           ______)
          _______)
    _______)
---.______)
""")
    if genNum==1:
        print("The computer choose : Stone")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("\n\nYou lost")
    elif genNum==2:
        print("The computer choose : Paper")
        print("""
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("\n\nIts a win")
    elif genNum==3:
        print("The computer choose : Scissor")
        print("""
    _______
---'    ____)____
           ______)
          _______)
      _______)
---.______)
""")
        print("\n\nIts a Draw")
else:
    print("\nWrong Input --_--\n")
