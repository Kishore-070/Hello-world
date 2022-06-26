print("\n")

print("                 WELCOME TO THE GAME *MONEY HUNT*")
print("\n")
print("              COME ON GEAR UP YOURSELF TO HUNT MODE")
print("\n")
print("In this game you can earn upto 1 crore  ")
print("\n")
print("There are three rounds in total in this game")
print("\n")
print("                LETS START THE GAME")
print("\n")
print("                  ROUND 1")
print("\n")
print("This is a simple round . In this round there will be 5 questions ")
print("You can earn upto 250000 in this round")
print(" correct = gain   wrong=loss")
print("\n")
money=0
prizes=[0,10,100,1000,10000,25000,50000]
import random
a=random.choice(prizes)

print("                    Question1")

print(" who is the captain of csk")
print("1=kohli   2=dhoni   3=rohit  4=sachin")
print("\n")
q1=int(input("enter your choice"))
if q1==2:
	money=a
	print("congratulations you have won",a)
else:
	print("oops! you have lost",a)	
print("your amount=",money)
print("\n")

print("                    Question 2")
print("which game ranks 1 in play store")
print("1=freefire   2=clash of clans  3=call of duty   4=pubg")
b=random.choice(prizes)
print("\n")
q2=int(input("enter your choice"))
if q2==4:
	money=money+b
	print("wow! you have won",b)
else:
	money=money-b
	print("sorry wrong answer you have lost",b)
print("now your amount=",money)
print("\n")

print("                  Question 3")
print("In the word *FIFA* the abbrevation for the first F is")
print("1=federation   2=football   3=foriegners   4=foul")
c=random.choice(prizes)
print("\n")
q3=int(input("enter your choice"))
if q3==1:
	money=money+c
	print("lucky you have won",c)
else:
	money=money-c
	print("alas! you have lost",c)
print("now your amount=",money)
print("\n")

print("                  Question 4")
print("who is your favorite cricketer")
print("1=Abd   2=rohit   3=dhoni  4=kohli")
d=random.choice(prizes)
print("\n")
q4=int(input("enter your choice"))
if q4==3:
	money=money+d
	print("GRT you have won",d)
else:
	money=money-d
	print("oops you have lost",d)
print("your remaining amount",money)
print("\n")

print("                     Question 5")
print("Translate the word *VERITHANAM* in english")
print("1=furious   2=madly   3=anger   4=powerful")
e=random.choice(prizes)
print("\n")
q5=int(input("enter your choice"))
if q5==2:
	money=money+e
	print("wow! you have won",e)
else:
	money=money-e
	print("OMG you have lost",e)
print("now your amount is =",money)
print("\n")


print("                    ROUND 2")
print("\n")
print(" In this round you you have 3 divisions")
print("\n")
print("you can earn upto 6000000 in this round")
print("\n")

prizes2=[0,1000,10000,25000,50000,75000,100000,500000,1000000]

print("                   DIVISION 1")
print("\n")
print("This is a bonus round for you")
print("you will have 3 chances you will not going to lose  money here.. only gaining ")
print("\n")

print("Enter a number between 1 to 10")
print("\n")
num=int(input("Enter a number"))
f=random.choice(prizes2)
print("you got",f)
money=money+f
print("\n")

num2=int(input("Enter a number"))
g=random.choice(prizes2)
print("nice you have won",g)
money=money+g
print("\n")

num3=int(input("Enter a number"))
h=random.choice(prizes2)
print("wow you got",h)
money=money+h
print("\n")

print("                   DIVISION 2")

print("NOW ITS TIME TO USE YOUR BRAIN TO GAIN    ELSE  LOSE ")
print("\n")
print("In this division you will have 3 question .. answer coorectly for gaining else lose your money")
print("\n")

print("                     Question 1")
print("which tournament is not conducting in india")
print("1=Baseball     2=football    3=cricket    4=kabadi")
print("\n")
q6=int(input("Enter your choice"))
i=random.choice(prizes2)
if q6==1:
	money=money+i
	print("excellent you have won",i)
else:
	money=money-i
	print("ohh you have lost",i)
	print("\n")
print("                   Question 2")	
print("Cristiano ronaldo belongs to which country ")

print("1=spain    2=argentina     3=brazil     4=portugul")
print("\n")
q7=int(input("Enter your choice"))
j=random.choice(prizes2)
if q7==4:
	money=money+j
	print("nice you got",j)
	
else:
	money=money-j
	print("alas! you have lost",j)
	print("\n")
	
print("                  Question 3")	
print("How much time does sun rays take to reach earth")

print("1=6mins   2= 8 mins  3=5 mins  4=7mins")
k=random.choice(prizes2)
print("\n")
q8=int(input("Enter your choice"))
if q8==2:
	money=money+k
	print("you have won",k)
else:
	money=money-k
	print("you have lost",k)
print("\n")

print("                  DIVISION 3")
	
print("Now its time to see how much bad luck you have")
print("\n")
print("In this division you are going to lose your money .. your luck only will decide how much amount you are going to lose ")
print("\n")
print("Enter a number between 1 to 10")
print("\n")
num4=int(input("Enter a number"))
l=random.choice(prizes2)
print("you have lost",l)
money=money-l
print("\n")

num5=int(input("Enter your choice"))
m=random.choice(prizes2)
print("your lost amount is ",m)
money=money-m
print("\n")

num6=int(input("Enter a number"))
n=random.choice(prizes2)
print(n,"has been deducted from your amount")
money=money-n
print("\n")




print("                  ROUND 3")

print(" NOW ITS TIME TO SCORE SOME RUNS ")
print("\n")
print("In this round you are going to bat ")
print("you will get money according the runs you had scored ")
print("\n")
print("You will have 20 balls ")
print("score above 50--250000    above 100--500000   above 150-- 750000    above 200--2000000")
print("\n")
print("                      LETS GO")
print("\n")

import random
score=0
no=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,20):
	comp=random.choice(no)
	player=int(input("enter a number"))
	score=score+player
	print("opponents no",comp)
	print("your score",score)
	if player==comp:
		print(" oops! youre out")
		break 
print("your total score",score)	
print("\n")
    
    	
if score>50<100:
	money=money+250000
	print("you have won 250000")
elif score>100<150:
	money=money+500000
	print("you have won 500000")
elif score>150<200:
	money=money+750000
	print("you have won 750000")
elif score==200:
	money=money+2000000
	print("you have won 2000000")
elif score<50:
	money=money-100000
	print("oops you have lost 100000")
print("\n")
if money<0:
	money=0
	
print("NOW WE HAD ENTERED INTO THE LAST STAGE ")
print("There is a small twist here")
print("\n")
print("you don't know how much amount you have got from this game")
print("It may be more or less")
print("\n")
print("now you have a choice ")
ASS=[100000,200000,300000,500000,1000000]
OO=random.choice(ASS)
print("WE ARE GIVING YOU A  ASSURED MONEY =",OO)
print("\n")
print("If you want to get the assured money enter 2 .. or  if you want your hunted money enter 1")
print("\n")
final=int(input("Enter a number"))
if final==2:
	print("You got your assured money ",OO)
print("\n")
print("Your hunted amount is",money)
if final==1:
	print("NICE GUTS ..your hunted amount is",money)
print("\n")
print("DO YOU LIKE THIS GAME??")
print("IF yes enter 7 .. if NO enter 1")
print("\n")
dho=int(input("Enter your choice"))
print("\n")
if dho==7:
	money=money+100000
	print(" HURRAY you have received a bonus amount=100000")
print("\n")
print("Now your final amount is ",money)
print("\n")

print("WE HOPE YOU ARE HAPPY NOW ")
print("                YOU HUNTED MERCILESSLY")
print("\n")
print("                 THANK YOU")

	
	

	


		

	
	
	


	

				
												