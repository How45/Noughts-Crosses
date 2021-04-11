from graphics import *

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

def CheckIfRepeat(lst,clst):
	for i in clst:
		if lst == i:
			return True
	return False

def CheckWin(wlst,num):

	if wlst[0] == num and wlst[1] == num and wlst[2] == num: # X axis
		return False
	elif wlst[3] == num and wlst[4] == num and wlst[5] == num:
		return False
	elif wlst[6] == num and wlst[7] == num and wlst[8] == num:
		return False

	elif wlst[0] == num and wlst[3] == num and wlst[6] == num: # Y axis
		return False
	elif wlst[1] == num and wlst[4] == num and wlst[7] == num:
		return False
	elif wlst[2] == num and wlst[5] == num and wlst[8] == num:
		return False

	elif wlst[0] == num and wlst[4] == num and wlst[8] == num:
		return False
	elif wlst[2] == num and wlst[4] == num and wlst[6] == num:
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
def Game():
	win = GraphWin("Noughts&Crosses",300,300)
	winGrid = [0,0,0,
			   0,0,0,
			   0,0,0]

	lstGridLayout = GridLayout(win)
	checkLst = []
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

		checkLst, winGrid = CirlcePoint(win,lstGridLayout,winGrid,checkLst)
		winner = CheckWin(winGrid,2)

		if winner == False:
			print("O Won!")
			win.close()
			break

	print("GG, Play Again?")
Game()
