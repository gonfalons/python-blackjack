### Blackjack:

[see Wikipedia for full rules](https://en.wikipedia.org/wiki/Blackjack)

Use classes to replicate a game of blackjack as part of a bootcamp project in Python3.
[Random module which is designed for modeling and speed for simulations, not security.](https://docs.python.org/3/library/secrets.html)

#### Status:

Under active development

References:
[0] -- random module is insecure. it is for modeling and simulation, which is perfect for the use case as a study project only.
Refer to secrets library for a secure implementation

[1] -- Dealer plays a static strategy -- knowledge of opponents cards do not benefit the dealer, as he plays the same regardless of any cards shown. (except blackjack)

[1a] - blackjack means an instant 1.5:1 return on wager;
bet $10 receive $10 back + winnings of $15 = $25

[2] - An ace is required in the initial hand for 21 points -- a blackjack. Aces also act as the only two-value card. They are the best of 1 point or 11 points. If you reach over 21 points (22 points or greater is called a BUST and a dead hand.

The exception is if you had an ace--
for example:

\_Dealt: Ac 4h for 15 points
hit(): take another card. receive 7c for 22 points. Would normally bust,
but now Ac is worth 1 point, rather than 11 points. Score is now 22-10 and player has 12 points and can continue.


[3] --  
https://mikeaponte.com/game-selection/hit-soft-17-friend-or-foe/

Below are the dealer outcome probabilities for a 6-deck shoe for stand soft 17 versus  hit soft 17.*



                          18              19            20              21           Bust

Stand Soft 17    14.62%    14.04       18.85%     7.65%       29.60%

Hit Soft 17        14.82%    14.24       19.06%     7.86%       30.00%

 

As you can see, when the dealer hits soft 17 rule is in effect there is a greater probability the dealer will draw to 18, 19, 20, or 21.  The net result of the hit soft 17 rule is that it adds .22% to the house edge.  All else being equal your odds are better when the dealer stands on soft 17.
### Use:

Python3.6+ with pytest, random, logging modules
