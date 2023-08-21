"""
import time
def tax_calculator(hourly_rate,num_hours,tax_bracket):
    weekly_salary=hourly_rate*num_hours
    annual_salary=weekly_salary*52
    posttax_salary=annual_salary*(1-tax_bracket)
    return posttax_salary

msg='''
Hello, I am a robot...

My job is to calculate your annual salary post tax

To do this, I will require some info.
'''
print(msg)
time.sleep(5)

Question_1=input("would you like me to calculate your post tax salary??")
print(Question_1)
if Question_1=='yes':
    print("nice")
else:
    print("No problem, Have a nice day")


"""
"""
def deposit_calculator(credit_status,houseprice):
    if credit_status=='good':
        deposit=houseprice*0.1
    else:
        deposit=houseprice*0.2
    return deposit
    
x=deposit_calculator('not good',1000000)
y=str(x)
print(f"Deposit Amount: {y}")
"""
"""
def eligibility_status(has_good_credit,has_criminal_record):
    if has_good_credit and not has_criminal_record:
        print('Congrats! \n You are eligible')
    else:
        print('Fuck off you stupid little cunt')


John=eligibility_status(True, True)
"""
"""
def name_status(name):
    if len(name)<3:
        print('name too short')
    elif len(name)>50:
        print('your name too long')
    else:
        print(f"yoooo\n sup {name}")


x=name_status('summalumma dumamambfjsa ssaf hasg fashg fiasufsdfhjkasfhifjash fsa')
"""
"""
i=1
while i<=16:
    print(':)'*i)
    i=i+1

print('niice')
"""
"""
#making a guessing game using while loops
the_answer=9
guess_count=0
while guess_count<3:
    guess=input("Guess:")
    guess_count=guess_count+1
    if int(guess)==the_answer:
        print("Nice job dude")
        break
else:
    print("sorry, you have exceeded your guess limiit")

"""

#Building the Engine for a car game


"""
help_msg='''
Start-to start the car
stop- to stop the car
quit
'''
car_started=False
command=""

while command !="quit":
    command=input(">" ).lower()
    if command.lower()=='help':
        print(help_msg)
    elif command=='start':
        if car_started: 
            print('car already started')
        else:
            car_started=True
            print('car moving')
    elif command=='stop':
        if not car_started:
            print("Car has already stopped")
        else:
            car_started=False
            print('car has stopped')
    elif command=='quit':
        print('you quit')
        break
    else:
        print('sorry idk what you mean')
"""
"""
#This is a simple example of using a for loop 
prices=[10,20,30]
total=0
for price in prices:
    total+=price
print(f"Total: {total}")
"""
"""
#nested for loops example

for x in range(4):
    for y in range(4):
        for z in range(4):
            print(f"{x},{y},{z}")     
             
"""
"""
#use a for loop to find the max number in a list
list=[10,982,3,43,543,67,5744,2,3,4536,457,4,2,3253,53,445,57,4,42,3,2443,546,463,43]

max=list[0]
for number in list:
    if number>max:
        max=number
        print(max)
"""
"""
#Below is a bit of code that is capable of removing all of the duplicates in the below code
list=[1,2,3,1,2,2,2,2,3,3,1,1,1,2,2,3,5,6,6]
new_list=[]
for number in list:
    if number not in new_list:
        new_list.append(number)

print(new_list)
"""
"""
#writing a bit of code which changes number to words
#eg. 1 --> one

number_word_conversion={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven'}
user_input=input("Enter your numbers:")

output=""
for ch in user_input:
    output+=number_word_conversion[:]

print(output)
"""
"""
#create a class called person

class Person:
    def __init__(self,name)
        self.name=name
    def talk(self):
        print('sup dog')

jon=Person()
jon.talk()

"""
"""
#this is ChatGPTs take on the guessing game, which is actually better than the code with mosh one
import random

def guessing_game():
    secret_number = random.randint(1, 10)
    max_guesses = 3
    guesses_taken = 0
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    while guesses_taken < max_guesses:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        guesses_taken += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {guesses_taken} guesses.")
            break
    
    if guesses_taken == max_guesses and guess != secret_number:
        print(f"Sorry, you've used all your guesses. The secret number was {secret_number}.")

guessing_game()

"""
"""
#making a dice
#make a class called dice
#within class make a method called roll which gives you a tuple
import random
class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second


dice=Dice()
print(dice.roll())
"""
"""
from pathlib import Path
#checking all of the files within the current directory
path=Path()
for file in path.glob('*'):
    print (file)
    
"""
"""
#fizzbuss game

def fizz_buzz(number):
    if number%3==0 and number%5==0:
        print('FizzBuzz')
    elif number%5==0:
        print('Buzz')
    elif number%3==0:
        print('Fizz')
    else:
        return number


x=fizz_buzz(3)
"""
"""
names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]

for name in names1:
    if name not in names2 and names1:
        names2.append(name)
        print(names2) 
        """



  
"""
def estimate_average_slot_payout(n_runs):
    i=0
    collective_sum=0
    for i in n_runs:
        i=i+1
        print(collective_sum+=i)
        
        return collective_sum
    

n_runs=[0,0,0,0,1.5,1.5,60]
print(estimate_average_slot_payout(n_runs))
"""
# list1=[1,1,2,3,4,5,6,5,4,3,5,6,7,8,10,2,3,4,5,6,7,2,2]

# new_list=[]

# for num in list1:
#     if num  not in new_list:
#         new_list.append(num)

# print(new_list)


#let's make a quick guessing game
import datetime

print('hello world')