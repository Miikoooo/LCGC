import random, sys

#Setzt die Spieleranzahl und Anzahl der Teams fest
players, p, teams = [], int(input('Wie viele Spielen werden wieder ein qualvolles Customgame spielen: ')), int(input('Wie viele Teams wird es geben (obv. 2): '))

if p < teams:
    # Wenn eines davon =true ist wird das Programm beendet
    print('Zu viele Teams oder zu viele Spieler')
    sys.exit()

for i in range(p):
    n = input('Spieler {}: '.format(i+1))
    n = n[0].upper() + n[1:] # Der erste Buchstabe im Nanem wird groß ausgegeben
    players.append(n)
print(players)

# Erstell eine random Liste und benutzt .append in jeder leeren Liste
# dadurch wird die Größe der Team bestimmt durch list comprehension.
team_g = [list() for _ in range(teams)]

while len(players) > 0:
    for i in range(teams):
        p=random.choice(players)
        team_g[i].append(p)
        players.remove(p)
        if not players: # Wenn nicht genung Spieler angegeben werden break(ed) das Programm
            break
    continue # Schütz vor der break loop 

for i in range(teams):
    print( 'Team {} ist {}'.format(i+1, team_g[i]) )



