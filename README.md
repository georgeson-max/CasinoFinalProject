# Welcome to the casino!

Admittedly, it's not a very exciting casino, as the only game here is roulette. And a slightly simplified, European verson at that. Here's an overview:

Roulette is a casino game that has a spinning wheel with 37 divisions on it, labelled 0-36, and each of which is color coded red or black (except 0, which is green, and results in a loss regardless of the bet). The wheel is spun and a small ball is rolled into it, and whichever division the ball lands in when the wheel is done spinning decides the bets.  For our purposes, the player will have a set amount of money assigned to them, their bank, that they can wager on spins of the roulette wheel through the command line interface. 

There will be three types of bets with three different odds: **even bets**, which include betting on red versus black, even versus odd, or low (1-18) versus high (19-36), and pay out 1 to 1; **dozen bets**, which allow you to to place a bet on either the first dozen (1-12), second dozen (13-24), or third dozen (25-36), and pay out 2 to 1; and **straight up bets**, where you pick a number between 1 and 36, and it pays out 35 to 1.

Through GitHub actions, every time new code is pushed, it is run through a testing suite. As it stands, the test coverage using this suite is shown below:


|Name           |Stmts   |Miss  |Cover|

|-------------------------------------|

|classes.py       |193     |14    |93%|

|main.py          |29      |26    |10%|

|test_main.py     |244     |1     |99%|

|-------------------------------------|

|TOTAL            |466     |41    |91%|

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |


This can be checked for every new push, under the Actions tab and in the "Test with pytest" section of the job.

Another thing this action does is update a Docker container which contains all of this code and allows you to play the game anywhere you can run Docker containers. It is public, so you just have to type `docker pull maxgeorgeson/casino` into your CLI, and then you can play it with `docker run --interactive maxgeorgeson/casino`

Enjoy!
