
I don't get monty-hall, I hoped coding a simulation would make it obvious but instead it shows what everyone says is the wrong answer.

UPDATE: Ok, bug in v1 was causing a switch to be selecting the door that was shown, and it was showing a door that may have been a winner


```
Games: 1000  Loss: 477  Loss Pct: 47.70
Switch Wins: 344 / Switch Total: 496 = 69.35 switch win pct
Stay Wins: 179 / Stay Total: 504 = 35.52 stay win pct

Games: 10000  Loss: 4950  Loss Pct: 49.50
Switch Wins: 3382 / Switch Total: 5034 = 67.18 switch win pct
Stay Wins: 1668 / Stay Total: 4966 = 33.59 stay win pct

Prize: 2  Guess: 3  Show door: 1  Switch: 1
Switched to 2 and won
Prize: 1  Guess: 3  Show door: 2  Switch: 0
Stayed with 3 but prize was behind 1
Prize: 2  Guess: 2  Show door: 1  Switch: 1
Switched to 3 but prize was behind 2
Prize: 1  Guess: 1  Show door: 2  Switch: 1
Switched to 3 but prize was behind 1
Prize: 3  Guess: 2  Show door: 1  Switch: 0
Stayed with 2 but prize was behind 3
Prize: 3  Guess: 2  Show door: 1  Switch: 0
Stayed with 2 but prize was behind 3
Prize: 3  Guess: 2  Show door: 1  Switch: 0
Stayed with 2 but prize was behind 3
Prize: 1  Guess: 3  Show door: 2  Switch: 1
Switched to 1 and won
Prize: 1  Guess: 3  Show door: 2  Switch: 0
Stayed with 3 but prize was behind 1
Prize: 3  Guess: 1  Show door: 2  Switch: 0
Stayed with 1 but prize was behind 3
Games: 10  Loss: 8  Loss Pct: 80.00
Switch Wins: 2 / Switch Total: 4 = 50.00 switch win pct
Stay Wins: 0 / Stay Total: 6 = 0.00 stay win pct
```


```
$ python ./huh.py
Games: 1000000  Loss: 666460
Switch Wins: 167013 / Switch Total: 500438 = 33.37 switch win pct
Stay Wins: 166527 / Stay Total: 499562 = 33.33 stay win pct

$ python ./huh.py
Games: 1000000  Loss: 666215
Switch Wins: 166765 / Switch Total: 499882 = 33.36 switch win pct
Stay Wins: 167020 / Stay Total: 500118 = 33.40 stay win pct
```

Odds of winning seem to follow 1/door_cnt
