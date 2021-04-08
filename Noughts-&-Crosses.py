from graphics import *

def GridLayout(win):
	lst = []

	for colum in range(0,300,100):
		for row in range(0,300,100):
			tepLst = []
			tepLst.extend([row,colum,row+100,colum+100])

			square = Rectangle(Point(row, colum), Point(row+100, colum+100))
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


# Main /--------------------------------------------------------------------------------------\
def main():
	win = GraphWin("My Circle",300,300)
	winGrid = [0,0,0,
			   0,0,0,
			   0,0,0]

	lstGridLayout = GridLayout(win)
	checkLst = []

	while(True):
		checkLst, winGrid = CrossPoint(win,lstGridLayout,winGrid,checkLst)

		checkLst, winGrid = CirlcePoint(win,lstGridLayout,winGrid,checkLst)
		print(winGrid)
main()
