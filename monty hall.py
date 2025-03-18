import random
reply = None
revealed = None
cont = 0
slots = [1, 2, 3]
answer = random.randint(1, 3) #randomize correct answer 1-3

def check_reply(reply):
    global revealed, cont #for access
    try:
        reply = int(reply) #turn input into int for processing
        if reply in [1, 2, 3]: #is it within range
            if reply != revealed: #was it not revealed
                cont = 1 #then continue
            else:
                cont = 0
                print("Enter something that wasn't revealed.\n")
        else:
            cont = 0
            print(f"{reply} is invalid - fail, enter numbers 1, 2, or 3. Retrying...\n")
    except ValueError:
        cont = 0
        print("Invalid input, please enter a number.\n")

if answer in slots: #remove answer from slots for processing
    slots.remove(answer)

while cont != 1: #ask user for valid number 1-3
    reply = input("Between 3 doors, only in one lies the treasure. Enter a number 1-3.\n")
    check_reply(reply)

reply = int(reply) #string to int for processing
if reply in slots: #can be skipped if player correct
    slots.remove(reply)
    revealed = slots[0]
    print(f"{revealed} is empty. You have another chance to choose.\n")
    cont = 0
    while cont != 1:
        reply = input("Between 3 doors, only in one lies the treasure. Enter a number 1-3.\n")
        check_reply(reply)

if int(reply) == int(answer):
    print("Success! You got the treasure.\n")
else:
    print("Fail, better luck next time.\n")

