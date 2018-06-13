import random
random.seed()

games = 10
door_cnt = 3

wins_stay = 0
wins_switch = 0
count_switch = 0
count_stay = 0
loss = 0
doors = range(1, door_cnt+1)

def show(msg):
    if games <= 100:
        print msg

i = 0
while i < games:
    i += 1
    prize = random.randint(1, door_cnt)
    guess = random.randint(1, door_cnt)
    switch = random.randint(0, 1) == 1
    # remove a door that isn't a winner and isn't the guess
    show_door = list(set(doors) - set([guess]) - set([prize]))[0]
    #print doors
    #print guess
    #print prize
    #print show_door
    show("Prize: %d  Guess: %d  Show door: %d  Switch: %d" % (prize, guess, show_door, switch))
    # should we switch our guess
    if switch:
        count_switch += 1
        guess = list(set(doors) - set([guess]) - set([show_door]))[0]
        if prize == guess:
            wins_switch += 1
            show("Switched to %d and won" % (guess))
        else:
            loss += 1
            show("Switched to %d but prize was behind %d" % (guess, prize))
    else:
        count_stay += 1
        if prize == guess:
            wins_stay += 1
            show("Stayed and won")
        else:
            loss += 1
            show("Stayed with %d but prize was behind %d" % (guess, prize))

loss_pct = loss / float(games) * 100;
print "Games: %d  Loss: %d  Loss Pct: %0.2f" % ( games, loss, loss_pct )
if count_switch == 0:
    pct_switch = 0
else:
    pct_switch = wins_switch / float(count_switch) * 100
print "Switch Wins: %d / Switch Total: %d = %.2f switch win pct  " % ( wins_switch, count_switch, pct_switch )
if count_stay == 0:
    pct_stay = 0
else:
    pct_stay = wins_stay / float(count_stay) * 100
print "Stay Wins: %d / Stay Total: %d = %.2f stay win pct  " % ( wins_stay, count_stay, pct_stay )
