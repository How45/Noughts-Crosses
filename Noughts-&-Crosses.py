from graphics import *

# Grid /--------------------------------------------------------------------------------------\
def GridLayout(win):
	lst = []

	for column in range(0,300,100):
		for row in range(0,300,100):
			tepLst = []
			tepLst.extend([row,column,row+100,column+100])

			square = Rectangle(Point(row, column), Point(row+100, column+100))
			square.draw(win)

			lst.append(tepLst)

	return lst

# Draw Cross /--------------------------------------------------------------------------------------\
def DrawCross(win,lst):
	line = Line(Point(lst[0],lst[1]),Point(lst[2],lst[3]))
	line.draw(win)

	line2 = Line(Point(lst[0],lst[3]),Point(lst[2],lst[1]))
	line2.draw(win)
# Player One /--------------------------------------------------------------------------------------\
def CrossPoint(win,lst,bLst,cLst):
	checkSame = False
	index = 0

	while index != 1:
		lstCount = 0
		user = win.getMouse()

		for i in lst:
			if user.x>i[0] and user.y>i[1] and user.x<i[2] and user.y<i[3]:
				checkSame = CheckIfRepeat(i,cLst)
				break
			else:
				lstCount += 1

		if checkSame == False:
			cLst.append(i)
			bLst[lstCount] = 1
			DrawCross(win,i)
			index = 1

		elif checkSame == True:
			print("Can't do it there")

	return cLst,bLst

# Draw Circle /--------------------------------------------------------------------------------------\
def DrawCirlce(win,lst):
	circle = Circle(Point(lst[0]+50,lst[1]+50),50)
	circle.draw(win)
# PlayerTwo /--------------------------------------------------------------------------------------\
def CirlcePoint(win,lst,bLst,cLst):
	checkSame = False
	index = 0

	while index == 0:
		lstCount = 0
		user = win.getMouse()

		for i in lst:
			if user.x>i[0] and user.y>i[1] and user.x<i[2] and user.y<i[3]:
				checkSame = CheckIfRepeat(i,cLst)
				break
			else:
				lstCount += 1

		if checkSame == False:
			cLst.append(i)
			bLst[lstCount] = 2
			DrawCirlce(win,i)
			index = 1

		elif checkSame == True:
			print("Can't do it there")

	return cLst,bLst

# BotTurn /--------------------------------------------------------------------------------------\
def BotPick(win,lst,bLst,cLst):

	# Pick Winning position
	for i in range(len(lst)):
		winLst = bLst[:]

		if winLst[i-1] == 0:
			winLst[i-1] = 2

			if CheckWin(winLst,2) == False:
				DrawCirlce(win,lst[i-1])
				cLst.append(lst[i-1])
				bLst[i-1] = 2
				return cLst,bLst
			else:
				winLst[i-1] = 3

	# Sees if Opponet is gonna win
	for i in range(len(lst)):
		blockLst = bLst[:]

		if blockLst[i-1] == 0:
			blockLst[i-1] = 1

			if CheckWin(blockLst,1) == False:
				DrawCirlce(win,lst[i-1])
				cLst.append(lst[i-1])
				bLst[i-1] = 2
				return cLst,bLst
			else:
				blockLst[i-1] = 3

	# Random on the free spaces
	while (True):
		import random
		r = random.randrange(0,4)

		if r == 1:
			# Mid
			if CheckIfRepeat(lst[4],cLst) != True:
				cLst.append(lst[4])
				bLst[4] = 2
				DrawCirlce(win,lst[4])
				return cLst,bLst
		elif r == 2:
			# Corners
			for i in [0,2,6,8]:
				if CheckIfRepeat(lst[i],cLst) != True:
					cLst.append(lst[i])
					bLst[i] = 2
					DrawCirlce(win,lst[i])
					return cLst,bLst
		elif r == 3:
			# OuterMid
			for i in [1,3,5,7]:
				if CheckIfRepeat(lst[i],cLst) != True:
					cLst.append(lst[i])
					bLst[i] = 2
					DrawCirlce(win,lst[i])
					return cLst,bLst

# Checking Stuff /--------------------------------------------------------------------------------------\
def CheckIfRepeat(lst,clst):
	for i in clst:
		if lst == i:
			return True
	return False

def CheckWin(wlst,num):

	if (wlst[0] == num and wlst[1] == num and wlst[2] == num) or (wlst[3] == num and wlst[4] == num and wlst[5] == num) or (wlst[6] == num and wlst[7] == num and wlst[8] == num) or (wlst[0] == num and wlst[3] == num and wlst[6] == num) or (wlst[1] == num and wlst[4] == num and wlst[7] == num) or (wlst[2] == num and wlst[5] == num and wlst[8] == num) or (wlst[0] == num and wlst[4] == num and wlst[8] == num) or (wlst[2] == num and wlst[4] == num and wlst[6] == num):
		return False

	return True

def CheckDraw(wLst):
	draw = 0
	for i in wLst:
		if i != 0:
			draw += 1

		if draw == 9:
			return False
	return True

# Main /--------------------------------------------------------------------------------------\
def main():
	win = GraphWin("Noughts&Crosses",300,300)
	winGrid = [0,0,0,
			   0,0,0,
			   0,0,0] # Contaias the points were the player has placed something (Atm no one has done anything)

	lstGridLayout = GridLayout(win) # [[0,0,100,100],[100,0,200,200],...,[200,200,300,300]]
	checkLst = [] # This will look like lstGridLayout if there is a draw (A cord is added each time a player places a X or O)
	draw = 0

	while(True):

		checkLst, winGrid = CrossPoint(win,lstGridLayout,winGrid,checkLst)
		winner = CheckWin(winGrid,1)
		draw = CheckDraw(winGrid)

		if winner == False:
			print("X Won!")
			win.close()
			break

		if draw == False:
			print("Draw")
			win.close()
			break

		# checkLst, winGrid = CirlcePoint(win,lstGridLayout,winGrid,checkLst)
		checkLst, winGrid = BotPick(win,lstGridLayout,winGrid,checkLst)
		winner = CheckWin(winGrid,2)

		if winner == False:
			print("O Won!")
			win.close()
			break

	print("GG, Play Again?")
	print("Well you cant")
main()

# AI ALgorithm
# 	We wanna check if we can win (if cant) V
#  	We wanna check if player might win and block him (if player has no possible moves to win) V
