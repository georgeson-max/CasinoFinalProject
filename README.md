# Welcome to the casino!

Admittedly, it's not a very exciting casino, as the only game here is roulette. And a slightly simplified, European verson at that. Here's an overview:

Roulette is a casino game that has a spinning wheel with 37 divisions on it, labelled 0-36, and each of which is color coded red or black (except 0, which is green, and results in a loss regardless of the bet). The wheel is spun and a small ball is rolled into it, and whichever division the ball lands in when the wheel is done spinning decides the bets. This is what it looks like:

![image](https://user-images.githubusercontent.com/66698837/165361918-dd0dd038-0287-4818-8dc3-a453b6340405.png)

There are three types of bets with three different odds in this version: **even bets**, which include betting on red versus black, even versus odd, or low (1-18) versus high (19-36), and pay out 1 to 1; **dozen bets**, which allow you to to place a bet on either the first dozen (1-12), second dozen (13-24), or third dozen (25-36), and pay out 2 to 1; and **straight up bets**, where you pick a number between 1 and 36, and it pays out 35 to 1. For our purposes, the player will have a set amount of money assigned to them, their bank, that they can wager on spins of the roulette wheel through the command line interface. 

## Gameplay 
First, the above bets are explained, and then the player is prompted to choose between an even bet, a dozen bet, or a straight up bet. Depending on their answer, the player gets to choose one of the specific bets listed above for each bet type. Then the player is asked how much they'd like to bet, and the wheel is spun and the result is displayed. If the player wins, the amount they wagered multiplied by the odds of their bet is added to their bank, and they are asked if they'd like to play again.

## Automated Testing
Using GitHub actions, every time new code is pushed, all of the code is automatically linted and tested using a virtual Ubuntu machine hosted by GitHub. As it stands, the test coverage is shown below:


|Name           |Stmts   |Miss  |Cover|
|---------------|--------|------|-----|
|classes.py       |193     |14    |93%|
|main.py          |29      |26    |10%|
|test_main.py     |244     |1     |99%|
|TOTAL            |466     |41    |91%|

This can be checked for every new push, under the Actions tab and in the "Test with pytest" section of the job. I don't think the coverage of the test file itself is really all that relevant, so for all intents and purposes, the total statements should be 222 and the total number of misses should be 40. This means that **the practical code coverage is ~82%**. Basically all of the missed coverage is in the main file, because it mostly just organizes the functions, as well as some in menus where an unacceptable input causes the menu to loop until there's a valid input, which is very difficult to test without having the test run forever. 

## Automated Deployment
Another thing this GitHub Workflow does is automatically update a Docker container which contains all of this code. This allows you to play the game anywhere you can run Docker containers, as it contains all of the necessary dependencies within it. It is public, so you just have to type `docker pull maxgeorgeson/casino` into your CLI, and then you can play it with `docker run --interactive maxgeorgeson/casino`

Enjoy!
