# rock-paper-scissors
A python script simulating two player playing rock-paper-scissors with multiple strategies

In a [video from Numberphile](https://www.youtube.com/watch?v=rudzYPHuewc) [Hannah Fry](https://en.wikipedia.org/wiki/Hannah_Fry) talks about the game rock-paper-scissors or more specifically about a strategy one can use to increase the chances of winning.  

Inspired by this I wrote this small python script to simulate two players playing against each other with different strategies.

Here is an example result of the script.
```
Situation 1: Both choose randomly
Player 1 wins:  356 = 35.6%
Player 2 wins:  330 = 33.0%
Draws:          314 = 31.4%

Situation 2: Player 1 chooses randomly, Player 2 is strategic
Player 1 wins:  351 = 35.1%
Player 2 wins:  354 = 35.4%
Draws:          295 = 29.5%

Situation 3: Player 1 keeps move if won, Player 2 is strategic
Player 1 wins:  218 = 21.8%
Player 2 wins:  408 = 40.8%
Draws:          374 = 37.4%

Sitation 4: Player 1 keeps move if won, Player 2 is strategic but changes move at draws
Player 1 wins:  304 = 30.4%
Player 2 wins:  207 = 20.7%
Draws:          489 = 48.9%

Situation 5: Both are strategic
Player 1 wins:  357 = 35.7%
Player 2 wins:  325 = 32.5%
Draws:          318 = 31.8%
```
You can play around with the variables especially with the bias of player 1 in Situation 3 which will determine how likely the player is to keep his move when he has won. 
