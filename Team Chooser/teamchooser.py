from random import choice

players = ['Harry', 'Luna', 'Neville', 'Hermione', 'Ginny', 'Fred']
print(players)

teamA = []
teamB = []

while len(players) > 0:
  playerA = choice(players)
  teamA.append(playerA)
  players.remove(playerA)

  playerB = choice(players)
  teamB.append(playerB)
  players.remove(playerB)

print("TeamA:", teamA)
print("TeamB:", teamB)
