import json
import sys
import os
import matplotlib.pyplot as mplot




def writeData():
	with open('data.json', 'w') as file:
		file.write(json.dumps(data, indent=3))


if os.path.exists('data.json'):
	with open('data.json', 'r') as file:
		data = json.loads(file.read())
else:
	with open('data.json', 'w') as file:
		data = {"0": {"0": "[ KrulYuno ]","1": {"0": 440,"1": 490,"2": 496,"3": 314,"4": 286,"5": 387}}}
	writeData()
	sys.exit(0)


def newPlayer(name, stamina, tenacity, agility, accuracy, precision, reaction):
	player = find_missing(list(data))
	if len(player) != 0:
		player = min(player)
	else:
		player = len(data)
	
	data[player] = {0: name, 1:{0:stamina, 1:tenacity, 2:agility, 3:accuracy, 4:precision, 5:reaction}}
	writeData()


def removePlayer(player):
	data.pop(f'{player}', None)
	writeData()


def plotGraph():
	x_labels = ["Stamina", "Tenacity", "Agility", "Accuracy", "Precision", "Reaction"]
	y_values = {}

	for p in list(data):
		player = p
		y_values[f'{player}'] = []
		for i in range(6):
			y_values[f'{player}'].append(data[f'{player}']['1'][f'{i}'])
			
		mplot.plot(x_labels, y_values[f'{player}'], label=data[f'{player}']['0'], linewidth=0.5, marker='o', markersize=2)

	mplot.title("osu!stats")
	mplot.legend()
	mplot.show()

def find_missing(players):
	players = [int(i) for i in players]
	return [x for x in range(players[0], players[-1]+1) if x not in players]

def doTask(c):
	if c == "1":
		name = input("Name: ")
		stamina = int(input("Stamina: "))
		tenacity = int(input("Tenacity: "))
		agility = int(input("Agility: "))
		accuracy = int(input("Accuracy: "))
		precision = int(input("Precision: "))
		reaction = int(input("Reaction: "))
		newPlayer(name, stamina, tenacity, agility, accuracy, precision, reaction)
	elif c == "2":
		player = input("Player index: ")
		removePlayer(player)
	elif c == "4":
		plotGraph()
	else:
		sys.exit(0)

def main():

	print("""	1) Add a new player
	2) Remove a player
	3) Show all players
	4) Plot osu!stats graph
""")
	c = input(">> ")
	doTask(c)
		

if __name__ == '__main__':
	main()
