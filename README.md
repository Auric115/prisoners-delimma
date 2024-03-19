# Prisoner's Dilemma Simulation

This Python code simulates the classic game theory scenario known as the Prisoner's Dilemma. The code provides implementations for different types of players, including:

- `Player`: A basic player who makes random decisions with a 50% probability. This is the parent class for the following players.
- `PassivePlayer`: A player who tends to cooperate with a probability of 20%.
- `AggressivePlayer`: A player who tends to defect with a probability of 80%.
- `TitForTatPlayer`: A player who initially cooperates and then mimics the opponent's previous move.

## How the Game Works

William Poundstone described this "typical contemporary version" of the game in his 1993 book Prisoner's Dilemma:
  Two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of speaking to or exchanging messages with the other. 
  The police admit they don't have enough evidence to convict the pair on the principal charge. They plan to sentence both to a year in prison on a lesser charge. 
  Simultaneously, the police offer each prisoner a Faustian bargain. If he testifies against his partner, he will go free while the partner will get three years in prison on the main charge. 
  Oh, yes, there is a catch ... If both prisoners testify against each other, both will be sentenced to two years in jail. The prisoners are given a little time to think this over, 
  but in no case may either learn what the other has decided until he has irrevocably made his decision. Each is informed that the other prisoner is being offered the very same deal. 
  Each prisoner is concerned only with his own welfare—with minimizing his own prison sentence.

## Running the Simulation

The `main()` function orchestrates the simulation. It pits each type of player against all others in a series of epochs (rounds) where each player faces each other player 10,000 times. The total scores for each player are then printed.

## Understanding the Output

The output of the simulation shows the results of each matchup between players. For each pair of players, the counts of wins, losses, and draws are displayed, along with the player who won the most rounds.

## Observations

- The simulation allows for observing how different player strategies fare against each other.
- It provides insights into the dynamics of cooperation and competition in repeated interactions.
- It can be used to analyze the effectiveness of various strategies in different scenarios.

By adjusting the probabilities in player decision-making, the simulation can be adapted to explore various aspects of the Prisoner's Dilemma and related game theory concepts.
  
