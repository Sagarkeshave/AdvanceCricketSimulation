# importing random package
import random


class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        """
        Represents a player in a cricket team.
        Initialize a Player object with the provided attributes.

        Args:
            name (str): The name of the player.
            bowling (float): The bowling skill of the player.
            batting (float): The batting skill of the player.
            fielding (float): The fielding skill of the player.
            running (float): The running skill of the player.
            experience (float): The experience level of the player.
        """
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience


class Team:
    def __init__(self, name, players):
        """
        Initialize a Team object with the provided attributes.

        Args:
            name (str): The name of the team.
            players (list): The list of Player objects representing the team's players.
        """
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = players.copy()
        self.bowlers = []

    def select_captain(self, captain):
        """
        Select the captain for the team.

        Args:
            captain (Player): The Player object representing the captain of the team.
        """
        self.captain = captain

    def sending_next_player(self):
        """
        Send the next player from the batting order.

        Returns:
            Player or None: The next Player object from the batting order, or None if the batting order is empty.
        """
        if len(self.batting_order) > 0:
            return self.batting_order.pop(0)
        return None

    def choose_bowler(self):
        """
        Choose a bowler randomly from the team's bowlers.

        Returns:
            Player: The Player object representing the chosen bowler.
        """
        return random.choice(self.bowlers)


class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        """
        Initialize a Field object with the provided attributes.

        Args:
            size (str): The size of the field.
            fan_ratio (float): The fan ratio of the field.
            pitch_conditions (float): The pitch conditions of the field.
            home_advantage (float): The home advantage of the field.
        """
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage


class Umpire:
    def __init__(self, field):
        """
        Initialize an Umpire object with the provided attributes.

        Args:
            field (Field): The Field object representing the field conditions.
        """
        self.field = field
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def update_score(self, runs):
        """
        Update the score based on the runs scored.

        Args:
            runs (int): The runs scored in the ball.
        """
        self.scores += runs

    def update_wickets(self):
        """
        Update the wickets count.
        """
        self.wickets += 1

    def update_overs(self):
        """
        Update the overs count.
        """
        self.overs += 1

    def predict_outcome(self, batsman, bowler):
        """
        Predict the outcome of a ball based on batsman and bowler stats.

        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.

        Returns:
            str: The outcome of the ball (either "OUT" or "NOT OUT").
        """
        batting_prob = batsman.batting * self.field.pitch_conditions
        bowling_prob = bowler.bowling * self.field.pitch_conditions
        if batting_prob > bowling_prob:
            return "NOT OUT"
        return "OUT"


class Commentator:
    def __init__(self, umpire):
        """
        Initialize a Commentator object with the provided attributes.

        Args:
            umpire (Umpire): The Umpire object providing match information.
        """
        self.umpire = umpire

    def describe_ball(self, batsman, bowler):
        """
        Generate a description of the ball played by the batsman.

        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.

        Returns:
            str: The description of the ball played by the batsman.
        """
        outcome = self.umpire.predict_outcome(batsman, bowler)
        print("Outcome: ", outcome)
        if outcome == "OUT":
            description = f"{batsman.name} is OUT!"
        else:
            description = f"{batsman.name} plays the shot."

        return description

    def describe_game(self, captain1, captain2, team1, team2, over):
        """
        Provide a description of the cricket match.

        Args:
            captain1 (str): The name of the captain of the first team.
            captain2 (str): The name of the captain of the second team.
            country1 (str): The name of the first team.
            country2 (str): The name of the second team.
            over (int): The total number of overs in the match.
        """
        print("\n--------- Game Information ---------\n")
        print(f"{team1} Vs {team2}")
        print(f"Captain 1 : {captain1}, Captain 2 : {captain2}")
        print(f"Over : {over}")
        print("\n---------------------------------------------\n")

    def describe_start(self, team):
        """
        Provide a description of the start of an innings.

        Args:
            team (str): The name of the team currently batting.
        """
        print("\n------------- GAME STARTED ------------------\n")
        print(f"Team {team} playing: ")



    def describe_end(self):
        """
        Provide a description of the end of an innings.
        """
        print(f"\n\nCurrent batting team Score --- Runs: {self.umpire.scores} Wickets: {self.umpire.wickets} in Overs: {self.umpire.overs}")
        print("\n---------------------------------------------\n")

    def current_info(self, ball_count):
        """
        Provide the current match information.

        Args:
            ball_count (int): The count of balls played in the current over.
        """
        print(f"Balls: {ball_count} Over: {self.umpire.overs} Run: {self.umpire.scores}  Wicket: {self.umpire.wickets}")

    def describe_final_result(self, name, scores):
        """
        Provide a description of the final result of the match.

        Args:
            name (str): The name of the winning team.
            scores (int): The```
            score achieved by the winning team.
        """
        print("--------------- Winner -----------------------")
        print(f"TEAM : {name} WON BY SCORE: {scores}")
        print("\n---------------------------------------------\n")


class Match:
    def __init__(self, team1, team2, field, total_overs):
        """
        Represents a cricket match between two teams.

        Args:
            team1 (Team): The Team object representing the first team.
            team2 (Team): The Team object representing the second team.
            field (Field): The Field object representing the field conditions.
            total_overs (int): The total number of overs in the match.
        """
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(field)
        self.commentator = Commentator(self.umpire)
        self.total_overs = total_overs

    def start_match(self):
        """
        Starts the cricket match.
        """
        self.team1.select_captain(random.choice(self.team1.players))
        self.team2.select_captain(random.choice(self.team2.players))
        self.team1.batting_order = self.team1.players.copy()
        self.team2.batting_order = self.team2.players.copy()
        self.team1.bowlers = self.team1.players.copy()
        self.team2.bowlers = self.team2.players.copy()

        self.commentator.describe_game(self.team1.captain.name, self.team2.captain.name, self.team1.name,
                                       self.team2.name, over=self.total_overs)

        # Team 1 playing
        self.commentator.describe_start(self.team1.name)
        self.play_innings(self.team1, self.team2)
        self.commentator.describe_end()
        team1_score = self.commentator.umpire.scores

        # Team 2 playing
        self.commentator.umpire.scores = 0
        self.commentator.umpire.wickets = 0
        self.commentator.umpire.overs = 0
        self.commentator.describe_start(self.team2.name)
        self.play_innings(self.team2, self.team1)
        self.commentator.describe_end()
        team2_score = self.commentator.umpire.scores

        # Final outcome
        if team1_score > team2_score:

            self.commentator.describe_final_result(team1.name, (team1_score-team2_score))
        else:
            self.commentator.describe_final_result(team2.name, (team2_score-team1_score))

    def play_innings(self, batting_team, bowling_team):
        """
        Simulates the innings of a team.

        Args:
            batting_team (Team): The Team object representing the batting team.
            bowling_team (Team): The Team object representing the bowling team.
        """
        ball_count = 1
        over = 0
        bowler = bowling_team.choose_bowler()
        batsman = batting_team.sending_next_player()

        while over < self.total_overs:
            print("\n")
            self.commentator.current_info(ball_count)
            ball_description = self.commentator.describe_ball(batsman, bowler)

            print(ball_description)
            if ball_description.endswith("OUT!"):
                batsman = batting_team.sending_next_player()
                if batsman is None:
                    break
                self.umpire.update_wickets()
                print(f"Wickets: {self.umpire.wickets} , Overs: {self.umpire.overs}")
                print(f"New player {batsman.name} is playing...")
            else:
                runs = random.randint(0, 6)
                self.umpire.update_score(runs)

            if ball_count > 5:
                over += 1
                print(f"Over {over} Starting...")
                self.umpire.update_overs()
                bowler = bowling_team.choose_bowler()
                ball_count = 0

            self.commentator.current_info(ball_count)
            ball_count += 1



players_1 = [
    Player("MS Dhoni", 0.2, 0.8, 0.99, 0.8, 0.9),
    Player("Virat Kohli", 0.1, 0.9, 0.95, 0.85, 0.95),
    Player("Rohit Sharma", 0.3, 0.85, 0.9, 0.82, 0.88),
    Player("AB de Villiers", 0.1, 0.92, 0.92, 0.88, 0.87),
    Player("Kane Williamson", 0.85, 0.85, 0.88, 0.8, 0.92),
    Player("Joe Root", 0.7, 0.87, 0.87, 0.78, 0.86),
    Player("Steve Smith", 0.3, 0.88, 0.89, 0.81, 0.89),
    Player("David Warner", 0.2, 0.9, 0.85, 0.83, 0.87),
    Player("Jasprit Bumrah", 0.9, 0.1, 0.8, 0.7, 0.82),
    Player("Mitchell Starc", 0.85, 0.1, 0.75, 0.7, 0.84),
    Player("Rashid Khan", 0.8, 0.1, 0.7, 0.75, 0.81)]

players_2 = [ Player("Ben Stokes", 0.7, 0.78, 0.85, 0.85, 0.85),
    Player("Shakib Al Hasan", 0.85, 0.77, 0.88, 0.8, 0.83),
    Player("Kagiso Rabada", 0.9, 0.1, 0.78, 0.75, 0.86),
    Player("Chris Gayle", 0.1, 0.9, 0.7, 0.7, 0.78),
    Player("Andre Russell", 0.7, 0.7, 0.8, 0.8, 0.75),
    Player("Faf du Plessis", 0.3, 0.78, 0.86, 0.75, 0.83),
    Player("Quinton de Kock", 0.3, 0.82, 0.85, 0.8, 0.81),
    Player("Babar Azam", 0.1, 0.85, 0.82, 0.8, 0.84),
    Player("Eoin Morgan", 0.4, 0.8, 0.83, 0.75, 0.87),
    Player("Dwayne Bravo", 0.8, 0.89, 0.81, 0.72, 0.80),
    Player("Yuvi Singh", 0.7, 0.87, 0.82, 0.74, 0.86)
]


# Adding players to team
team1 = Team("CSK", players_1)
team2 = Team("MI", players_2)

# showing the field
field = Field("Large", 0.7, 0.8, 0.9)

# starting match simulation
total_overs = 2
match = Match(team1, team2, field, total_overs)
match.start_match()