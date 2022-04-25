import os, sys

boardStandard = [
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",], #  -
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",], #  +
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",], #  -
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",], #  +
] #10+4 rows, 30 long

backBoardStandard = [
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",], #  -
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",], #  +
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",], #  -
	[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",], #  +
] #for electrical currents
#PRINT EACH VALUE WITH 5 CHARACTERS

tableStandard = [
	[" "," "," "],
	[" "," "," "],
	[" "," "," "],
	[" "," "," "],
	[" "," "," "],
] #3x3, for things like laptops, screens, etc. 

"""
		"item": {
			"description": "desc",
			"character": "char",
		},
"""

catalog = {
	"board": {
		"jumper cables": {
			"description": "connects 2 points on the board or from the board to the laptop input",
			"character": "J",
		},
		"LCD power": {
			"description": "power for LCD screen, needs 5v",
			"character": "LCDv",
		},
		"LCD ground": {
			"description": "ground for LCD screen",
			"character": "LCDg",
		},
		"sound sensor power": {
			"description": "powers the sound sensor",
			"character": "SNDp",
		},
		"sound sensor ground": {
			"description": "ground for the sound sensor",
			"character": "SNDg",
		},
		"sound sensor": {
			"description": "senses sound and outputs the decibels",
			"character": "SND",
		},
	},
	"table": {
		"LCD screen": {
			"description": "a screen that shows text",
			"character": "LCD",
		},
		"LCD input": {
			"description": "text input for LCD screen, needs to come from laptop, needs to be next to LCD screen",
			"character": "LCDi",
		},
		"laptop": {
			"description": "processes text for inputs",
			"character": "LPT",
		},
		"laptop input": {
			"description": "connects inputs to the laptop via jumper cables, needs to be next to the laptop",
			"character": "LPTi",
		},
	},
}
#for multiple items, add number after, such as J1, J2, J3, etc.

class Board:
	def __init__(self,boardType,backBoard,table):
		self.table = table.copy()
		if len(boardType) != len(backBoard):
			input(f"uERROR in class <Board> func. __init__: \nboardType != backBoard")
			return
		self.board = boardType.copy()
		self.backBoard = backBoard.copy()
	def findCurrent(self,boardCoords: tuple):
		#format: (row,column)
		if boardCoords[0] > len(self.board)-1:
			print(f"uERROR in classe <Board> func. findCurrent:\nboardCoords[0] too large\nboardCoords[0] == {boardCoords[0]}")
			sys.exit()
		if boardCoords[1] > len(self.board[0])-1:
			print(f"uERROR in classe <Board> func. findCurrent:\nboardCoords[1] too large\nboardCoords[1] == {boardCoords[1]}")
			sys.exit()
		if boardCoords[0] in [0,1,len(self.board),len(self.board)-1]:
			powered = False
			for i in self.backBoard[1]:
				if i == "5" or i == "3.3":
					return True
			for i in self.backBoard[0]:
				if i == "5" or i == "3.3":
					return True
			for i in self.backBoard[len(self.board)]:
				if i == "5" or i == "3.3":
					return True
			for i in self.backBoard[len(self.board)-1]:
				if i == "5" or i == "3.3":
					return True
		else:
			row,col = 0,0
			for i in self.backBoard:
				for x in i:
					for z in range(len(self.board)):
						if z in [0,1,len(self.board),len(self.board)-1]: continue
						if self.backBoard[z][col] == "5" or self.backBoard[z][col] == "3.3":
							return True
					col += 1
				row += 1
		if self.backBoard[boardCoords[0]][boardCoords[1]] == "5": return "5"
		if self.backBoard[boardCoords[0]][boardCoords[1]] == "3.3": return "3.3"
	def printBoard(self):
		row,col = 0,0
		for i in self.board:
			if row == 2 or row == len(self.board)-2: print()
			for x in i:
				if x == " ": x = "[]"
				paste = str(x)
				if len(x) != 5:
					if len(x) % 2 == 1:
						paste = f"{((5-len(x))//2)*' '}{x}{((5-len(x))//2)*' '}"
					else:
						paste = f"{((5-len(x))//2-1)*' '}{x}{((5-len(x))//2)*' '}"
					#print(f"P:{paste.replace(' ','-')}")
				sys.stdout.write(paste)
				sys.stdout.flush()
				col += 1
			print()
			row += 1
	def printTable(self):
		for i in self.table:
			pass

def clear(): os.system("cls" if os.name == "nt" else "clear")

colors = {
	"black": "\u001b[30;1m",
	"red": "\u001b[31;1m",
	"green": "\u001b[32;1m",
	"yellow": "\u001b[33;1m",
	"blue": "\u001b[34;1m",
	"magenta": "\u001b[35;1m",
	"cyan": "\u001b[36;1m",
	"white": "\u001b[37;1m",
	"reset": "\u001b[0m",
}

board1 = Board(boardStandard,backBoardStandard,tableStandard)
board1.backBoard[0][0] = "5"
print(board1.findCurrent((3,2)))
#board1.printBoard()
