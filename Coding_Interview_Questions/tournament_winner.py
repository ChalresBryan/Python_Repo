'''tournament_winner.py'''
# pylint: disable=E1101
# pylint: disable=C0206
# pylint: disable=W0621
print(" ")

# team compete against each other in a round robin
# home and away team
# [homeTeam, awayTeam]
# 1, home team won
# 0, away team won
# one winner and loser
# no ties
# winning team receives 3 points
# team name < 30 chars

competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"]
]

results = [0, 1, 1, 1, 0, 1]


def tournament_winner(competitions, results):
    '''tournamentWinner'''
    winners = {}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition
        home_team_won = False

        if result == 1:
            home_team_won = True

        if home_team_won:
            if home_team in winners:
                winners[home_team] += 1
            else:
                winners[home_team] = 1
        else:
            if away_team in winners:
                winners[away_team] += 1
            else:
                winners[away_team] = 1

    most_wins = max(winners.values())
    for winner in winners:
        winner_score = winners[winner]

        if winner_score == most_wins:
            return winner

    return None


# O(n) time | O(k) space
HOME_TEAM_WON = 1

def tournament_winner2(competitions, results):
    '''tournament_winner2'''
    current_best_team = ""
    scores = {current_best_team: 0}

    for idx, competition in enumerate(competitions):
        results = results[idx]
        home_team, away_team = competition

        wining_team = home_team if results == HOME_TEAM_WON else away_team

        update_scores(wining_team, 3, scores)

        if scores[wining_team] > scores[current_best_team]:
            current_best_team = wining_team

        return current_best_team


def update_scores(team, points, scores):
    '''update_scores'''
    if team not in scores:
        scores[team] = 0

    scores[team] += points


print(tournament_winner(competitions, results))
print(tournament_winner2(competitions, results))

print(" ")
