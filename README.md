
I don't get monty-hall, I hoped coding a simulation would make it obvious but instead it shows what everyone says is the wrong answer.

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
