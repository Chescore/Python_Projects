print("Welcome to the Love Calculator")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")
 
true = str(t+r+u+e)
love = str(l+o+v+e)
truelove = int(true + love)

if truelove<10 or truelove>90:
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove>40 and truelove<50:
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}")