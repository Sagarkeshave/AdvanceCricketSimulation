# Advanced Cricket Tournament Simulation

This is a Python program that simulates a cricket tournament involving various teams with advanced level detail. The program mimics real-world cricket matches and statistics.

Live Demo :  https://youtu.be/HmhUWOhTCkQ


## Program Overview

The program consists of the following key classes:

- `Player`: Represents a player in a cricket team, with attributes such as name, bowling, batting, fielding, running, and experience.
- `Team`: Represents a cricket team, with methods for selecting a captain, sending the next player to the field, choosing a bowler, and managing the batting order.
- `Field`: Represents the field conditions, including size, fan ratio, pitch conditions, and home advantage.
- `Umpire`: Handles the umpiring and scoring of the match, predicting the outcome of a ball based on player stats.
- `Commentator`: Provides commentary for each ball and over, generating descriptions of game events.
- `Match`: Simulates an individual cricket match, using objects of the above classes to start, change innings, and end the match.


## Installation and Usage
 

1. Clone the repository:
```
git clone https://github.com/Sagarkeshave/AdvanceCricketSimulation.git
```

2. Navigate to the project directory:
```
cd AdvancedCricketTournament
```

3. Run the `main.py` file to start the simulation:
```
python main.py
```
